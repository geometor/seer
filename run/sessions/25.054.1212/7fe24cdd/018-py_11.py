"""
The transformation expands a 3x3 input grid into a 6x6 output grid. Each cell in the input grid corresponds to a 2x2 block in the output grid. The values within each 2x2 block are determined as follows:

1.  Top-Left: The top-left cell of the 2x2 block has the same value as the corresponding input cell.

2.  Top-Right: The top-right cell of the 2x2 block has the same value as the input cell that is *to the right* of the corresponding input cell. If the current input cell is in the rightmost column, the top-right cell of the 2x2 block is 0.

3.  Bottom-Left: The bottom-left cell of the 2x2 block has the same value as the input cell *below* the current input cell. If the current input cell is in the bottom row, the bottom-left cell of the 2x2 block is 0.

4. Bottom-Right: The bottom-right cell of the 2x2 block is a copy of the top-right value from the 2x2 block directly above. If there is no block above (i.e. current input cell is in first row), then:
    * If there is a cell below and to the right of the current input cell, the bottom-right cell is set to that cell's value.
    * If the current cell is on the bottom edge, use the value to the right.
    * If the current cell is on the right edge, use the value below it.
    * If the current cell is the bottom-right corner, use the value of the current cell
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2 * rows, 2 * cols), dtype=int)

    for row in range(rows):
        for col in range(cols):
            # Top-left: Value of the input cell.
            output_grid[2*row][2*col] = input_grid[row][col]

            # Top-right: Value of the right neighbor (or 0 if at the right edge).
            if col + 1 < cols:
                output_grid[2*row][2*col + 1] = input_grid[row][col+1]
            else:
                output_grid[2*row][2*col + 1] = 0

            # Bottom-left: Value of the bottom neighbor (or 0 if at the bottom edge).
            if row + 1 < rows:
                output_grid[2*row + 1][2*col] = input_grid[row+1][col]
            else:
                output_grid[2*row + 1][2*col] = 0

            # Bottom-right: Copy from top-right of the block above, or use special logic for the first row.
            if row > 0:
                output_grid[2*row + 1][2*col + 1] = output_grid[2*(row-1) + 1][2*col + 1]
            else:  # First row logic
                if row + 1 < rows and col + 1 < cols:
                    output_grid[2*row+1][2*col+1] = input_grid[row+1][col+1]
                elif row + 1 == rows and col+1 < cols:
                    output_grid[2*row + 1][2 * col + 1] = input_grid[row][col+1]
                elif col + 1 == cols and row+1 < rows:
                    output_grid[2*row + 1][2 * col + 1] = input_grid[row+1][col]
                else:
                    output_grid[2*row + 1][2*col+1] = input_grid[row][col]

    return output_grid.tolist()