"""
1.  **Preservation:** The original red (2) and blue (1) pixels from the input grid are preserved in the output grid at their original locations.
2.  **Yellow (4) Generation:** For the red (2) pixel in the input, create two yellow (4) pixels one row above and one row below.
    Create two yellow pixels beside the original yellow pixels.
3. **Orange (7) Generation:** For the blue (1) pixel in the input, create four orange (7) pixels:
    *   one position directly above
    *   one position directly below
    *   one position to the left
    *   one position to the right.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    output_grid = np.copy(input_grid)  # Start with a copy to preserve original pixels

    # Iterate through the input grid to find trigger pixels
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 2:  # Red pixel
                # Yellow generation
                if r > 0:
                    output_grid[r - 1, c] = 4
                    if c>0:
                      output_grid[r-1,c-1] = 0
                    if c < output_grid.shape[1]-1:
                        output_grid[r - 1, c+1] =4

                if r < input_grid.shape[0] - 1:
                    output_grid[r + 1, c] = 4
                    if c>0:
                      output_grid[r+1,c-1]=0
                    if c < output_grid.shape[1]-1:
                        output_grid[r+1,c+1]=4
                if c > 0:
                  output_grid[r, c - 1] = 0

                if c < input_grid.shape[1] -1:
                    output_grid[r,c+1]=0

            elif input_grid[r, c] == 1:  # Blue pixel
                # Orange generation
                if r > 0:
                    output_grid[r - 1, c] = 7
                if r < input_grid.shape[0] - 1:
                    output_grid[r + 1, c] = 7
                if c > 0:
                    output_grid[r, c - 1] = 7
                if c < input_grid.shape[1] - 1:
                    output_grid[r, c + 1] = 7

    return output_grid