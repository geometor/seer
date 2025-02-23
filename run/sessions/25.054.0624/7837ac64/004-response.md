# 7837ac64 • 004 • refine_coder

---
```python
"""
The transformation extracts a 3x3 subgrid from the input grid. The subgrid is identified
by a distinct 3x3 color pattern, prioritizing the top-leftmost occurrence if multiple
such patterns exist.
"""

import numpy as np

def find_distinct_3x3(input_grid):
    """
    Finds the top-leftmost 3x3 subgrid with a distinct color pattern.
    """
    rows, cols = input_grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            subgrid = input_grid[r:r+3, c:c+3]
            if is_distinct(subgrid):
                return r, c
    return None, None

def is_distinct(subgrid):
    """
    Checks if a 3x3 subgrid has a distinct color pattern.  This is a placeholder
    for a more robust pattern detection, which could involve checking for:
    - Diagonal color matches.
    - Specific corner colors.
    - Row/column color repetitions or alternations.
    - More than 'n' unique colors
    
    For this iteration it is more unique than solid colors.
    """
    unique_colors = np.unique(subgrid)
    return unique_colors.size > 1 and unique_colors.size < 9


def transform(input_grid):
    # Find the top-leftmost distinct 3x3 subgrid
    r, c = find_distinct_3x3(input_grid)

    # If no distinct subgrid is found, return a default 3x3 white grid
    if r is None or c is None:
        return np.zeros((3, 3), dtype=int)

    # Extract and return the 3x3 subgrid
    output_grid = input_grid[r:r+3, c:c+3]
    return output_grid
```
