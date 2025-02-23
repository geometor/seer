"""
The transformation identifies objects of different colors in the input grid. If an object of one color has an adjacent different color, the "background" color is changed.
The background is defined as color 1 in example 1, color 4 in example 2, and color 8 in example 3.
"""

import numpy as np

def get_objects(grid):
    """Finds contiguous objects (non-background pixels) in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, color, obj_pixels):
        """Depth-first search to find contiguous pixels of the same color."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        obj_pixels.append((row, col))
        dfs(row + 1, col, color, obj_pixels)
        dfs(row - 1, col, color, obj_pixels)
        dfs(row, col + 1, color, obj_pixels)
        dfs(row, col - 1, color, obj_pixels)
        dfs(row + 1, col + 1, color, obj_pixels)  # Check diagonals
        dfs(row - 1, col - 1, color, obj_pixels)
        dfs(row + 1, col - 1, color, obj_pixels)
        dfs(row - 1, col + 1, color, obj_pixels)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col]:
                obj_pixels = []
                dfs(row, col, grid[row, col], obj_pixels)
                objects.append((grid[row,col], obj_pixels))
    return objects

def get_neighbors(grid, row, col):
    """Get the neighbors of a pixel, including diagonals."""
    neighbors = []
    for r in range(max(0, row - 1), min(grid.shape[0], row + 2)):
        for c in range(max(0, col - 1), min(grid.shape[1], col + 2)):
            if (r, c) != (row, col):
                neighbors.append(grid[r, c])
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find objects and background
    objects = get_objects(input_grid)
    background_color = input_grid[0,0] #infer background

    # Create a set of object colors excluding background
    object_colors = {color for color, _ in objects if color != background_color}

    # Iterate through each pixel
    for row in range(input_grid.shape[0]):
      for col in range(input_grid.shape[1]):
          #check if its background color
          if input_grid[row,col] == background_color:
            neighbors = get_neighbors(input_grid, row, col)
            for neighbor_color in neighbors:
              if neighbor_color != background_color:
                # found different neighbor, so change
                output_grid[row,col] = neighbor_color # take the value

    return output_grid