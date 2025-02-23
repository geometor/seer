# AboveBelow2 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule is a color-based filter: 
- Retain green (value 3) pixels in the output grid at the same position.
- Change all other pixels (white, azure, or orange) to white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid, filled with 0s (white).
    output_grid = np.zeros_like(input_grid)

    # Iterate through each pixel of the input grid.
    for row_index, row in enumerate(input_grid):
        for col_index, pixel_value in enumerate(row):
            # Check if the pixel is green (value 3).
            if pixel_value == 3:
                # If it's green, retain the value in the output grid.
                output_grid[row_index, col_index] = pixel_value
            # else, leave at initialized value of zero
            
    return output_grid
```
