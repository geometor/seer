"""
Transforms an input grid by replacing every third gray (5) pixel in each row with a green (3) pixel. White (0) pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input
    rows, cols = input_grid.shape

    for r in range(rows):
        gray_count = 0 # Counter for gray pixels in the current row
        for c in range(cols):
            if output_grid[r, c] == 5:  # Check if the pixel is gray
                gray_count += 1
                if gray_count % 3 == 0:  # Check if it's the third gray pixel
                    output_grid[r, c] = 3  # Replace with green
            # White pixels (0) are implicitly kept unchanged by copying the input_grid

    return output_grid