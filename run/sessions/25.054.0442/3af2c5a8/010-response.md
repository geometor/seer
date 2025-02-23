# 3af2c5a8 • 010 • refine_coder

---
```python
"""
The output grid's dimensions are double the input grid's dimensions. The output grid is constructed by filling its four quadrants with the original input grid, its horizontal mirror, its vertical mirror, and a version mirrored both horizontally and vertically.
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    input_height, input_width = input_grid.shape

    # Calculate output grid dimensions
    output_height = 2 * input_height
    output_width = 2 * input_width

    # Initialize output grid with zeros
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Top-left quadrant: Direct copy
    output_grid[:input_height, :input_width] = input_grid

    # Top-right quadrant: Horizontal reflection
    output_grid[:input_height, input_width:] = np.fliplr(input_grid)

    # Bottom-left quadrant: Vertical reflection
    output_grid[input_height:, :input_width] = np.flipud(input_grid)

    # Bottom-right quadrant: Horizontal and vertical reflection
    output_grid[input_height:, input_width:] = np.fliplr(np.flipud(input_grid))
    
    return output_grid
```
