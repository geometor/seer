"""
1.  **Identify** the two non-zero values in the input grid's row containing non-zero values. Note their colors and positions.
2.  **Calculate** the midpoint index of this row.
3.  **Expand** the left-most non-zero value (3, green) to the right, filling cells with its value until one cell before the midpoint.
4.  **Expand** the right-most non-zero value (7, orange) to the left, filling cell with its value up to and potentially including the calculated midpoint.
5.  **Determine** the midpoint. If the number of columns is odd, then there is a true single midpoint. If it is even, use floor((left+right)/2)
6.  **Insert** the value 5 (gray) into the cell at the midpoint position determined in the previous step.
"""

import numpy as np

def find_non_zero_indices(row):
    """Finds the indices of non-zero elements in a row."""
    indices = np.nonzero(row)[0]
    return indices

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find the row with non-zero values.
    non_zero_row_index = -1
    for i, row in enumerate(input_grid):
        if np.any(row != 0):
            non_zero_row_index = i
            break
    
    if non_zero_row_index == -1:
        return output_grid # Nothing to transform

    non_zero_row = input_grid[non_zero_row_index]
    
    # Find indices of the non-zero values.
    non_zero_indices = find_non_zero_indices(non_zero_row)
    if len(non_zero_indices) < 2:
        return output_grid # Need at least 2
    left_index = non_zero_indices[0]
    right_index = non_zero_indices[-1]
    left_color = non_zero_row[left_index]
    right_color = non_zero_row[right_index]

    # Calculate the midpoint.
    midpoint = (left_index + right_index) // 2

    # Expand the left color.
    for i in range(left_index, midpoint):
        output_grid[non_zero_row_index, i] = left_color

    # Expand the right color.
    for i in range(midpoint + 1, right_index + 1):
        output_grid[non_zero_row_index, i] = right_color
    
    # Insert 5 at the midpoint
    output_grid[non_zero_row_index, midpoint] = 5


    return output_grid