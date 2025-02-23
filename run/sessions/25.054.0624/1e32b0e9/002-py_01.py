"""
Transforms an input grid by expanding azure (8) pixels.  Azure pixels expand 
by one layer around existing azure pixels. If an azure pixel is adjacent to a 
red (2) pixel, the azure region expands by adding azure pixels to *all*
adjacencies of the azure pixel.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighboring coordinates of a cell."""
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the described rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. & 2. Iterate through existing azure pixels and expand
    azure_pixels = np.argwhere(input_grid == 8)
    for row, col in azure_pixels:
        neighbors = get_neighbors(input_grid, row, col)
        for nr, nc in neighbors:
            if output_grid[nr, nc] == 0:  # If neighbor is white
                output_grid[nr, nc] = 8

    #3. & 4. Iterate through each red pixel
    red_pixels = np.argwhere(input_grid == 2)
    for row, col in red_pixels:
      neighbors = get_neighbors(input_grid, row, col)
      for nr, nc in neighbors:
        if output_grid[nr, nc] == 8:
          # 5. Expand azure, adjacent to red
          azure_neighbors = get_neighbors(input_grid, nr, nc)
          for anr, anc in azure_neighbors:
            output_grid[anr, anc] = 8


    return output_grid