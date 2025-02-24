# c59eb873 • 002 • example_1 • investigate_coder

---
```python
"""
The input grid is expanded by a factor of 2 in both dimensions. Each original pixel becomes a 2x2 square of the same color in the output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 2, input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels 
    for i in range(input_height):
        for j in range(input_width):
            color = input_grid[i, j]
            output_grid[2*i:2*i+2, 2*j:2*j+2] = color

    return output_grid
```

