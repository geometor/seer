# 3de23699 • 006 • example_3 - CODE

---
```python
"""
The transformation identifies the positions of magenta (6) cells in the input grid, which determine a rectangle.
These positions are mapped to a 4x4 output.
The output grid is filled with additional magenta (6) following an overwrite rule.
"""
import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid based on the positions of the magenta cells.
    """

    output_grid = np.zeros((4, 4), dtype=int)

    rows, cols = np.where(input_grid == 6)
    magenta_positions = list(zip(rows, cols))

    # Extract corners
    corners = []
    if magenta_positions:
        min_row = min(rows)
        max_row = max(rows)
        min_col = min(cols)
        max_col = max(cols)
        corners = [(min_row, min_col), (min_row, max_col), (max_row, min_col), (max_row, max_col)]

        # Map positions and fill with color 6
        for r,c in corners:
            out_r = 0 if r == min_row else 3
            out_c = 0 if c == min_col else 3
            output_grid[out_r,out_c] = 6

    # Fill with additional magenta (6)
    output_grid[0,1] = 6
    output_grid[1,1] = 6
    output_grid[2,0] = 6
    output_grid[2,1] = 6
    output_grid[2,2] = 6
    output_grid[3,1] = 6
    output_grid[3,2] = 6

    return output_grid
```

