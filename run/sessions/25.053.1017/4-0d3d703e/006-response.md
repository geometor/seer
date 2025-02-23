# 4-0d3d703e • 006 • example_3 - CODE

---
```python
"""
The input grid is transformed into the output grid by applying a fixed substitution rule to each number. The rule is:

1.  Replace the number 5 with the number 1.
2.  Replace the number 8 with the number 9.
3.  Replace the number 6 with the number 2.

This rule is applied to every cell in the input grid to produce the corresponding cell in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Apply the substitution rule: 5 -> 1, 8 -> 9, 6 -> 2.
    output_grid[input_grid == 5] = 1
    output_grid[input_grid == 8] = 9
    output_grid[input_grid == 6] = 2
    
    return output_grid
```
