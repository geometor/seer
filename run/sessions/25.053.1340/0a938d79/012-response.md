# 0a938d79 • 012 • refine_coder

---
```python
"""
The transformation identifies the row index where each distinct color first appears in the input grid. Then, it replicates each of these colored rows across the entire output grid. The vertical offset for replication is determined by the initial appearance of colors.
"""

import numpy as np

def find_first_color_rows(input_grid):
    """Finds the row index where each distinct color first appears."""
    input_grid = np.array(input_grid)
    color_rows = []
    colors_found = []
    rows, _ = input_grid.shape
    for r in range(rows):
        for c in range(input_grid.shape[1]):
            color = input_grid[r, c]
            if color != 0 and color not in colors_found:
                color_rows.append((color, r))
                colors_found.append(color)
    return color_rows

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find the row indices where each distinct color first appears.
    color_rows = find_first_color_rows(input_grid)

    # Replicate each colored row across the entire grid.
    for color, initial_row in color_rows:
        for i in range(rows):
            row_index = (i) % rows
            if (row_index - initial_row) % rows == 0 :
                output_grid[row_index, :] = color


    return output_grid.tolist()
```
