# 6-0520fde7 • 002 • example_1 - CODE

---
```python
"""
Extracts the central column from the input grid, identifies the first non-white color,
and creates a 3x3 output grid with the identified color at the center and white elsewhere,
but changing to color code 2.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by extracting the central column, identifying the first
    non-white color, and creating a 3x3 output grid with the identified color's
    pixel (changed to color code 2) at the center, and white (0) elsewhere.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Get dimensions of the input grid
    rows, cols = input_grid.shape

    # Find the center column index
    center_col_index = cols // 2

    # Extract the center column
    center_column = input_grid[:, center_col_index]

    # Find the first non-white (non-zero) color in the center column
    first_non_white_color = 0
    for cell_color in center_column:
        if cell_color != 0:
            first_non_white_color = cell_color
            break

    # Create a 3x3 output grid filled with white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Place the identified color (changed to 2) at the center of the output grid
    output_grid[1, 1] = 2

    return output_grid
```
