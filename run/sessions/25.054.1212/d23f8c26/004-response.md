# d23f8c26 • 004 • refine_coder

---
```python
"""
1. Examine each pixel in the input grid.
2. Identify the colors present in all output grids from the training examples.
3. If the pixel's color is present in all of the output grids, keep its original value in the output grid.
4. If the pixel's color is *not* present in all of the output grids, set its value to 0 (background) in the output grid.
"""

import numpy as np

def get_colors_in_output(examples):
    """
    Collects all unique colors present across all output grids in the examples.
    """
    all_colors = set()
    for example in examples:
        all_colors.update(np.unique(example["output"]))
    return all_colors

def transform(input_grid, examples):
    # Initialize output_grid as a copy of the input, ensures same size and type
    output_grid = np.zeros_like(input_grid)

    # Get the unique colors that exist in *all* of the output grids
    output_colors = get_colors_in_output(examples)

    # Iterate through each cell of the input grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Check if current input color exists in the set of all output colors
            if input_grid[i, j] in output_colors:
                output_grid[i,j] = input_grid[i, j]  # keep color
            else:
                output_grid[i, j] = 0   # set to background

    return output_grid
```
