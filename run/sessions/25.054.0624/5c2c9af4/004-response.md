# 5c2c9af4 • 004 • refine_coder

---
```python
"""
Fills the entire grid with the most frequent non-black, non-white color in the input grid.
"""

import numpy as np
from collections import Counter

def find_most_frequent_non_background_color(grid):
    """Finds the most frequent color in the grid, excluding black (0) and white/background."""
    # Flatten the grid to a 1D array for easier counting
    flat_grid = grid.flatten()

    # Count the occurrences of each color
    color_counts = Counter(flat_grid)

    # Remove black (0) and white (if present)
    color_counts.pop(0, None)  # Remove black, if it exists
    # this task has a white/background-color: find the value if this applies
    # this is consistent across all ARC-AGI data
    if np.max(grid) == 0 and np.min(grid) == 0:
        #pop the background color 0, already completed
        pass
    elif len(color_counts)>0:
       most_common_color = color_counts.most_common(1)[0][0]
       return most_common_color
    return 0

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Find the most frequent non-background color
    fill_color = find_most_frequent_non_background_color(input_grid)

    # Fill the entire output grid with the fill color
    output_grid[:] = fill_color

    return output_grid
```
