"""
The color 4 (yellow) cell creates a mirrored "E" (or "3") pattern repeated vertically.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by expanding the yellow (4) cell into a "3" shaped pattern.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the input grid to find the seed cell (color 4)
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 4:
                # Create the "3" pattern for yellow (4)
                for i in range(3):  # Iterate every other row
                    if r + i * 2 < rows:
                      output_grid[r + i*2, c] = 4
                      if c-1 >=0: output_grid[r + i*2, c - 1] = 4
                      if c+1 < cols: output_grid[r + i*2, c + 1] = 4

    return output_grid