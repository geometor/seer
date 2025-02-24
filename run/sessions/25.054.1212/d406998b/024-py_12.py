"""
Transforms an input grid by replacing the first gray (5) pixel with a green (3) pixel in every other group of consecutive gray pixels within each row, starting with the first group. Non-gray pixels act as separators between groups.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input
    rows, cols = input_grid.shape

    for r in range(rows):
        replace_group = True  # Flag to indicate whether to replace in the current group. Start by replacing the FIRST group.
        group_start_col = -1

        for c in range(cols):
            if output_grid[r, c] == 5:  # Check if the pixel is gray
                if group_start_col == -1:
                    group_start_col = c  # Mark the start of a new group
                # We don't need a counter, just the start of the group
            else: # Non-gray pixel, process any previous group
                if group_start_col != -1:  # If we were in a gray group
                    if replace_group:
                        output_grid[r, group_start_col] = 3  # Replace the first gray pixel
                    replace_group = not replace_group  # Toggle for the next group
                group_start_col = -1  # Reset group start

        # Handle any remaining group at the end of the row
        if group_start_col != -1:  # If the row ended within a gray group
            if replace_group:
                output_grid[r, group_start_col] = 3  # Replace the first gray pixel

    return output_grid