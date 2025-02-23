# 1b60fb0c • 004 • example_2 - CODE

---
```python
"""
1. Copy the blue object from the input.
2. Find the rows in the input which contain the blue object.
   Change up to 3 leftmost blue pixels in each of these rows to red.
   If a row has less than or equal to three blue pixels and at least one blue pixel,
   all of those get changed to color red.
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
    
    # Find the rows contain blue pixels.
    blue_rows = []
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r,c] == 1:
                blue_rows.append(r)
                break;    
    #print(blue_rows)
    
    
    for row_index in blue_rows:
        #Find the leftmost 3 blue pixels, change it to red
        blue_pixels_in_row = np.where(output_grid[row_index,:]==1)[0]

        if 0 < len(blue_pixels_in_row) <= 3:
            for i in range(len(blue_pixels_in_row)):
                output_grid[row_index,blue_pixels_in_row[i]] = 2
        elif len(blue_pixels_in_row) > 3:
            for i in range(3):
                output_grid[row_index,blue_pixels_in_row[i]] = 2
        

    return output_grid
```

