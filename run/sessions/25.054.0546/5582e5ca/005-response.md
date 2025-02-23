# 5582e5ca • 005 • refine_coder

---
```python
"""
The output grid is the same dimensions as the input grid. The output grid is
filled entirely with a single color. The color chosen for the output grid is
the most frequently occurring color in the input grid. If multiple colors share
the highest frequency, the color chosen appears to be consistent.
"""

import numpy as np
from collections import Counter

def transform(input_grid):
    """Transforms an input grid by filling it with the most frequent color."""
    # Convert the input grid to a NumPy array for easier processing.
    input_grid = np.array(input_grid)
    # Determine the shape of the input grid.
    rows, cols = input_grid.shape
    # Initialize the output grid with the same dimensions and filled with zeros.
    output_grid = np.zeros((rows, cols), dtype=int)

    # Count the occurrences of each color in the input grid.
    color_counts = Counter(input_grid.flatten())

    # Find the most frequent color(s).
    max_count = 0
    most_frequent_colors = []
    for color, count in color_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_colors = [color]
        elif count == max_count:
            most_frequent_colors.append(color)

    # Select the most frequent color (handling potential ties).
    # NOTE: current tie-breaking is arbitrary (selects first)
    most_frequent_color = most_frequent_colors[0]

    # Fill the output grid with the most frequent color.
    output_grid[:] = most_frequent_color

    return output_grid
```

