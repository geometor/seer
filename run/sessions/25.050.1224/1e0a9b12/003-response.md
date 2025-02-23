# 1e0a9b12 • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**Observations:**

Input Grid:

-   Dimensions: 6x6
-   Colors: 0 (white), 4 (yellow), 7 (orange), 8 (azure), 9 (maroon)
-   Objects:
    -   Three yellow cells (4) forming a vertical line at column 0, rows 3, 4, and 5.
    -   Two orange cells (7) at (4, 2) and (5, 2).
    -   Two azure cells (8) at (1,3) and (4,3)
    -    One maroon cell at (0,5)

Output Grid:

-   Dimensions: 6x6
-    Colors: 0 (white), 4 (yellow), 7 (orange), 8 (azure), 9 (maroon)
-   Objects:
        -   Three yellow cells (4) forming a vertical line at column 0, rows 3, 4, and 5.
    -   Two orange cells (7) at (4, 2) and (5, 2).
    -    Two azure cells (8) at (5,3)
    -    One maroon cell at (5,5)

**Transformation Rule (Natural Language Program):**

1.  **Identify Objects:** Find all non-white cells in the input grid.

2.  **Move Down:** Move all identified colored cells to the lowest available row within their respective columns. If multiple objects exist in the same column, stack them from bottom to top in the order they appeared in the input (top to bottom).

3. **Fill with White** Fill with white the cells left by the objects

In summary: This transformation moves each non-white cell down to the lowest available position in its column, effectively "dropping" the colored cells to the bottom, and filling the other positions with white.

The code written for the first example work as is for this second example.

```python
"""
The colored cells are moved to the last row of the output, the other cells are filled with white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white cells to the last row,
    preserving their original column order, and filling the remaining cells with white.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find non-white cells and store their color and column
    non_white_cells = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((input_grid[r, c], c))

    # Place the non-white cells in the last row
    for i, (color, col) in enumerate(non_white_cells):
        output_grid[rows - 1, col] = color

    return output_grid
```

