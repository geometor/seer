# 1b60fb0c • 002 • example_1 - CODE

---
```python
"""
1. Copy the blue object from the input.
2. Find the left most 3 blue pixels on row 5 and change them to red.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all cells with the specified color.
    coords = np.argwhere(grid == color)
    return coords

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    
    # Copy the blue object (color 1)
    # No operation needed as the initial copy already includes blue pixels.
    
    # Find the 5th row (index 4).
    row_index = 4
    
    #Find the leftmost 3 blue pixels
    blue_pixels_in_row = np.where(output_grid[row_index,:]==1)[0]
    
    if len(blue_pixels_in_row) >=3:
        for i in range(3):
            output_grid[row_index,blue_pixels_in_row[i]] = 2
    

    return output_grid
```

