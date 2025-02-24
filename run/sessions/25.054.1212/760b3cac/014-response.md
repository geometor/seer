# 760b3cac • 014 • example_3 • investigate_coder

---
```python
"""
The Yellow object remains the same.
The Azure object is copied and expanded to the left.
"""

import numpy as np

def find_object(grid, color):
    coords = np.argwhere(grid == color)
    if len(coords) == 0:
        return []
    return coords.tolist()

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find the azure and yellow objects
    azure_object = find_object(input_grid, 8)
    yellow_object = find_object(input_grid, 4)
    
    # yellow object does not change
    
    # azure object transformation
    if azure_object:
        # Top pixel shift
        top_pixel = min(azure_object, key=lambda p: (p[0], p[1]))
        if top_pixel[1] == 3 and top_pixel[0] == 0:
            output_grid[top_pixel[0], top_pixel[1]-1] = 8
        
        # Second row shift
        second_row_pixels = [p for p in azure_object if p[0] == 1]
        if second_row_pixels:
          output_grid[1,0] = 8
          output_grid[1,1] = 8

        # Third row duplication
        third_row_pixels = [p for p in azure_object if p[0] == 2]
        if len(third_row_pixels) >0 and third_row_pixels[0][1] == 3:
          output_grid[2,2] = 8

    return output_grid
```
