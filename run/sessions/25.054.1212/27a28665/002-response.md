# 27a28665 • 002 • example_1 • investigate_coder

---
```python
"""
Counts the number of distinct colors in the input grid, excluding white (0),
and returns this count as a 1x1 grid.
"""

import numpy as np

def transform(input_grid):
    """
    Counts non-white colors in the input and returns the count as a 1x1 grid.
    """
    # Convert input grid to numpy array for easier manipulation.
    input_array = np.array(input_grid)

    # Find unique colors, excluding 0 (white).
    unique_colors = np.unique(input_array)
    unique_colors_excluding_white = unique_colors[unique_colors != 0]

    # Count the number of unique colors (excluding white).
    count = len(unique_colors_excluding_white)

    # Create a 1x1 output grid with the count.
    output_grid = np.array([[count]])

    return output_grid
```

