"""
1.  **Locate Target:** Find the contiguous vertical stripe of blue (1) pixels in the input grid.
2.  **Define Subgrid:** Define a region of interest to the immediate right of the blue stripe. This region will have fixed dimensions of 5x3 (rows x columns).
3. **Extract Subgrid.** Extract a 5x3 subgrid from the input whose left edge is adjacent to the right of the identified blue stripe. The top of the subgrid will match the row index of the input grid.
4.  **Transform Subgrid:** Within this 5x3 subgrid, apply the following transformation:
    *   If a pixel is white (0), change it to azure (8).
    *   If a pixel is not white (0), change it to black (0).
5. **Output:** Create an output grid that matches the dimensions of the subgrid (5x3) from steps 2 and 3. Copy the transformed subgrid to the output grid.
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
                    return j, i, stripe_length # return the starting column index, row index and length of stipe
                
    return None, None, None

def transform(input_grid):
    # Find the vertical stripe of color '1' (blue)
    stripe_col, stripe_row, stripe_height = find_vertical_stripe(np.array(input_grid), 1)

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
            if start_col + c < np.array(input_grid).shape[1] and stripe_row + r < np.array(input_grid).shape[0] :
                if input_grid[stripe_row + r][start_col + c] == 0:
                    output_grid[r][c] = 8
                else:
                    output_grid[r][c] = 0
            else:
                #fill with zeros
                output_grid[r][c] = 0

    return output_grid.tolist()