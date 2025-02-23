# 5582e5ca • 002 • example_1 • investigate_coder

---
```python
"""
The task is to transform an input grid of colored pixels into an output grid of the same dimensions, where all pixels in the output grid have the same color, and the chosen color is present in the input grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find a color.  Here we use the color from the input grid's top-left corner.
    fill_color = input_grid[0, 0]

    # change output pixels
    for i in range(rows):
        for j in range(cols):
            output_grid[i, j] = fill_color

    return output_grid
```

