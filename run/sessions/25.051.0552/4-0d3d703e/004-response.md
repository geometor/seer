# 4-0d3d703e • 004 • example_2 - CODE

---
```python
"""
The transformation rule is a simple color mapping:
- Color 2 (red) becomes color 6 (magenta).
- Color 3 (green) becomes color 4 (yellow).
- Color 8 (azure) becomes color 9 (maroon).
The structure of the grid remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    - 2 (red) -> 6 (magenta)
    - 3 (green) -> 4 (yellow)
    - 8 (azure) -> 9 (maroon)
    Maintains the original grid structure.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply the color mapping
    output_grid[input_grid == 2] = 6  # Replace all occurrences of 2 with 6
    output_grid[input_grid == 3] = 4  # Replace all occurrences of 3 with 4
    output_grid[input_grid == 8] = 9  # Replace all occurrences of 8 with 9

    return output_grid
```

