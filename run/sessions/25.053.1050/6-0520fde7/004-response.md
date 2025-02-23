# 6-0520fde7 • 004 • refine_coder

---
```python
"""
1.  **Initialize Output:** Create a 3x3 output grid filled with white pixels (color 0).

2.  Locate zero value pixels in input.

3.  **Iterate through zero value pixels**:
  *   if a zero value pixel in the input aligns with the output origin (0,0) and a color of 2 in the output, set the corresponding output to 2.
  *   if a zero value pixel in the input aligns with the output center (1,1) and a color of 2 in the output, set the corresponding output to 2.
  *   if a zero value pixel in the input aligns with the bottom right of the output (2,2) and a color of 2 in the output, set the corresponding output to 2.

4. **Return the output grid**
"""

import numpy as np

def get_zero_pixel_positions(grid):
    return np.argwhere(grid == 0)

def transform(input_grid):
    # Initialize a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Get positions of zero-valued pixels in the input grid
    zero_positions = get_zero_pixel_positions(input_grid)

    # Get the center column for alignment checks.  We use the center
    # column because the examples show the output 3x3 centered there.
    center_col = input_grid.shape[1] // 2

    # Iterate and check alignment
    for row, col in zero_positions:
        # Calculate relative position to the center of the input
        row_rel = row 
        col_rel = col - (center_col-1)  # Adjust column relative to the output grid center
        # check alignment and update corresponding output pixel, origin
        if row_rel == 0 and col_rel == 0 :
          if (row_rel, col_rel) == (0,0):
             output_grid[0,0] = 2
          elif (row_rel, col_rel) == (0,1):
             output_grid[0,1] = 2
          elif (row_rel, col_rel) == (0,2):
             output_grid[0,2] = 2
          
        # check alignment and update corresponding output pixel, center
        elif row_rel == 1 and col_rel == 1:
            output_grid[1, 1] = 2
        
        elif row_rel == 1 and col_rel == 0:
            output_grid[1, 0] = 2

        #bottom right
        elif row_rel == 2 and col_rel == 2 :
            output_grid[2, 2] = 2

        elif row_rel == 2 and col_rel == 1 :
            output_grid[2, 1] = 2
    return output_grid
```
