# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a simple color mapping:
- Color 3 (green) becomes color 4 (yellow).
- Color 1 (blue) becomes color 5 (gray).
- Color 2 (red) becomes color 6 (magenta).
The structure of the grid remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    - 3 (green) -> 4 (yellow)
    - 1 (blue) -> 5 (gray)
    - 2 (red) -> 6 (magenta)
    Maintains the original grid structure.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply the color mapping
    output_grid[input_grid == 3] = 4  # Replace all occurrences of 3 with 4
    output_grid[input_grid == 1] = 5  # Replace all occurrences of 1 with 5
    output_grid[input_grid == 2] = 6  # Replace all occurrences of 2 with 6

    return output_grid
```

