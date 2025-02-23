# 6-0520fde7 • 002 • example_1 - CODE

---
```python
"""
1. **Identify Center:** Locate the vertical stripe of gray (value 5) pixels in the input grid.
2. **Define Region:** Define a 3x3 region centered on the identified gray stripe.
3. **Color Change:** The output grid will mirror the region of the input with white and blue becoming white, and gray becoming red.
"""

import numpy as np

def find_gray_stripe_center(input_grid):
    # Find the column index where the gray (value 5) pixels are located.
    for j in range(input_grid.shape[1]):
        if np.all(input_grid[:, j] == 5):
            return j
    return -1  # Return -1 if no gray stripe is found


def transform(input_grid):
    """
    Extracts a 3x3 region from the input grid centered on a vertical gray stripe and recolors it.
    """
    input_grid = np.array(input_grid)
    center_col = find_gray_stripe_center(input_grid)
    
    if center_col == -1:
        return None # No gray stripe found

    # Define the 3x3 region
    start_row = 0
    end_row = input_grid.shape[0]
    start_col = center_col - 1
    end_col = center_col + 2

    # Extract the region
    region = input_grid[start_row:end_row, start_col:end_col]
    
    # Create output grid
    output_grid = np.zeros_like(region)
    
    # recolor output based on input region
    for i in range(region.shape[0]):
        for j in range(region.shape[1]):
            if region[i,j] == 0 or region[i,j] == 1:
                output_grid[i,j] = 0
            if region[i,j] == 5:
                output_grid[i,j] = 2

    return output_grid.tolist()
```
