# 4-0d3d703e • 014 • example_4 - CODE

---
```python
"""
The transformation rule is a color mapping:
1. Identify vertical lines of the same color.
2. Map colors:
   - Replace color 9 (maroon) with color 8 (azure).
   - Replace color 4 (yellow) with color 3 (green).
   - Replace color 2 (red) with color 6 (magenta).
3. Preserve the structure and positions of the lines.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    # Create a copy of the input grid to modify.
    output_grid = np.copy(input_grid)

    # Apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 9:
                output_grid[i, j] = 8
            elif output_grid[i, j] == 4:
                output_grid[i, j] = 3
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6

    return output_grid
```

