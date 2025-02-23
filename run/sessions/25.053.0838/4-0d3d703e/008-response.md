# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The transformation rule is a one-to-one color mapping:
9 (maroon) -> 8 (azure)
4 (yellow) -> 3 (green)
2 (red) -> 6 (magenta)
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
        9: 8,  # maroon -> azure
        4: 3,  # yellow -> green
        2: 6   # red -> magenta
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

