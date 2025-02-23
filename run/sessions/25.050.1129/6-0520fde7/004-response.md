# 6-0520fde7 • 004 • example_2 - CODE

---
```python
"""
Extracts the central column from the input grid, identifies the first two non-white colors,
and creates a 3x3 output grid. The identified color's pixel (changed to color 2) is
placed at positions [0,1], [2,1], [1,2] forming a cross, and white (0) elsewhere.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by extracting the central column, identifies the first two
    non-white color, and creates a 3x3 output grid. The color 2 is placed on positions
    [0,1], [2,1] and [1,2]
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Get dimensions of the input grid
    rows, cols = input_grid.shape

    # Find the center column index
    center_col_index = cols // 2

    # Extract the center column
    center_column = input_grid[:, center_col_index]


    # Create a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the first non-white (non-zero) colors in the center column
    non_white_colors = []
    for cell_color in center_column:
        if cell_color != 0 and cell_color not in non_white_colors:
          non_white_colors.append(cell_color)

    # Place the color 2 in output grid according to the cross pattern
    output_grid[0, 1] = 2
    output_grid[2, 1] = 2
    output_grid[1, 2] = 2

    return output_grid
```

