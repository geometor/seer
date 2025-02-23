"""
1. **Identify Green Regions:** Locate all contiguous regions of green (3) pixels within the 20x20 grid.
2. **Inner Infill:** For each green region, identify any green pixel that is completely surrounded by other green pixels (up, down, left, and right). Change these inner green pixels to yellow (4).
3. **Diagonal Infill:** In addition, change to yellow any green pixel that has at least two green pixels diagonally adjacent to it.
4. **Preserve Others:**  All other pixels, including the white background (0) and green pixels not meeting the "inner" or diagonal infill criteria, remain unchanged.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the neighbors (including diagonals) of a cell."""
    neighbors = []
    rows, cols = grid.shape
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append(grid[i, j])
    return neighbors

def get_diagonal_neighbors(grid, row, col):
    """Gets only the diagonal neighbors of a cell"""
    neighbors = []
    rows, cols = grid.shape
    for i in range(-1,2,2):
        for j in range(-1,2,2):
          if 0 <= row + i < rows and 0 <= col + j < cols:
                neighbors.append(grid[row+i, col+j])

    return neighbors

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is green (3)
            if input_grid[row, col] == 3:
                neighbors = get_neighbors(input_grid, row, col)
                # Inner Infill: Check for surrounding green pixels
                if all(neighbor == 3 for neighbor in neighbors):
                    output_grid[row, col] = 4  # Change to yellow (4)
                else:
                  # count diagonal neighbors
                  diagonal_neighbors = get_diagonal_neighbors(input_grid, row, col)
                  count_green = sum( 1 for dn in diagonal_neighbors if dn == 3)
                  if count_green >= 2:
                    output_grid[row,col] = 4


    return output_grid