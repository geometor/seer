"""
1. Identify Target Regions: Locate all white (0) pixels within the input grid.
2. Selective Removal: Remove only those white (0) pixels that form an enclosed shape. More precisely, if a shape formed of white pixels have at least one other colored pixel adjacent to the white pixel, either horizontally, vertically, or diagonally, those white pixels are removed.
3. Retain all other color and white pixels as they appear in the input grid.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Get the neighbors of a cell (including diagonals).
    """
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append(grid[i, j])
    return neighbors

def transform(input_grid):
    """
    Transforms the input grid by removing white pixels that are part of enclosed shapes.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is white (0)
            if input_grid[row, col] == 0:
                neighbors = get_neighbors(input_grid, row, col)
                # Check if any neighbor is not white
                if any(neighbor != 0 for neighbor in neighbors):
                  output_grid[row,col] = input_grid[row,col] # keep the white pixels in output
                if all(neighbor == 0 for neighbor in neighbors):
                    #remove isolated white pixels from the output
                    output_grid[row,col] = input_grid[row, col] # Keep isolated white cells
                if any(neighbor != 0 for neighbor in neighbors):
                    # Check for adjacent non-white pixels, change to match input if adjacent to one
                    output_grid[row, col] = 1 # we determined this wasn't correct and needed to change to white
    for row in range(rows):
      for col in range(cols):
        if input_grid[row,col] == 0:
          neighbors = get_neighbors(input_grid, row, col)
          if any(neighbor != 0 for neighbor in neighbors):
            output_grid[row,col] = input_grid[row,col]

    return output_grid