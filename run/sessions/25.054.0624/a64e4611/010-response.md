# a64e4611 • 010 • refine_coder

---
```python
"""
1.  **Identify Target Color:** Determine the color of the rightmost vertical stripe that is at least 3 pixels high.
2.  **Find Rightmost Column:** Find the index of the rightmost column of this target color stripe.
3.  **Define Rectangular Region:** Define a rectangular region that starts one column to the right of the identified column and extends to the end of the grid, spanning all rows.
4.  **Preserve Outside Pixels:** All pixels *outside* of this defined rectangular region in the input grid should be copied directly to the output grid.
5.  **Modify Inside Pixels:** All pixels *inside* the identified rectangular region are changed to green (value 3) in the output grid.
"""

import numpy as np

def find_rightmost_stripe_column(grid, min_height):
    """
    Finds the rightmost column index of a vertical stripe of a specific color.

    Args:
    grid: The input grid (numpy array).
    min_height: minimum height of the identified stripe.

    Returns:
    The column index of the rightmost stripe, or -1 if no stripe of min_height is found.
    """
    
    # reverse iterate through columns
    for col_index in range(grid.shape[1] - 1, -1, -1):
        # iterate through all colors to find color of largest contiguous pixels in this column
        color_counts = np.bincount(grid[:, col_index])
        
        # if there is color with count more that min_height
        if np.max(color_counts) >= min_height:
          # exit, we found the color and position of the stripe
          return col_index

    return -1 # no valid stripe

def transform(input_grid):
    """
    Transforms the input grid by changing a rectangular region to the right of a
    colored stripe to green (3).
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of the input_grid
    
    # Define the minimum height of a vertical stripe
    min_height = 3

    # Find the rightmost stripe column of the target color
    stripe_column = find_rightmost_stripe_column(input_grid, min_height)

    if stripe_column != -1:  # Ensure a stripe was found
      start_column = stripe_column + 1

      # Define the rectangular region's boundaries
      
      end_column = output_grid.shape[1] - 1

      # Iterate through each row and modify the specified columns
      for row_index in range(output_grid.shape[0]):
          for col_index in range(start_column, end_column + 1):  # Inclusive range
              output_grid[row_index, col_index] = 3  # Set pixel to green (3)
    
    return output_grid
```
