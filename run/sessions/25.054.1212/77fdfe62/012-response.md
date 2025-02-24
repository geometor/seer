# 77fdfe62 • 012 • refine_coder

---
```python
"""
The output grid's size is determined as follows: If the input grid has an even number of rows AND even number of columns, AND both the row and column count are >= 8, then the output is 4x4. In this case (4x4 output), create a 4x4 grid. Fill the top-left 2x2 section with the color of the top-left pixel of the input. Fill the top-right 2x2 section with the color of the top-right pixel. Fill the bottom-left 2x2 section with the color of the bottom-left pixel. Fill the bottom-right 2x2 section with the color of the bottom-right pixel. If the size condition is not met but the input has even numbered rows and columns, then the output is 2x2. If the output grid is 2x2, then the output grid consists of the four corner pixels of the input grid. The top-left pixel of the output is the top-left pixel of the input. The top-right is the top-right, etc.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rules derived from the examples.
    """
    rows, cols = input_grid.shape

    # Determine output size based on input dimensions.
    if rows % 2 == 0 and cols % 2 == 0 and rows >= 8 and cols >= 8:
        output_grid = np.zeros((4, 4), dtype=int)
        top_left = input_grid[0, 0]
        top_right = input_grid[0, cols - 1]
        bottom_left = input_grid[rows - 1, 0]
        bottom_right = input_grid[rows - 1, cols - 1]

        # Fill quadrants.
        output_grid[:2, :2] = top_left
        output_grid[:2, 2:] = top_right
        output_grid[2:, :2] = bottom_left
        output_grid[2:, 2:] = bottom_right
    elif rows % 2 == 0 and cols % 2 == 0:
        output_grid = np.zeros((2, 2), dtype=int)
        output_grid[0, 0] = input_grid[0, 0]
        output_grid[0, 1] = input_grid[0, cols - 1]
        output_grid[1, 0] = input_grid[rows - 1, 0]
        output_grid[1, 1] = input_grid[rows - 1, cols - 1]

    else:  # Should not happen, based on the current examples and problem description
        output_grid = np.zeros((2,2), dtype=int) # return a 2x2 to prevent failures
        output_grid[0, 0] = input_grid[0, 0]
        output_grid[0, 1] = input_grid[0, cols - 1]
        output_grid[1, 0] = input_grid[rows - 1, 0]
        output_grid[1, 1] = input_grid[rows - 1, cols - 1]


    return output_grid
```

