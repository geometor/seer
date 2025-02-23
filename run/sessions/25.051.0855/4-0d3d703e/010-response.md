# 4-0d3d703e • 010 • example_3 - CODE

---
```python
"""
The transformation rule is a color mapping:
1. Identify vertical lines of the same color.
2. Map colors:
   - Replace color 5 (gray) with color 1 (blue).
   - Replace color 8 (azure) with color 9 (maroon).
   - Replace color 6 (magenta) with color 2 (red).
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
            if output_grid[i, j] == 5:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 2

    return output_grid
```

