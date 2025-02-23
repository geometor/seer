# 0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a simple integer substitution. Every instance of the number 3 is replaced with 4, every instance of the number 1 is replaced with 5 and every instance of 2 is replaced by 6. The grid dimensions (3x3) remain unchanged, and the relative positions of all elements stay the same. Essentially this is can be described as addition of +1 to each element, and elements can only contains single digits, 0-9..
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Apply the substitution rule: 3 -> 4, 1 -> 5, 2 -> 6
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6

    return output_grid
```
