# 0d3d703e • 008 • example_2 - CODE

---
```python
"""
The program takes the numbers from the input grid, and performs a direct substitution based on these rules: 2 becomes 6, 3 becomes 4, and 8 becomes 9. The structure of the grid doesn't change, just the values in the cells change.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # change output pixels based on the substitution rules
    output_grid[input_grid == 2] = 6
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 8] = 9

    return output_grid
```
