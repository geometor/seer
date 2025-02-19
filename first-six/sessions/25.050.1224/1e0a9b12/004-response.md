# 1e0a9b12 • 004 • example_2 - CODE

---
Okay, let's analyze the transformation between the input and output grids.

**Observations:**

Input Grid:

-   Dimensions: 4x4
-   Colors present: 0 (white), 1 (blue), 4 (yellow), 6 (magenta), 9 (maroon)
-   Objects:
    -   A single blue cell (1) at (3, 0).
    -   Two single yellow cells (4) at (0, 1) and (2, 1).
    -   A single magenta cell (6) at (2,2).
    -    A single maroon cell (9) at (0,3)

Output Grid:

-   Dimensions: 4x4
-   Colors present: 0 (white), 1 (blue), 4 (yellow), 6 (magenta), 9 (maroon)
-   Objects:
    -   A single blue cell (1) at (3, 0).
    -    A single yellow cell (4) at (3,1)
    -   A single magenta cell (6) at (3, 2).
    -   A single maroon cell (9) at (3, 3).

**Transformation Rule (Natural Language Program):**

1.  **Identify Objects:** Locate all non-white cells in the input grid. These are our objects.

2.  **Move Down:** Shift the identified colored cells to the last row of the grid.

3. **Preserve X, Sort by X** The colored cells preserve the column, that is their horizontal (X) position.

4. **Fill with White** Fill the cells that the objects leaved with white.

In summary: The colored cells are moved to the last row of the output, the other cells are filled with white.


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

