# 4-0d3d703e • 006 • example_2 - CODE

---
```python
"""
The transformation rule is a color mapping:
1. Identify vertical lines of the same color.
2. Map colors:
   - Replace color 2 (red) with color 6 (magenta).
   - Replace color 3 (green) with color 4 (yellow).
   - Replace color 8 (azure) with color 9 (maroon).
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
            if output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9

    return output_grid
```

