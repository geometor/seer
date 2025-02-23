# 3-1e0a9b12 • 004 • example_2 - CODE

---
```python
"""
1.  **Identify Moving Pixels:** Focus on pixels in the first and second row (row indices 0 and 1) of the input grid that are not black (value 0).
2.  **Move Pixels:** For each of these pixels, move it to the last row (row index 5) of the output grid, but keep it in the same column.
3.  **Copy Unmoved:** All other pixels from the input grid are copied to the output grid in their original positions.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)  # Initialize output as a copy of input
    height, width = input_grid.shape

    # Iterate through the first two rows
    for row_index in range(2):
        for col_index in range(width):
            if input_grid[row_index, col_index] != 0:
                #check that the target space is available
                if output_grid[height - 1, col_index] == 0:
                    # Move the pixel to the last row, same column
                    output_grid[height - 1, col_index] = input_grid[row_index, col_index]
                    output_grid[row_index, col_index] = 0  # Set the original position to 0


    return output_grid
```

