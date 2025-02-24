"""
Transforms an input grid by extracting a three-column window centered around a blue (color 1) stripe. 
The blue color within this window is mapped to azure (8), and all other pixels in the window are set to 0.
If the blue stripe is on the edge, the window wraps around.
"""

import numpy as np

def find_blue_stripe_column(grid):
    """Finds the column index of the vertical blue stripe (color 1)."""
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == 1) or np.all(grid[:,j] == [0,1]) or np.all(grid[:,j] == [1,0]):
            return j
    return -1  # Return -1 if no blue stripe is found


def transform(input_grid):
    """Transforms the input grid according to the rule."""
    rows = input_grid.shape[0]
    cols = 3
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find the blue stripe column
    blue_stripe_col = find_blue_stripe_column(input_grid)

    if blue_stripe_col == -1:
        return output_grid  # All 0 if no blue stripe

    # Calculate window column indices with wrapping
    left_col = (blue_stripe_col - 1) % input_grid.shape[1]
    center_col = blue_stripe_col
    right_col = (blue_stripe_col + 1) % input_grid.shape[1]

    # Populate the output grid
    for i in range(rows):
        # Left column
        output_grid[i, 0] = 8 if input_grid[i, left_col] == 1 else 0
        
        # Center column
        output_grid[i, 1] = 8 if input_grid[i, center_col] == 1 else 0

        # Right column
        output_grid[i, 2] = 8 if input_grid[i, right_col] == 1 else 0

    return output_grid