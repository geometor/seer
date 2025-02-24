# 794b24be • 014 • example_3 • investigate_coder

---
```python
"""
Iterate through each pixel of the input grid. If the pixel is blue (value 1), change it to red (value 2) in the output grid. Else, if the pixel is white (value 0), keep it white (value 0) in the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Get the dimensions of the grid
    rows, cols = output_grid.shape

    # Iterate through each pixel of the grid
    for i in range(rows):
        for j in range(cols):
            # change output pixels based on input pixel value
            if input_grid[i, j] == 1:  # If blue
                output_grid[i, j] = 2  # Change to red
            #elif input_grid[i,j] == 0: # white pixels remain unchanged
            #   output_grid[i,j] = 0

    return output_grid
```

