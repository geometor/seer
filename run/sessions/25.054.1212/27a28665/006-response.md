# 27a28665 • 006 • refine_coder

---
```python
"""
Counts the number of times the most frequent non-white color appears in the
input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Calculates the count of the most frequent non-white color and
    returns it as a 1x1 grid.
    """
    input_array = np.array(input_grid)

    # Find all non-white colors.
    non_white_colors = input_array[input_array != 0]

    # If there are no non-white colors, return 0.
    if non_white_colors.size == 0:
        return np.array([[0]])

    # Count the occurrences of each non-white color.
    unique, counts = np.unique(non_white_colors, return_counts=True)
    
    # Find maximum count
    max_count = np.max(counts)

    # Create a 1x1 output grid with the maximum count.
    output_grid = np.array([[max_count]])

    return output_grid
```

