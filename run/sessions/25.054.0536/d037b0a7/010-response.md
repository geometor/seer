# d037b0a7 • 010 • refine_coder

---
```python
"""
1. Find Red: Identify all pixels that are the color red (value 2) in the input grid.
2. Propagate Downward: For each column, identify the top pixel of that column.
Then, for each column containing a red pixel,
all pixels from that red pixel to the bottom of the grid in
that column become the color/value of the top pixel of that column.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of red pixels.
    If a red pixel is found, all pixels below it in that
    *column* become the color of the top pixel in that column.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find Red Pixels and Top Pixels
    red_pixels = []
    top_pixels = []
    for c in range(cols):
        top_pixels.append(input_grid[0,c]) #store the colors/value of the top row
        for r in range(rows):
            if input_grid[r, c] == 2:
                red_pixels.append((r, c))


    # 2. Propagate Downward within Columns
    for r, c in red_pixels:
        top_color = top_pixels[c]
        for next_row in range(r, rows):
            output_grid[next_row, c] = top_color  # Fill with top color

    return output_grid
```

