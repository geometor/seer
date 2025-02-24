# 99fa7670 • 024 • refine_coder

---
```python
"""
1.  **Identify Non-White Pixels:** Examine each pixel in the input grid. If a pixel is *not* white (color 0), it triggers a fill operation.

2.  **Horizontal Fill (Right):** Starting from the non-white pixel, change the color of the pixels to its *right*, within the *same row*, to the same color. Stop this horizontal fill when either:
    *   The edge of the grid is reached.
    *   Another non-white pixel is encountered.

3.  **Vertical Fill (Down):** Using the *last pixel filled* during the horizontal fill, change the color of the pixels directly *below* it, in the *same column*, to be the same color. Stop the vertical fill when either:
    * The edge of the grid (last row) is reached
    * A non-white cell is encountered.

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
                c2_end = cols  # init end column
                for c2 in range(c + 1, cols):
                    if output_grid[r, c2] == 0:
                        output_grid[r, c2] = current_color
                    else:
                        c2_end = c2
                        break  # Stop expansion if a non-white pixel is encountered
                # Drop Down
                if c2_end == cols:
                    c2_end = c2 -1  # Use last filled
                else:
                    c2_end = c2 -1

                for r2 in range(r + 1, rows):
                    if output_grid[r2, c2_end] == 0:
                        output_grid[r2, c2_end] = current_color
                    else:
                        break

    return output_grid
```
