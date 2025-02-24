"""
Copies the bottom n-2 rows of the input grid to the output grid, where n is the number of rows in the input.
Fills the top two rows of the output grid with white pixels (0).
Fills the third row of the output grid with blue (1) where the corresponding column in the top three rows of the input grid was white (0), otherwise fills with white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input grid
    output_grid = np.zeros_like(input_grid)

    # Get the number of rows in the input grid
    num_rows = input_grid.shape[0]

    # Copy the bottom n-2 rows from input to output
    output_grid[2:] = input_grid[2:]

    # Fill the top two rows with white (0)
    output_grid[:2, :] = 0

    # Find where the input grid's top three rows are white (0)
    white_cols = np.where(input_grid[:3] == 0)

    # Create a set of columns where white pixels exist in the top three rows
    unique_white_cols = np.unique(white_cols[1])

    # Fill the third row based on the rule
    for col in range(input_grid.shape[1]):
        if col in unique_white_cols:
            output_grid[2, col] = 1  # Blue
        else:
            output_grid[2, col] = 0  # White

    return output_grid