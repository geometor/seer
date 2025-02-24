# 99b1bc43 • 018 • refine_coder

---
```python
"""
1.  **Divide:** Divide the input grid into non-overlapping 2x2 blocks.  Ignore any leftover rows or columns if the dimensions are odd.
2.  **Reduce:** Each 2x2 block in the input grid corresponds to *one* pixel in the output grid. The row and column of the output pixel are half the row and column of the 2x2 block's top-left corner (using integer division).
3.  **Conditional Color Mapping:**
    *   If the 2x2 input block contains *any* blue (1), red (2), or yellow (4) pixel, the corresponding output pixel is green (3).
    *   Otherwise, the output pixel is white (0).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_array = np.array(input_grid)
    input_height, input_width = input_array.shape
    output_height = input_height // 2
    output_width = input_width // 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through 2x2 blocks in the input grid
    for i in range(output_height):
        for j in range(output_width):
            # Extract the 2x2 block
            block = input_array[i*2:(i+1)*2, j*2:(j+1)*2]

            # change output pixels
            # Conditional Color Mapping
            if 1 in block or 2 in block or 4 in block:
                output_grid[i, j] = 3  # Output green
            else:
                output_grid[i, j] = 0  # Output white

    return output_grid.tolist()
```
