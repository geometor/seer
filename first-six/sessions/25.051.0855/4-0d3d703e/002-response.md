# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a color mapping:
1. Identify vertical lines of the same color.
2. Map colors:
   - Replace color 3 (green) with color 4 (yellow).
   - Replace color 1 (blue) with color 5 (gray).
   - Replace color 2 (red) with color 6 (magenta).
3. Preserve the structure and positions of the lines.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    # Create a copy of the input grid to modify.  This ensures we don't alter the original input.
    output_grid = np.copy(input_grid)

    # Apply the color mapping.  We iterate through all cells and change the colors based on the rule.
    # We don't strictly need to search for vertical lines in this simple case because the color mapping applies to every cell.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6

    return output_grid
```

