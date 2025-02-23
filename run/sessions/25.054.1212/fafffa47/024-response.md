# fafffa47 • 024 • refine_coder

---
```python
"""
The program transforms a 6x3 input grid into a 3x3 output grid. The transformation
identifies maroon (9) pixels in the input grid. These maroon pixels are mapped
to red (2) pixels in the output grid based on these rules:

1.  **Height Reduction:** The output grid's height is half that of the input grid.
2.  **Maroon to Red Mapping:**
    *   Iterate through pairs of consecutive rows in the input grid (rows 0 and 1, rows 2 and 3, rows 4 and 5).
    *   Within each pair, a red (2) pixel is placed in the output grid at `output_row = input_row // 2` and `output_col = input_col - input_row % 2` if and only if there is a maroon pixel in the input grid at `input_row`, `input_col`.
3.  **All Other Pixels:**  All other pixels in the output grid that do not correspond to a mapped maroon pixel are set to white (0).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height = len(input_grid)
    input_width = len(input_grid[0])
    output_height = input_height // 2
    output_width = input_width
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels
    for input_row in range(0, input_height, 2):
        for input_col in range(input_width):
            if input_grid[input_row][input_col] == 9:
                output_row = input_row // 2
                output_col = input_col
                output_grid[output_row, output_col] = 2

            if input_row + 1 < input_height and input_grid[input_row + 1][input_col] == 9:
                output_row = (input_row + 1) // 2
                output_col = input_col - (input_row + 1) % 2
                if output_col >= 0:
                    output_grid[output_row][output_col] = 2



    return output_grid
```

