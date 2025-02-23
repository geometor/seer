# 5582e5ca • 002 • example_1 • investigate_coder

---
```python
"""
The transformation identifies the most frequent color in the input grid and flood-fills the output grid with that color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by flood-filling the output with the most frequent color.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the output grid.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Count the occurrences of each color
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    
    # Find the most frequent color
    most_frequent_color_index = np.argmax(counts)
    most_frequent_color = unique_colors[most_frequent_color_index]

    # change output pixels 
    output_grid[:] = most_frequent_color

    return output_grid
```

