# 4-0d3d703e • 006 • example_3 - CODE

---
```python
"""
The transformation rule is a one-to-one color mapping:
5 (gray) -> 1 (blue)
8 (azure) -> 9 (maroon)
6 (magenta) -> 2 (red)
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
        5: 1,  # gray -> blue
        8: 9,  # azure -> maroon
        6: 2   # magenta -> red
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

