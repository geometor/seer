# ce4f8723 • 004 • refine_coder

---
```python
"""
The task involves downsampling a larger input grid to a 4x4 output grid.
The transformation rule is based on the top-left 4x4 subgrid of the input.
Non-white pixels within this input subgrid are converted to green in the output grid, while white pixels remain white.
"""

import numpy as np

def transform(input_grid):
    # Initialize the 4x4 output grid with zeros (white).
    output_grid = np.zeros((4, 4), dtype=int)

    # Iterate through each cell of the output grid (and, equivalently, the top-left 4x4 subgrid).
    for i in range(4):
        for j in range(4):
            # Get the corresponding pixel value from the input grid's top-left 4x4 subgrid.
            pixel_value = input_grid[i][j]

            # Apply the color transformation:
            # - If the input pixel is white (0), the output pixel is white (0).
            # - Otherwise (if the input pixel is not white), the output pixel is green (3).
            if pixel_value != 0:
                output_grid[i][j] = 3

    return output_grid
```

