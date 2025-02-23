# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a one-to-one color mapping:
1 (blue) -> 4 (yellow)
2 (red) -> 5 (gray)
3 (green) -> 6 (magenta)
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        1: 4,  # blue -> yellow
        2: 5,  # red -> gray
        3: 6   # green -> magenta
    }

    # Iterate through each pixel in the grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Apply color mapping.
            original_color = input_grid[i, j]
            if original_color in color_map:
              output_grid[i, j] = color_map[original_color]

    return output_grid
```
