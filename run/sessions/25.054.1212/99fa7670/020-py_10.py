"""
1.  **Identify Non-White Pixels:** Iterate through each pixel in the input grid. If a pixel is not white (0), proceed to the next step.
2.  **Expand to the Right:** For each non-white pixel, change the color of the pixels to its right in same row, to the same color, until a the end of row or another non-white pixel is encountered.
3.  **Output:** The resulting grid is the output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # iterate through each pixel in the grid
    for r in range(rows):
        for c in range(cols):
            # Identify Non-White Pixels
            if output_grid[r, c] != 0:
                # Expand to the Right
                current_color = output_grid[r, c]
                for c2 in range(c + 1, cols):
                    if output_grid[r, c2] == 0:
                        output_grid[r, c2] = current_color
                    else:
                        break  # Stop expansion if a non-white pixel is encountered

    return output_grid