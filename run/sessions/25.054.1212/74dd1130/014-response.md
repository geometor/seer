# 74dd1130 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation rule is: The value '5' at position (1,0) changes into a '9', the '9' at (0,0) stays as '9'.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Apply the specific rule:
    # The value '5' at position (1,0) changes into a '9', the '9' at (0,0) stays at '9'
    output_grid[1,0] = input_grid[0,0]


    return output_grid
```
