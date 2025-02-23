# 2-0ca9ddb6 • 008 • refine_code - CODE

---
```python
"""
1.  **Identify Target Cells:** Find all cells colored blue (1) and red (2) within the input grid. These are the centers of our transformations.

2.  **Create Non-Touching Plus Shapes:**
    *   For each red cell (2): Create a "plus" shape made of yellow cells (4). This plus shape is centered *adjacent to* the red cell, meaning the yellow cells *do not* replace the original red cell. The plus shape's arms extend one cell in each cardinal direction (up, down, left, right) from the central red cell's position.
    *   For each blue cell (1): Create a "plus" shape made of orange cells (7).  This plus shape is also centered *adjacent to* the blue cell. The orange cells do not replace the original blue cell. The arms extend one cell in each cardinal direction.

3.  **Preserve Other Cells:** All other cells in the grid (those not colored blue or red, and not part of a generated plus shape) remain unchanged. This includes colors like 0 (background) and 8.
"""

import numpy as np

def create_plus_shape(grid, center, color):
    """Creates a plus shape around a center cell with a specified color,
    without overwriting the center cell itself."""
    rows, cols = grid.shape
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in offsets:
        r, c = center[0] + dr, center[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            grid[r, c] = color  # Directly set the color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)  # Work on a copy
    rows, cols = input_grid.shape

    # Iterate through all cell positions
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:  # Red cell
                create_plus_shape(output_grid, (r, c), 4) #yellow
            elif input_grid[r, c] == 1:  # Blue cell
                create_plus_shape(output_grid, (r, c), 7) #orange

    return output_grid
```

