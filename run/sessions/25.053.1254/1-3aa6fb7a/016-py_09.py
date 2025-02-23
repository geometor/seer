"""
1.  **Locate Azure:** Identify all azure (value 8) pixels within the input grid.

2.  **Check for 2x2 Formation:** For each azure pixel:
    *   Iterate through each diagonal location.
    *   Check if placing a blue pixel (value 1) in the diagonally opposite position *would* complete a 2x2 square.
    *   This check requires:
        *   The diagonally opposite cell, and the cells between it and the original must be within the grid bounds.
        *   The two intermediate cells must be *either* azure (8) or blue (1).
        *   The diagonally opposite cell must be white(0) or azure(8) or blue(1)
    * If a valid 2x2 square can be formed, place a blue pixel (1) at the diagonal location. Proceed to the next azure pixel - only one blue pixel created for each.

3. **Output:** After checking all azure pixels, the modified grid is the output.
"""

import numpy as np

def find_azure_pixels(grid):
    # Find coordinates of all azure pixels
    return np.argwhere(grid == 8)

def is_valid(grid, row, col):
    rows, cols = grid.shape
    return 0 <= row < rows and 0<= col < cols

def can_form_2x2_square(grid, r_azure, c_azure, r_check, c_check):
     # check opposite side from the azure for out of bounds

    if not is_valid(grid, r_check, c_check):
        return False

    row_diff = r_azure - r_check
    col_diff = c_azure - c_check

    # must be diagonal
    if abs(row_diff) != 1 or abs(col_diff) != 1: return False

    r1 = r_azure - row_diff
    c1 = c_azure
    if not is_valid(grid, r1, c1) or (grid[r1,c1] != 1 and grid[r1, c1] != 8): return False
        
    r2 = r_azure
    c2 = c_azure - col_diff
    if not is_valid(grid, r2, c2) or (grid[r2, c2] != 1 and grid[r2,c2] != 8): return False

    # check opposite is not blocking
    if grid[r_check, c_check] != 0 and grid[r_check,c_check] != 1 and grid[r_check, c_check] != 8 : return False
    
    return True

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    azure_pixels = find_azure_pixels(input_grid)

    # Iterate through azure pixels and apply transformation rule
    for r_azure, c_azure in azure_pixels:
        for r_check in [r_azure -1, r_azure + 1]:
            for c_check in [c_azure -1, c_azure + 1]:
                if can_form_2x2_square(input_grid, r_azure, c_azure, r_check, c_check):
                    output_grid[r_check, c_check] = 1
                    break  # Move to the next azure pixel after placing one blue pixel
            else:
                continue
            break

    return output_grid