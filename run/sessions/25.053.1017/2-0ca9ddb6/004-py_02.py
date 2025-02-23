"""
1.  **Preserve Azure:** Keep any azure (8) pixels in their original positions.

2.  **Orange Crosses:** For each blue (1) pixel in the input:
    *   Create an orange (7) pixel at the same location in the output.
    *   Extend an orange (7) "cross" shape: one pixel up, down, left, and right from the original blue pixel's location, but only if those locations are within the grid bounds and not occupied by the azure (8) pixel.

3.  **Yellow Diagonals:** For each red (2) pixel in the input:
    * Create a yellow pixel one step diagonally up and to the right.
    * Create a yellow pixel one step diagonally down and to the left.

4. **Maintain Input:** Keep any red and blue pixels in their original position.

5.  **Fill Remaining:** All other pixels remain white (0).
"""

import numpy as np

def find_pixels(grid, color):
    """Finds the locations of all pixels of a given color."""
    return np.argwhere(grid == color).tolist()

def is_valid(row, col, shape):
    """Checks if a given row and column are within the grid bounds."""
    return 0 <= row < shape[0] and 0 <= col < shape[1]

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Preserve Azure (rule 1)
    # azure pixels are already in place due to the copy

    # Orange Crosses (rule 2)
    blue_pixels = find_pixels(input_grid, 1)
    for row, col in blue_pixels:
        output_grid[row, col] = 7  # Center of the cross
        # Extend the cross
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col, (rows, cols)) and input_grid[new_row,new_col] != 8:
                output_grid[new_row, new_col] = 7

    # Yellow Diagonals (rule 3)
    red_pixels = find_pixels(input_grid, 2)
    for row, col in red_pixels:
        #output_grid[row,col] = 2
        for dr, dc in [(1, 1), (-1, -1)]:
          new_row, new_col = row+dr, col+dc
          if is_valid(new_row, new_col, (rows, cols)):
            output_grid[new_row,new_col] = 4

    #Rule 4 already done - we operate on a copy
    
    return output_grid