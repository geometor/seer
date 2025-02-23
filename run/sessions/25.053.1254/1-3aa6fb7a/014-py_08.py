"""
1.  **Identify Azure Pixels:** Find all pixels with the value 8 (azure) in the input grid.

2.  **Check for 2x2 Square Formation:** For each azure pixel, examine the three other pixels that could potentially form a 2x2 square with it. These are the pixels diagonally, above/below, and to the left/right.

3.  **Conditional Blue Pixel Addition:** Add a blue pixel (value 1) *only* if *all* of the following conditions are met:
    *   The potential 2x2 square lies entirely within the grid boundaries.
    *   The three examined pixels are *exclusively* colors 1 (blue) or 8 (azure).
    *   The blue pixel is placed at the diagonally opposite position to the selected azure pixel.

4.  **One Blue per Azure:** Only one blue pixel may be added per azure pixel considered.

5.  **Output:** The modified grid with the added blue pixels (if any) is the output.
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
    azure_pixels = find_azure_pixels(output_grid)

    # Iterate through azure pixels and apply transformation rule
    for r_azure, c_azure in azure_pixels:
        for r_check in [r_azure -1, r_azure + 1]:
            for c_check in [c_azure -1, c_azure + 1]:
                if can_form_2x2_square(output_grid, r_azure, c_azure, r_check, c_check):
                    output_grid[r_check, c_check] = 1
                    break # only create one
            else:
                continue
            break


    return output_grid