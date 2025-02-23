# AboveBelow5 • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Key Column:** Locate the central vertical column (column index 5, since the grid is 9x9).

2.  **Conditional Color Swap:**
    *   Iterate through each pixel in the input grid.
    *   If a pixel in the input is blue (1) AND it is *not* in the central column, change it to green (3) in the output grid.
    *   If a pixel in the input is green (3) AND it *is* in the central column, change to blue (1) in the output grid.

3.  **Preserve Other Pixels:** All other pixels (white/0) retain their original color and position in the output grid.
"""

import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)  # Initialize output grid with the original values
    rows, cols = input_grid.shape
    center_col = cols // 2 # Integer division to find center column.

    # Iterate over each cell of input and apply rule
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 1 and c != center_col:  # Blue and not in center column.
                output_grid[r, c] = 3
            elif input_grid[r, c] == 3 and c == center_col:  # Green and in center column.
                output_grid[r, c] = 1
    return output_grid
```
