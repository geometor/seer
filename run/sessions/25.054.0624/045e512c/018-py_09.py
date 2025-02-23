"""
Transforms the input grid based on a set of rules, primarily focusing on how colored objects are mirrored, replicated, or otherwise altered based on their color. Gray objects remain unchanged.
"""

import numpy as np

def find_objects(grid):
    """Finds and returns a list of objects in the grid, along with their bounding boxes."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, color, obj_pixels, min_r, min_c, max_r, max_c):
        """Depth-first search to find contiguous pixels of the same color and update bounding box."""
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != color:
            return min_r, min_c, max_r, max_c
        visited.add((r, c))
        obj_pixels.append((r, c))
        min_r = min(min_r, r)
        min_c = min(min_c, c)
        max_r = max(max_r, r)
        max_c = max(max_c, c)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            min_r, min_c, max_r, max_c = dfs(r + dr, c + dc, color, obj_pixels, min_r, min_c, max_r, max_c)
        return min_r, min_c, max_r, max_c

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                obj_pixels = []
                min_r, min_c, max_r, max_c = dfs(r, c, grid[r, c], obj_pixels, r, c, r, c)
                objects.append({
                    'color': grid[r, c],
                    'pixels': obj_pixels,
                    'bounding_box': [(min_r, min_c), (max_r, max_c)]
                })
    return objects

def transform(input_grid):
    """Transforms the input grid according to the identified rules."""
    grid = np.array(input_grid)
    output_grid = np.copy(grid)  # Initialize with a copy of the input
    objects = find_objects(grid)
    rows, cols = grid.shape

    for obj in objects:
        color = obj['color']
        pixels = obj['pixels']
        bbox = obj['bounding_box']

        if color == 5:  # Gray objects
            continue # remain unchanged

        elif color == 4:  # Yellow
            for r, c in pixels:
                # Vertical line of 3
                output_grid[max(0, r - 1):min(rows, r + 2), c] = 4

        elif color == 8 or color == 3:  # Azure and Green
            for r, c in pixels:
                # Mirror vertically across the grid
                output_grid[r, cols - 1 - c] = color

        elif color == 6:  # Magenta
            for r, c in pixels:
              # Mirror vertically across the grid
              output_grid[r, cols -1 -c] = 6

        elif color == 2: # Red
            for r, c in pixels:
                # Mirror vertically and expand
                output_grid[r, cols - 1 - c] = 2  # Mirror
                # original pixel expansion
                min_r, min_c = max(0, r - 1), max(0, c-1)
                max_r, max_c = min(rows-1, r+1), min(cols-1,c)

                output_grid[min_r:max_r+1, max(0, (cols - 1 - c) -1)] = 2


        elif color == 1: #blue
            for r, c in pixels:
                min_r, min_c = max(0, r - 1), max(0, c - 1)
                max_r, max_c = min(rows - 1, r + 1), min(cols - 1, c + 1)
                output_grid[min_r:max_r+1, min_c:max_c+1] = 1


    return output_grid.tolist()