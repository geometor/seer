"""
1.  **Identify the blue stripe:** Locate the contiguous vertical stripe of blue (1) pixels in the input grid.
2.  **Extract Stripe Index:** Note the x-coordinate (column index) of this blue stripe. In this case, it's column 3 (starting from 0).
3.  **Extract column:** extract the values from the input grid at that column
4.  **Replace Values:** In the values, replace all blue (1) values with azure (8).
5.  **Construct Output Grid:** Create a new grid. The values extracted will be the center column. Add a column of white(0) on each side. The output grid's height will be equal to input grids, and the width is defined from the number of padding columns plus the extracted one.
"""

import numpy as np

def find_vertical_stripe(grid, color):
    """Finds the index of a vertical stripe of the specified color."""
    height, width = grid.shape
    for x in range(width):
        is_stripe = True
        for y in range(height):
            if grid[y, x] != color:
                is_stripe = False
                break
        if is_stripe:
            return x
    return -1

def transform(input_grid):
    # 1. Identify the blue stripe and its index.
    blue_stripe_index = find_vertical_stripe(input_grid, 1)

    #initialize the height and padding
    height = input_grid.shape[0]
    preceding_columns = 1
    following_columns = 1
    
    # 2. If no blue stripe is found, return an empty grid (or handle appropriately).
    if blue_stripe_index == -1:
        return np.zeros((input_grid.shape[0], 3), dtype=int) #should normally return 0 array

    # 3. Extract column
    extracted_column = input_grid[:, blue_stripe_index]
    
    # 4. Replace Values
    replaced_column = np.where(extracted_column == 1, 8, extracted_column)
   
    # 5. Construct Output Grid
    output_grid = np.zeros((height, preceding_columns + 1 + following_columns), dtype=int)
    output_grid[:, preceding_columns] = replaced_column

    return output_grid