# 2dee498d • 012 • refine_coder

---
```python
"""
Extracts a subgrid from the top-left corner of the input grid. The dimensions of
the subgrid are determined by the expected output grid's dimensions.
"""

import numpy as np

def transform(input_grid, output_height, output_width):
    """
    Extracts a subgrid from the top-left corner.  The output grid's dimensions
    are determined by the provided output_height and output_width.

    Args:
        input_grid (list of lists): The input grid.
        output_height (int): Expected height of the output grid.
        output_width (int): Expected width of the output grid.

    Returns:
        list of lists: The extracted subgrid.
    """
    # Determine Output Dimensions (using provided values):


    # Extract Subgrid:
    output_grid = []
    for i in range(output_height):
        row = []
        for j in range(output_width):
            row.append(input_grid[i][j])
        output_grid.append(row)

    return output_grid
```

