# 99fa7670 • 022 • refine_coder

---
```python
"""
1.  **Identify Non-White Pixels:** Iterate through each pixel in the input grid. If a pixel is not white (color code 0), proceed to the next step.
2.  **Expand to the Right:** For each non-white pixel, change the color of the pixels to its right, in the same row, to be the same color, until the end of the row is reached or another non-white pixel is encountered.
3.  **Drop Down:** The last pixel filled during step two should then be used as the color for all cells below it, within its column, until the last row is reached.
4.  **Output:** The resulting grid after applying steps 1-3 is the final output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # iterate through each pixel in the grid
    for r in range(rows):
        for c in range(cols):
            # Identify Non-White Pixels
            if output_grid[r, c] != 0:
                # Expand to the Right
                current_color = output_grid[r, c]
                c2_end = cols # init end column
                for c2 in range(c + 1, cols):
                    if output_grid[r, c2] == 0:
                        output_grid[r, c2] = current_color
                    else:
                        c2_end = c2
                        break  # Stop expansion if a non-white pixel is encountered
                # Drop Down
                if c2_end == cols:
                    c2_end -= 1
                
                for r2 in range(r + 1, rows):
                  output_grid[r2,c2_end] = current_color

    return output_grid
```
