"""
1.  **Mirroring and Initial Expansion**: Copy each non-white pixel from the input to the output, then "expand" the colors.
    *   Expand red (2) to all directly adjacent white pixels.
    *   Expand yellow (4) to all directly adjacent white pixels.
    *   Mirror the initial colored pixels positions across a vertical and a horizontal axis.

2.  **Adjacency Check and Gray Fill**: For each white (0) pixel in the *output* grid:
    *   Check if it is adjacent to at least one non-white pixel.
    *   Check if the adjacent non-white pixels contain at least two different colors.
    *   If *both conditions are true*, replace the white pixel with gray (5). Otherwise, keep the current value of the pixel.
3. If the cell is not white and has not been changed to gray, maintain its input color in the output grid.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets the values of adjacent pixels (up, down, left, right)."""
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append(grid[row - 1, col])  # Up
    if row < rows - 1:
        adjacent.append(grid[row + 1, col])  # Down
    if col > 0:
        adjacent.append(grid[row, col - 1])  # Left
    if col < cols - 1:
        adjacent.append(grid[row, col + 1])  # Right
    return adjacent

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    # Mirror and initial placement
    for i in range(rows):
      for j in range(cols):
        if input_grid[i,j] != 0:
          output_grid[i,j] = input_grid[i,j]
          output_grid[i, cols-1-j] = input_grid[i,j]
          output_grid[rows-1-i, j] = input_grid[i,j]
          output_grid[rows-1-i, cols-1-j] = input_grid[i,j]


    # Expand Colors
    temp_grid = np.copy(output_grid)
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 0:  # Only expand onto white pixels
                adjacent = get_adjacent_pixels(output_grid, i, j)
                for adj_val in adjacent:
                  if adj_val == 2:
                      temp_grid[i,j] = 2
                  elif adj_val == 4:
                      temp_grid[i,j] = 4

    output_grid = np.copy(temp_grid)

    # Adjacency check and Gray Fill
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 0:
                adjacent = get_adjacent_pixels(output_grid, i, j)
                adjacent_colors = set(adjacent)
                adjacent_colors.discard(0)  # Remove white from consideration
                if len(adjacent_colors) >= 2:
                    output_grid[i, j] = 5

    return output_grid