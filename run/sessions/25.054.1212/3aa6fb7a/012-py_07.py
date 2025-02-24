"""
Identifies horizontal lines of exactly two contiguous azure (8) pixels and adds a
blue (1) pixel to the immediate left or right of the line, replacing a white (0)
pixel, if one exists. The choice of left or right depends on the presence of
white pixels above the ends of the azure line.
"""

import numpy as np

def find_two_azure_lines(grid):
    # type: (np.ndarray) -> list
    """Finds all horizontal lines of exactly two contiguous azure (8) pixels."""
    rows, cols = grid.shape
    two_azure_lines = []
    for row in range(rows):
        for col in range(cols - 1):  # Iterate up to the second-to-last column
            if grid[row, col] == 8 and grid[row, col + 1] == 8:
                #check that there are no other azure pixels next to this line
                is_two_pixel_line = True
                if col > 0: #check left
                    if grid[row, col-1] == 8:
                        is_two_pixel_line = False
                if col < cols - 2:
                    if grid[row, col+2] == 8:
                        is_two_pixel_line = False
                if is_two_pixel_line:
                    two_azure_lines.append((row, col, row, col + 1))  # Store start and end coordinates
    return two_azure_lines

def transform(input_grid):
    # type: (np.ndarray) -> np.ndarray
    """Transforms the input grid by adding blue pixels to the left or right of two-pixel azure lines."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all two-pixel azure lines
    azure_lines = find_two_azure_lines(input_grid)

    # Iterate through each identified line
    for line in azure_lines:
        row_start, col_start, row_end, col_end = line

        # Check for white pixel to the left and right
        left_white = col_start > 0 and output_grid[row_start, col_start - 1] == 0
        right_white = col_end < cols - 1 and output_grid[row_end, col_end + 1] == 0

        # Check for white pixels above the left and right ends
        above_left_white = row_start > 0 and grid[row_start - 1, col_start] == 0
        above_right_white = row_start > 0 and grid[row_start - 1, col_end] == 0


        if right_white and not left_white:
            # only right is an option
            output_grid[row_end, col_end + 1] = 1
        elif left_white and not right_white:
            # only left is an option
            output_grid[row_start, col_start - 1] = 1
        elif left_white and right_white:
            # Both sides are white, apply the priority rule
            if not above_left_white and above_right_white:
                output_grid[row_end, col_end + 1] = 1  # Add to the right
            else:
                output_grid[row_start, col_start - 1] = 1  # Add to the left

    return output_grid