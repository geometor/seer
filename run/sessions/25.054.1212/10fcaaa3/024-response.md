# 10fcaaa3 • 024 • refine_coder

---
```python
"""
Doubles the dimensions of the input grid. Copies non-zero pixels from the input 
grid to the output grid at upscaled locations, with a second copy placed two 
positions to the right if the original pixel isn't in the last column. Fills 
empty (zero-valued) cells in the output grid with azure (8) if their row and 
column indices are both even or both odd.
"""

import numpy as np

def transform(input_grid):
    # Double the grid size.
    input_height, input_width = input_grid.shape
    output_height, output_width = input_height * 2, input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through non-zero pixels in the input grid.
    for r in range(input_height):
        for c in range(input_width):
            color = input_grid[r, c]
            if color != 0:
                # Upscale and copy the color.
                out_row = r * 2 + 1
                out_col = c * 2 + 1
                output_grid[out_row, out_col] = color

                # Copy to the right if not in the last column.
                if c < input_width - 1:
                    output_grid[out_row, out_col + 2] = color

    # Fill with azure based on row and column parity.
    for r in range(output_height):
        for c in range(output_width):
            if output_grid[r, c] == 0:
                if (r % 2 == 0 and c % 2 == 0) or (r % 2 != 0 and c % 2 != 0) :
                    output_grid[r, c] = 8

    return output_grid
```
