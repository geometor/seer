"""
1.  **Identify the Target Object:** Locate the largest contiguous block of green (3) pixels within the input grid. This forms the primary object.

2.  **Identify inside pixels.** A pixel is considered to be on the inside of the
    object if is it part of a contiguous block of green pixels and is fully
    surrounded horizontally and vertically by other green pixels from the
    object.

3.  **Modify Pixel Colors:** Traverse the identified interior green pixels. Change the color
    of the pixel from green (3) to yellow (4).

4. **Leave other pixels unchanged.** All pixels which are not inside of the
   main green object remain unchanged.
"""

import numpy as np

def find_largest_object(grid, color):
    visited = np.zeros_like(grid, dtype=bool)
    max_size = 0
    largest_object_coords = []

    def dfs(row, col, current_object_coords):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return 0

        visited[row, col] = True
        current_object_coords.append((row, col))
        size = 1
        size += dfs(row + 1, col, current_object_coords)
        size += dfs(row - 1, col, current_object_coords)
        size += dfs(row, col + 1, current_object_coords)
        size += dfs(row, col - 1, current_object_coords)
        return size

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object_coords = []
                current_size = dfs(row, col, current_object_coords)
                if current_size > max_size:
                    max_size = current_size
                    largest_object_coords = current_object_coords

    return largest_object_coords

def is_inside(grid, row, col, object_coords, color):
    if (row, col) not in object_coords:
        return False

    # Check boundaries
    if row <= 0 or row >= grid.shape[0] - 1 or col <= 0 or col >= grid.shape[1] - 1:
        return False
    
    #check neighbors
    if (grid[row + 1, col] != color or
        grid[row - 1, col] != color or
        grid[row, col+1] != color or
        grid[row, col-1] != color):
        return False

    return True
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find largest green object
    green_object_coords = find_largest_object(input_grid, 3)
    
    # change interior object pixels to yellow
    for row, col in green_object_coords:
      if is_inside(input_grid, row, col, green_object_coords, 3):
        output_grid[row, col] = 4

    return output_grid