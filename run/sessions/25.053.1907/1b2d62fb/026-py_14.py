"""
1.  **Identify the Target:** Locate the contiguous vertical stripe of '1' (blue) pixels in the input grid.
2.  **Define the Region of Interest:** Consider the area immediately to the *right* of the blue stripe.
3. **Sub grid extraction.** extract a sub-grid from the input whose left edge is immediately to the right of the target. the dimensions match the output grid.
4.  **Transformation:** Within this region, change any '0' (white) pixel to '8' (azure). If the sub-grid pixel is not '0', it becomes '0'.
5.  **Output:** The transformed region is presented as the output grid.
"""

import numpy as np

def find_vertical_stripe(grid, color):
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i, j] == color:
                # Check if it's a vertical stripe
                stripe_length = 0
                for k in range(i, rows):
                    if grid[k, j] == color:
                        stripe_length += 1
                    else:
                        break
                if stripe_length > 1: # ensure that object height is more than one pixel
                    return j, stripe_length # return the starting column index, and length of stipe
                
    return None, None

def transform(input_grid):
    # Find the vertical stripe of color '1' (blue)
    stripe_col, stripe_height = find_vertical_stripe(np.array(input_grid), 1)

    if stripe_col is None:
        return None  # No stripe found

    # Determine output grid dimensions (5x3 based on the example)
    output_rows = 5
    output_cols = 3

    # initialize output_grid with zeros
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Define the region of interest (immediately to the right of the stripe)
    start_col = stripe_col + 1
    
    #fill output grid
    for r in range(output_rows):
        for c in range(output_cols):
            #check for out of input bounds
            if start_col + c < np.array(input_grid).shape[1] and r < np.array(input_grid).shape[0] :
                if input_grid[r][start_col + c] == 0:
                    output_grid[r][c] = 8
                else:
                    output_grid[r][c] = 0
            else:
                #fill with zeros
                output_grid[r][c] = 0

    return output_grid.tolist()