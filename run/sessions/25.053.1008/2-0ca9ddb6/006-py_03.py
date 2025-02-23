"""
1.  **Iterate** through each non-white pixel in the input grid.
2.  **Check** color of pixel, for each non-white pixel:
    *   If the pixel is blue (1), add orange (7) pixels to its top, bottom, left, and right.
    *   If the pixel is red (2), add a yellow (4) pixel to top and left
    *   If the pixel is magenta (6), don't add any pixels.
3.  **Preserve** all the original, input pixels in the output grid.
4. If the neighbors are outside the grid, the pixels are not drawn.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel
    for i in range(rows):
        for j in range(cols):
            current_pixel = input_grid[i, j]

            # Check color and add pixels accordingly
            if current_pixel == 1:  # Blue
                # Add orange pixels around
                if i > 0:
                    output_grid[i - 1, j] = 7
                if i < rows - 1:
                    output_grid[i + 1, j] = 7
                if j > 0:
                    output_grid[i, j - 1] = 7
                if j < cols - 1:
                    output_grid[i, j + 1] = 7
            elif current_pixel == 2: # Red
                if i > 0:
                    output_grid[i-1,j] = 4
                if j > 0:
                    output_grid[i,j-1] = 4
            elif current_pixel == 6:
                pass

    return output_grid