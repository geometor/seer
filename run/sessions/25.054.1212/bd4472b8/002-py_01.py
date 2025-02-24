"""
The transformation rule is to replicate each color from the first row of the input grid twice, creating new rows with those colors. The second row of the input is copied unchanged.
"""

import numpy as np

def get_pattern_region(input_grid):
    # Find the last row with a non-zero value to define pattern region height.
    last_non_zero_row = -1
    for i in range(input_grid.shape[0]):
        if np.any(input_grid[i, :] != 0):
            last_non_zero_row = i
        else:
            break # stop looking after a row of zeros

    return input_grid[:last_non_zero_row+1, :]

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    # Identify the pattern region (rows with non-zero values at the top).
    pattern_region = get_pattern_region(input_grid)
    #print(f"{pattern_region=}")

    # Initialize the output grid with zeros, same dimensions as input.
    output_grid = np.zeros_like(input_grid)

    # Copy the original pattern region to the top of the output grid.
    output_grid[:pattern_region.shape[0], :] = pattern_region

    # Current row index in output grid to start adding replicated rows.
    current_row = pattern_region.shape[0]
    #print(f"{current_row=}")
    # Replicate colors from the first row.

    if pattern_region.shape[0] > 0:
        for color in pattern_region[0, :]:
            for _ in range(2):  # Create two copies of each color.
                output_grid[current_row, :] = color
                current_row += 1

    return output_grid