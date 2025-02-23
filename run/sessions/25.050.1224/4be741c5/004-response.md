# 4be741c5 • 004 • example_2 - CODE

---
```python
"""
The transformation rule identifies distinct colored regions in the input grid and represents each with a single cell in the output grid. The output is a 1x3 grid with cells ordered according to a predefined sequence: yellow (4), red (2), and azure (8).
"""

import numpy as np

def get_distinct_colors(grid):
    """
    Returns a list of distinct colors present in the grid.
    """
    return np.unique(grid).tolist()

def transform(input_grid):
    """
    Transforms the input grid into a 1x3 grid representing the distinct colors in a specific order.
    """
    # Get the distinct colors from the input grid
    distinct_colors = get_distinct_colors(input_grid)

    # Initialize the output grid
    output_grid = []

    # Define the specific order of colors
    color_order = [4, 2, 8]

    # Filter and order the colors present in the input grid
    for color in color_order:
        if color in distinct_colors:
            output_grid.append(color)

    # Reshape the output to 1xN (where N is the number of colors found, up to 3)
    return np.array(output_grid).reshape(1, -1)
```

