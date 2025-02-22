# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
Transformation Rule:

1. **Identify Objects:** For each column (or vertical line of cells) in the input grid, identify its color.
2. **Color Substitution**: Replace the color of each column by the corresponding color as follows:
    *   If color is Green (3), change to the column to Yellow (4)
    *   If color is Blue (1), change to the column to Gray (5)
    *   If color is Red (2), change to the column to Magenta (6)
3. **Preserve Structure**: Maintain the shape of each column during transformation.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy to preserve structure.

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

    return output_grid
```

