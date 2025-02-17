"""
The transformation rule can be stated as follows:

For each azure (color 8) object, find its bottom-most, non-connected point. Change the adjacent right cell of this point to blue (color 1). If the right cell is already part of the azure object, or if the right cell is out of boundary, do nothing.
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
        # Find the bottom-most pixels
        bottom_most_y = max(y for x, y in obj)
        bottom_pixels = [(x, y) for x, y in obj if y == bottom_most_y]
        
        # Sort bottom pixels by x coordinate to check for connectivity
        bottom_pixels_sorted = sorted(bottom_pixels, key=lambda p: p[0])
        
        for pixel in bottom_pixels_sorted:
          x,y = pixel
          
          #consider only the rightmost pixels in connected components of bottom_pixels
          if (x+1,y) not in bottom_pixels_sorted:
            # color the cell to right in output, boundary check
            if x + 1 < output_grid.shape[0] and y+1 < output_grid.shape[1] and x+1 < input_grid.shape[0]:
                if (x + 1, y) not in obj: # Check for adjanceny to L
                    output_grid[x + 1, y] = 1
                    break

    return output_grid