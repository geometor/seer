"""
1.  **Iterate:** Examine each pixel in the input grid.
2.  **Locate Green and Red:** Identify pixels that are green (3) or red (2).
3.  **Horizontal Adjacency Check (Green then Red):** If a pixel is green (3) and the pixel immediately to its *right* is red (2), change *only* the green pixel to azure (8).
4.  **Horizontal Adjacency Check (Red then Green):** If a pixel is red (2) and the pixel immediately to its *right* is green (3), change *both* the red pixel and the green pixel to azure (8).
5.  **Preservation:** All other pixels remain unchanged. Do not evaluate cells after they have changed.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid based on adjacency rules for green and red pixels."""

    output_grid = np.copy(input_grid)  # Initialize output as a copy of input
    rows, cols = output_grid.shape
    changes = []

    for r in range(rows):
        for c in range(cols):
            # Check for Green then Red
            if c + 1 < cols and input_grid[r, c] == 3 and input_grid[r, c + 1] == 2:
                changes.append((r, c, 8))  # Change green to azure

            # Check for Red then Green
            elif c + 1 < cols and input_grid[r, c] == 2 and input_grid[r, c + 1] == 3:
                changes.append((r, c, 8))      # Change red to azure
                changes.append((r, c + 1, 8))  # Change green to azure

    for r, c, val in changes:
      output_grid[r,c] = val

    return output_grid