"""
For each azure (color 8) object:
1. Locate the *lowest* row of the azure object.
2. Identify the *right-most* pixel on that row.
3. Color the cell to the *left* of this identified cell to blue (color 1).
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(row, col):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != color:
            return []

        visited.add((row, col))
        object_pixels = [(row, col)]

        object_pixels.extend(dfs(row + 1, col))
        object_pixels.extend(dfs(row - 1, col))
        object_pixels.extend(dfs(row, col + 1))
        object_pixels.extend(dfs(row, col - 1))

        return object_pixels
    
    for r in range(grid.shape[0]):
      for c in range(grid.shape[1]):
        if grid[r,c] == color and (r,c) not in visited:
          objects.append(dfs(r,c))

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule described above.
    """
    output_grid = np.copy(input_grid)
    azure_objects = get_objects(input_grid, 8)

    for obj in azure_objects:
        # Find the bottom-most row
        bottom_most_row = max(r for r, c in obj)
        #get all pixels in that row
        bottom_pixels = [(r, c) for r, c in obj if r == bottom_most_row]

        # Find the right-most pixel in the bottom row
        rightmost_pixel = max(bottom_pixels, key=lambda p: p[1])

        # Color the cell to the left of the rightmost pixel blue, with boundary checks
        r, c = rightmost_pixel
        if c > 0:  # Check if there's a cell to the left
            output_grid[r, c - 1] = 1

    return output_grid