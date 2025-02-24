# 94f9d214 • 012 • refine_coder

---
```python
"""
1.  **Initialization:** Start with the input grid.
2.  **Row-wise Processing:** Iterate over the rows of input grid from top to bottom.
3.  **Subgrid Division & Color Check:** Divide the input grid rows in pairs. For each pair, consider 2x2 subgrids.
    *   If a 2x2 subgrid contains a green (3) pixel, the corresponding output pixel becomes red (2).
    *   Otherwise, if the 2x2 subgrid contains a blue (1) pixel, the corresponding output pixel becomes red (2).
    *   Otherwise, the output pixel remains white (0).
4.  **Output Construction:** The final output is constructed by keeping only those rows which contains red(2) pixels.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    temp_grid = np.zeros((rows // 2, cols), dtype=int)

    # Iterate through the input grid in 2x2 blocks with step of 2
    for i in range(0, rows - rows % 2, 2):
        for j in range(0, cols - cols % 2, 2):
            subgrid = input_grid[i:i+2, j:j+2]

            # Check for green or blue pixel and set output to red accordingly
            if 3 in subgrid:
                temp_grid[i // 2, j // 2] = 2
            elif 1 in subgrid:
                temp_grid[i // 2, j // 2] = 2

    # construct output by keeping rows which contain any red pixel
    output_rows = []
    for row in temp_grid:
        if 2 in row:
            output_rows.append(row)

    # Convert the output rows to the correct shape and format
    output_grid_full_width = np.array(output_rows)

    # Reduce width
    output_grid = []
    if len(output_grid_full_width) > 0:
        for row_pixels in output_grid_full_width:
            out_row = []
            for c_idx in range(0, len(row_pixels) - len(row_pixels) % 2, 2):
                if row_pixels[c_idx] != 0 or row_pixels[c_idx + 1] != 0:
                  out_row.append(row_pixels[c_idx] if row_pixels[c_idx] != 0 else row_pixels[c_idx+1])
                else:
                    out_row.append(0)
            output_grid.append(out_row)
    else:
        output_grid = np.zeros((rows//2, cols//2), dtype = int).tolist() # If empty, we can still reduce.

    return output_grid
```
