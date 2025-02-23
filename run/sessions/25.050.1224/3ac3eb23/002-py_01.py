"""
The colors 2 (red) and 8 (azure) are expanded into a 3x3 pattern that creates a shape like '3' and is repeated downwards every other row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by expanding the red (2) and azure (8) cells into a "3" shaped pattern.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the input grid to find the seed cells (color 2 and 8)
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:
                # Create the "3" pattern for red (2)
                for i in range(3):  # Iterate every other row
                    if r + i * 2 < rows:
                      output_grid[r + i*2, c] = 2
                      if c-1 >=0: output_grid[r + i*2, c - 1] = 2
                      if c+1 < cols: output_grid[r + i*2, c + 1] = 2
            elif input_grid[r, c] == 8:
                # Create the "3" pattern for azure (8)
                for i in range(3):
                    if r + i*2 < rows:
                        output_grid[r + i*2, c] = 8
                        if c - 1 >= 0: output_grid[r + i * 2, c - 1] = 8
                        if c + 1 < cols: output_grid[r + i * 2, c + 1] = 8

    return output_grid