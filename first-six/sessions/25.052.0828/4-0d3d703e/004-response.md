# 4-0d3d703e • 004 • refine_code - CODE

---
```python
"""
Transformation Rule:

1.  **Identify Objects:** The objects are individual cells within the grid, each with a specific color.
2.  **Color Substitution**: Replace the color of each cell based on the following mapping:
    *   Green (3) -> Yellow (4)
    *   Blue (1) -> Gray (5)
    *   Red (2) -> Magenta (6)
    *   Yellow (4) -> Green (3)
    *   Maroon (9) -> Azure (8)
3.  **Preserve Structure**: The grid's structure and dimensions remain unchanged; only the colors of individual cells are modified.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a specific color substitution rule.
    """
    output_grid = np.copy(input_grid)  # Create a copy of the input grid to modify.

    # Iterate through each cell in the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply the color substitution rules.
            if output_grid[i, j] == 3:  # Green to Yellow
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:  # Blue to Gray
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:  # Red to Magenta
                output_grid[i, j] = 6
            elif output_grid[i, j] == 4:  # Yellow to Green
                output_grid[i, j] = 3
            elif output_grid[i, j] == 9:  # Maroon to Azure
                output_grid[i, j] = 8

    return output_grid
```

