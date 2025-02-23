"""
1.  **Copy Unchanged:** If a pixel is azure (8) or magenta (6), copy it directly to the output grid at the same position.
2.  **Blue Pixel (1) Expansion:** For each blue pixel (1):
    *   Place an orange (7) pixel immediately to its left, right, above, and below, *only if the target cell is currently black/empty (0)*.
    *   Place a blue pixel (1) at the current location.
3.  **Red Pixel (2) Expansion:** For each red pixel (2):
    *   Place a yellow (4) pixel immediately to its left, right, above, and below, *only if the target cell is currently black/empty (0)*.
    *   Place a red pixel (2) at the current location.
4.  **Ignore other colors:** Pixels of colors other than 1, 2, 6, and 8 should not be directly processed or copied. The output grid starts filled with black (0).
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.zeros_like(input_grid)  # Initialize with zeros
    height = input_grid.shape[0]
    width = input_grid.shape[1]

    # Iterate through each cell of the input grid
    for r in range(height):
        for c in range(width):
            # Copy Unchanged: Azure (8) and Magenta (6)
            if input_grid[r, c] == 8 or input_grid[r, c] == 6:
                output_grid[r, c] = input_grid[r, c]
            # Blue Pixel (1) Expansion
            elif input_grid[r, c] == 1:
                # Place orange (7) to the left
                if c > 0 and output_grid[r, c - 1] == 0:
                    output_grid[r, c - 1] = 7
                # Place orange (7) to the right
                if c < width - 1 and output_grid[r, c + 1] == 0:
                    output_grid[r, c + 1] = 7
                # Place orange (7) above
                if r > 0 and output_grid[r - 1, c] == 0:
                    output_grid[r - 1, c] = 7
                # Place orange (7) below
                if r < height - 1 and output_grid[r + 1, c] == 0:
                    output_grid[r + 1, c] = 7
                # Place the blue pixel (1)
                output_grid[r,c] = 1
            # Red Pixel (2) Expansion
            elif input_grid[r, c] == 2:
                # Place yellow (4) above
                if r > 0 and output_grid[r - 1, c] == 0:
                    output_grid[r - 1, c] = 4
                # Place yellow (4) below
                if r < height - 1 and output_grid[r + 1, c] == 0:
                    output_grid[r + 1, c] = 4
                # Place yellow(4) to the left
                if c > 0 and output_grid[r, c - 1] == 0:
                  output_grid[r, c - 1] = 4
                # Place yellow(4) to the right
                if c < width - 1 and output_grid[r, c + 1] == 0:
                  output_grid[r, c + 1] = 4
                # Place the red pixel (2)
                output_grid[r,c] = 2

    return output_grid