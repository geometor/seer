# 44f52bb0 • 002 • example_1 • investigate_coder

---
```python
"""
Counts the number of red pixels in the input grid and returns a 1x1 grid with a blue pixel if the count is greater than 0.
"""

import numpy as np

def transform(input_grid):
    # Count the number of red pixels (value '2')
    red_count = np.count_nonzero(input_grid == 2)

    # Create a 1x1 output grid
    output_grid = np.zeros((1, 1), dtype=int)

    # Set the single pixel to blue (value '1') if red count > 0
    if red_count > 0:
      output_grid[0, 0] = 1

    return output_grid
```
