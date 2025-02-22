# 2-0ca9ddb6 • 004 • refine_code - CODE

---
```python
"""
1.  **Identify Unique Color Cells:** Find all cells that are the sole representative of their color within the input grid.

2.  **Create Plus Shapes Conditionally:** For each identified unique-color cell:
    *   If the unique color is red (2), create a "plus" shape of yellow (4) cells around it.
    *   If the unique color is blue (1), create a "plus" shape of orange (7) cells around it.
    *   If it is any other color, do nothing.

3.  **Plus Shape Definition:** The "plus" shape is formed by placing the new color (yellow or orange) in the four immediate adjacent cells (up, down, left, and right) *one cell away* from the unique-color cell. The unique color cell itself remains unchanged.

4. **Leave other cells unchanged**
"""

import numpy as np

def find_unique_color_cells(grid):
    """Finds cells that are the only instance of their color."""
    color_counts = np.bincount(grid.flatten(), minlength=10)
    unique_colors = np.where(color_counts == 1)[0]
    unique_cells = []
    for color in unique_colors:
        coords = np.where(grid == color)
        unique_cells.append((color, (coords[0][0], coords[1][0])))
    return unique_cells

def create_plus_shape(grid, center, color):
    """Creates a plus shape around a center cell, skipping one cell."""
    rows, cols = grid.shape
    offsets = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Offsets for plus shape, skipping one cell

    for offset in offsets:
        new_row = center[0] + offset[0]
        new_col = center[1] + offset[1]

        if 0 <= new_row < rows and 0 <= new_col < cols:
            grid[new_row, new_col] = color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    output_grid = np.copy(input_grid)
    unique_cells = find_unique_color_cells(input_grid)

    for unique_color, center in unique_cells:
        if unique_color == 2:  # Red
            output_grid = create_plus_shape(output_grid, center, 4)  # Yellow plus
        elif unique_color == 1:  # Blue
            output_grid = create_plus_shape(output_grid, center, 7)  # Orange plus
        #  Do nothing for other unique colors

    return output_grid
```

