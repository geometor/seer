"""
1.  **Identify Key Objects:**  Find two key objects in the input:
    a.  A "preserved" object, usually located near the top-left but can be slightly offset.  This object's color and shape are *mostly* preserved, but it *can* be altered slightly.
    b.  An "expanding" object, usually located near the bottom or center, but its position can vary. This object's color fills a larger area in the output.
2.  **Preserve/Modify Top-Left Object:** Copy the "preserved" object to the output grid, maintaining its original shape and color. Minor changes are possible, so don't assume perfect preservation.
3.  **Expand Bottom/Center Object:** The "expanding" object expands, but not as a simple rectangle. The expansion seems to maintain the *aspect ratio* and general shape features of the original object, rather than simply stretching to fill the available space.
4.  **Internal Pixel Handling:**  The most complex part. If the "expanding" object contains "internal" pixels (pixels of a different color within its bounds), the positions of these internal pixels relative to the expanding object's boundaries *and to each other* must be considered. The expanded region contains a *scaled* version of the internal pixel arrangement, not just a direct copy.
5. **Overlap Prevention:** Ensure the expanding object does not overlap with the copied upper-left object, adjusting the placement accordingly.
"""

import numpy as np
from collections import Counter

def find_objects(grid):
    """Finds all distinct objects in a grid."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return []
        visited.add((row, col))
        region = [(row, col)]
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            region.extend(dfs(row + dr, col + dc, color))
        return region

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and grid[r, c] != 0:
                color = grid[r, c]
                objects.append((color, dfs(r, c, color)))
    return objects

def get_object_bounds(obj):
    """Calculates the bounding box of an object."""
    rows, cols = zip(*obj)
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return min_row, max_row, min_col, max_col

def find_internal_pixels(grid, obj):
    """Finds internal pixels within an object and returns their relative positions."""
    min_row, max_row, min_col, max_col = get_object_bounds(obj)
    internal_pixels = []
    obj_color = grid[obj[0]] # Get the color of the object itself
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if (r, c) in obj and grid[r, c] != obj_color:
                internal_pixels.append((r, c, grid[r,c])) #Store row, col and color
    return internal_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    objects = find_objects(input_grid)

    # 1. & 2. Identify and preserve/modify the top-left object
    top_left_object = None
    if objects:
      top_left_object = min(objects, key=lambda x: (x[1][0][0], x[1][0][1]))  # Find object with min row, then min col
      top_left_color, top_left_region = top_left_object

      for r, c in top_left_region:
          output_grid[r, c] = top_left_color

    # 3. & 4. Identify and expand the bottom/center object
    expansion_object = None
    if len(objects) > 1:
        # Find the object that is NOT the top-left object
        for obj_color, obj_region in objects:
            if obj_color != top_left_color: # or obj_region != top_left_region:
                expansion_object = (obj_color, obj_region)
                break

    if expansion_object:
        expansion_color, expansion_region = expansion_object
        min_row, max_row, min_col, max_col = get_object_bounds(expansion_region)
        internal_pixels = find_internal_pixels(input_grid, expansion_region)

        # Calculate expansion ratios, attempting to maintain aspect ratio
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        available_height = output_grid.shape[0] - (get_object_bounds(top_left_region)[1] if top_left_object else 0 ) - 2  # -2 for padding
        available_width = output_grid.shape[1] - 2

        height_ratio = available_height / height if height >0 else 1
        width_ratio = available_width / width if width > 0 else 1
        
        #limit expansion if we have an object above
        expansion_ratio = min(height_ratio, width_ratio)


        new_height = int(height * expansion_ratio)
        new_width = int(width * expansion_ratio)

        # Calculate new top-left corner for the expanded object (avoiding overlap)
        new_min_row = (get_object_bounds(top_left_region)[1] + 2) if top_left_object else 1  # +2 to avoid overlap with the first object
        new_min_col = 1 #start from left

        # Fill expanded region
        for r in range(new_min_row, min(new_min_row + new_height, output_grid.shape[0]-1)): #stay inside output
            for c in range(new_min_col, min(new_min_col + new_width, output_grid.shape[1]-1)):
                output_grid[r, c] = expansion_color

        # Place internal pixels based on scaled offsets
        for internal_r, internal_c, internal_color in internal_pixels:
            r_offset = internal_r - min_row
            c_offset = internal_c - min_col
            new_r = int(new_min_row + r_offset * expansion_ratio)
            new_c = int(new_min_col + c_offset * expansion_ratio)
            if 0 <= new_r < output_grid.shape[0] and 0 <= new_c < output_grid.shape[1]: #stay inside
              output_grid[new_r, new_c] = internal_color

    return output_grid