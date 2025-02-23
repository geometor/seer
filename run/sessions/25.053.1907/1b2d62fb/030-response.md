# 1b2d62fb • 030 • refine_coder

---
```python
"""
1.  **Locate the Blue Stripe:** Find the vertical stripe of blue (1) pixels in the input grid. A vertical stripe is defined as a contiguous set of pixels of the same color in a single column, where the set has a length greater than one.
2.  **Define Subgrid Region:** Define a 5x3 rectangular region (5 rows, 3 columns) immediately to the right of the blue stripe. The top row of this subgrid is aligned with the top row of the blue stripe.
3.  **Extract Subgrid:** Extract the pixel values from the input grid within the defined 5x3 region. If the region extends beyond the input grid, the remaining values of the subgrid are filled with zeros.
4.  **Transform Subgrid Colors:** Within the extracted 5x3 subgrid, apply the following color transformation:
    *   If a pixel is white (0), change it to azure (8).
    *   Otherwise, change it to black (0).
5.  **Output:** Create an output grid that is 5x3. Place the transformed pixels from the subgrid into this output grid.
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

    # Determine output grid dimensions (5x3)
    output_rows = 5
    output_cols = 3

    # initialize output_grid with zeros
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Define the region of interest (immediately to the right of the stripe)
    start_col = stripe_col + 1
    start_row = stripe_row # Use the starting row of the stripe
    
    #fill output grid
    for r in range(output_rows):
        for c in range(output_cols):
            #check for out of input bounds
            if start_col + c < np.array(input_grid).shape[1] and start_row + r < np.array(input_grid).shape[0] :
                if input_grid[start_row + r][start_col + c] == 0:
                    output_grid[r][c] = 8
                else:
                    output_grid[r][c] = 0
            else:
                #fill with zeros
                output_grid[r][c] = 0

    return output_grid.tolist()
```
