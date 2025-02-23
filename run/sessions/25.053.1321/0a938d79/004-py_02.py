"""
The output grid is created by identifying each non-white pixel in the input grid. 
For each non-white pixel, its color is extended downwards, filling the rest of its column. 
The rows below are filled, then, it continues extending by wrapping around to the top of the grid (row 0) and filling down. This continues until the original row of the pixel is reached.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by extending the color of each non-white pixel downwards, wrapping around rows.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Iterate through the input grid to find non-white pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                color = input_grid[r, c]
                # Extend the color downwards, wrapping around
                current_row = r
                while True:
                    output_grid[current_row, c] = color
                    current_row = (current_row + 1) % rows  # Wrap around to row 0
                    if current_row == r:
                        break  # Stop when we reach the original row

    return output_grid