# 2-0ca9ddb6 • 012 • refine_code - CODE

---
```python
"""
1.  **Identify Target Cells:** Locate all cells with the colors red (2) and blue (1).

2.  **Create Surrounding Plus Shapes:**
    *   For each red cell (color 2), create a "plus" shape using yellow (color 4) in the four cells directly adjacent (up, down, left, right) to the red cell.  Do *not* change the color of the red cell itself.
    *   For each blue cell (color 1), create a "plus" shape using orange (color 7) in the four cells directly adjacent (up, down, left, right) to the blue cell. Do *not* change the color of the blue cell itself.

3.  **Preserve Other Cells:** All other cells in the grid (those that are not red or blue, and are not part of a plus shape drawn around a red or blue cell) retain their original color.
"""

import numpy as np

def create_plus_shape_around(grid, center, color):
    """Creates a plus shape around a center cell with a specified color,
    without changing the center cell itself."""
    rows, cols = grid.shape
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in offsets:
        r, c = center[0] + dr, center[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            grid[r, c] = color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:  # Red cell
                # Create yellow plus shape *around* the red cell
                output_grid = create_plus_shape_around(output_grid, (r, c), 4)
            elif input_grid[r, c] == 1:  # Blue cell
                # Create orange plus shape *around* the blue cell
                output_grid = create_plus_shape_around(output_grid, (r, c), 7)

    return output_grid
```

