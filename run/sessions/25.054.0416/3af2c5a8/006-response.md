# 3af2c5a8 • 006 • refine_coder

---
```python
"""
The transformation rule is as follows:

1.  **Examine the input grid:** Determine the dimensions (height and width) and the color of each pixel.
2.  **Create the output grid:** The output grid will have dimensions double that of the input grid (2 * height, 2 * width).
3.  **Iterate through each pixel of the input grid:** For each pixel at coordinates (y, x) in the input grid:
    *   Copy the color of the input pixel to the output grid at the following four positions:
        *   (2y, 2x)
        *   (2y + 1, 2x)
        *   (2y, 2x + 1)
        *   (2y + 1, 2x + 1)
    * This effectively replaces each input pixel with a 2x2 block of the same color in the output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # iterate through each pixel of the input grid
    for y in range(input_height):
        for x in range(input_width):
            # copy the color to the 2x2 block in output
            color = input_grid[y, x]
            output_grid[2*y, 2*x] = color
            output_grid[2*y + 1, 2*x] = color
            output_grid[2*y, 2*x + 1] = color
            output_grid[2*y + 1, 2*x + 1] = color

    return output_grid
```
