# 4-0d3d703e • 004 • example_2 - CODE

---
```python
"""
The transformation rule is a one-to-one color mapping:
2 (red) -> 5 (magenta)
3 (green) -> 6 (yellow)
8 (azure) -> 9 (maroon)
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
        2: 5,  # red -> magenta
        3: 6,  # green -> yellow
        8: 9   # azure -> maroon
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

