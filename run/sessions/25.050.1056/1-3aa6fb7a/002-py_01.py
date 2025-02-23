"""
The azure colored objects are maintained from the input grid to the output grid.
A blue pixel is placed in the grid at the top left corner and at the bottom right corner of the azure colored cluster.
"""

import numpy as np

def find_azure_objects(grid):
    """
    Finds the positions of azure (color 8) pixels in the grid.
    """
    azure_positions = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 8:
                azure_positions.append((i, j))
    return azure_positions

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Azure objects are preserved.
    - Blue pixels are placed at the top-left and bottom-right corners of azure clusters.
    """
    output_grid = np.copy(input_grid)
    azure_positions = find_azure_objects(input_grid)

    if azure_positions:
      #find top-left and bottom-right corners
      min_row = min(pos[0] for pos in azure_positions)
      min_col = min(pos[1] for pos in azure_positions)
      max_row = max(pos[0] for pos in azure_positions)
      max_col = max(pos[1] for pos in azure_positions)

      output_grid[min_row, min_col] = 1 # top-left
      output_grid[max_row,max_col] = 1 # bottom-right

    return output_grid