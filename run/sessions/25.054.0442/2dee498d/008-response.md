# 2dee498d • 008 • example_2 • investigate_coder

---
```python
"""
The transformation extracts the first instance of a horizontally repeating pattern in the input grid to produce the output.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the first instance of a horizontally repeating pattern.
    """
    # Get the dimensions of the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Determine the width of the repeating unit (output grid width).
    output_cols = 4

    # Initialize the output grid.
    output_grid = []

    # Extract the leftmost sub-grid of the determined width.
    for i in range(rows):
        output_grid.append(input_grid[i][:output_cols])

    return output_grid
```
