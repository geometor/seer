# 25d8a9c8 • 011 • refine_coder

---
```python
"""
1.  **Identity Transformation:** If the grid contains *only* the colors 1, 2, 4, or 9, the output grid is identical to the input grid.

2.  **Color 6 Replacement:** If color 6 is present in the input grid, replace all instances of color 6 with color 5 in the output grid.

3.  **Color 3 and 7 Replacement:** If Color 3 and/or 7 is present, change it to color 0 (black).

4.  **Conditional Color Change:** If none of conditions 1-3 apply, examine other pixel colors

    *   If 3 is present, it will be transformed to black(0).
    *   If 7 is present, it will be transformed to black(0).
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)  # Start with a copy

    unique_colors = np.unique(input_grid)

    # Condition 1: Identity Transformation
    if np.all(np.isin(unique_colors, [1, 2, 4, 9])):
        return output_grid

    # Condition 2: Color 6 Replacement
    if 6 in unique_colors:
        output_grid[input_grid == 6] = 5

    # Condition 3 & 4: Color 3 and 7 Replacement
    if 3 in unique_colors:
        output_grid[input_grid == 3] = 0
    if 7 in unique_colors:
        output_grid[input_grid == 7] = 0


    return output_grid
```

