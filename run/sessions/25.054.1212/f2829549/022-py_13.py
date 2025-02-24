"""
1.  **Input and Output:** The input is a 4x7 grid, and the output is a 4x3 grid.
2.  **Row-wise Transformation:** For each row in the input grid:
    *   Check if the color orange (7) is present in any of the first three columns.
    *   If orange is found in any of the first three columns, check the values in each of these columns:
        *   If the cell is orange, change it to green.
        *   Otherwise, change it to white.
    *   If orange is not found, the output row becomes all white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid
    output_grid = np.zeros((4, 3), dtype=int)

    # Iterate through each row of the input grid
    for i in range(input_grid.shape[0]):
        # Check for orange in the first three columns of the current row
        orange_present = False
        for j in range(3):
            if input_grid[i, j] == 7:
                orange_present = True
                break

        # Transform the row based on the presence of orange
        if orange_present:
            for j in range(3):
                if input_grid[i, j] == 7:
                    output_grid[i, j] = 3  # Change orange to green
                else:
                    output_grid[i, j] = 0  # Change other colors to white
        else:
            output_grid[i, :] = 0  # Set entire row to white

    return output_grid