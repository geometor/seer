"""
1.  **Identify Azure Objects:** Find all contiguous regions (objects) of azure (color 8) pixels in the input grid.
2.  **Find Rightmost Pixels:** For each azure object, determine the pixel(s) with the largest column index (the rightmost pixel(s) of that object). There can be multiple "rightmost" pixels if they share the same column.
3.  **Insert Single Blue Pixel:** For each *object*, if the rightmost pixel's column index + 1 is within the grid boundaries, insert a *single* blue (color 1) pixel into the output grid at the location (row of the rightmost pixel, column index of the rightmost pixel + 1).
4. shift all values in that row, right of the column to the right by 1
5. If the output grid at the insertion point is not already blue, copy the shifted value, otherwise leave as is
"""

import numpy as np

def get_objects(grid, color):
    """
    Find contiguous regions of the specified color.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        # Explore adjacent cells
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_rightmost_pixels(object_coords):
    """
    Finds the rightmost pixel(s) of an object.  Handles cases where multiple pixels
    share the maximum column index.
    """
    if not object_coords:
        return []
    max_col = max(c for r, c in object_coords)
    return [(r, c) for r, c in object_coords if c == max_col]

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)


    # 1. Identify Azure Objects
    azure_objects = get_objects(input_grid, 8)

    # 2. Find Rightmost Pixels and 3. Insert Blue Pixel
    for obj in azure_objects:
        rightmost_pixels = find_rightmost_pixels(obj)
        if rightmost_pixels:  # Check if the object exists
            # Use the row of the first rightmost pixel (they all should have the same row if they are connected)
            r, c = rightmost_pixels[0]
            if c + 1 < cols:  # Check boundary
                insert_col = c + 1
                # 4. Shift and copy
                for col_idx in range(cols):
                    if col_idx < insert_col:
                        output_grid[r,col_idx] = input_grid[r,col_idx]
                    elif col_idx == insert_col:
                        output_grid[r, col_idx] = 1  # Insert blue pixel

                    elif col_idx > insert_col:
                        if input_grid[r, col_idx-1] != 1: # only shift non-blue
                           output_grid[r,col_idx] = input_grid[r, col_idx-1]



    # copy any rows that did not have a shift
    for row_idx in range(rows):
        if not any(r == row_idx for obj in azure_objects for r, _ in obj):
            output_grid[row_idx, :] = input_grid[row_idx, :]

    return output_grid