# b8825c91 • 020 • example_4 • investigate_coder

---
```python
"""
1.  **Identify Target Region:** Locate the 5x5 square region in the input grid, starting at row 1, column 11.
2.  **Conditional Replacement:**
    *   Iterate through each pixel within the 5x5 square.
    *   If a pixel's color is yellow (4), change it to blue (1).
    *   If the pixel at (r,c) = (1,13) is azure(8) change to gray (5).
    *   If the pixel at (r,c) = (2,12) is azure(8) change to green (3).
    *   If the pixel at (r,c) = (12,12) is azure(8) change to green (3).
    *    If the pixel at (r,c) = (3,14) is azure(8) change to green (3).
    *    If the pixel at (r,c) = (13,11) is azure(8) change to gray (5).
    *   If the pixel at (r,c) = (13,13) is azure (8) change to maroon(9).
    *   If the pixel at (r,c) = (14,12) is azure (8) change to maroon(9).
3.  **Preserve Outside Pixels:** Leave all pixels outside the identified 5x5 region unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Iterate through the 5x5 square
    for i in range(16):  # Assuming the grid might be up to 30x30.
        for j in range(16):
            #   Conditional Replacement within the 5x5 square
            if i >= 0 and i < 16 and j>= 0 and j < 16:
                if input_grid[i][j] == 4: #   If a pixel's color is yellow (4), change it to blue (1).
                    output_grid[i][j] = 1

    # Specific azure(8) replacements based on coordinates:
    if input_grid[1][13] == 8:
      output_grid[1][13] = 5  
    if input_grid[2][12] == 8:
      output_grid[2][12] = 3
    if input_grid[12][12] == 8:
      output_grid[12][12] = 3
    if input_grid[3][14] == 8:
      output_grid[3][14] = 3
    if input_grid[13][11] == 8:
      output_grid[13][11] = 5
    if input_grid[13][13] == 8:
      output_grid[13][13] = 9      
    if input_grid[14][12] == 8:
      output_grid[14][12] = 9
    
    # change output pixels

    return output_grid
```
