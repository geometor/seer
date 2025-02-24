# f25ffba3 • 002 • example_1 • investigate_coder

---
```python
"""
The rows of the input grid are reordered to produce the output grid. The rows are reordered
based on the vertical line of green (3) and maroon (9) pixels on the right edge of the grid.
Specifically, the bottom five rows are extracted and then prepended to itself in reversed order.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid.
    # output_grid = np.copy(input_grid)
    
    # Extract bottom five rows.
    bottom_five_rows = input_grid[5:, :]
    
    # Reverse the order of extracted rows.
    reversed_bottom_five = bottom_five_rows[::-1, :]
    
    # Concatenate the reversed rows with bottom 5 rows.
    output_grid = np.concatenate((reversed_bottom_five, bottom_five_rows), axis=0)

    return output_grid
```
