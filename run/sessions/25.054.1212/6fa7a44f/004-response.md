# 6fa7a44f • 004 • refine_coder

---
```python
"""
The transformation rule is to take the input grid and create a new output grid that is double the height. The first half of the output is an exact copy of input. The next half of the grid will contain the rows of the input, but attached in reverse order.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # reverse the input grid
    reversed_input_grid = np.flipud(input_grid)
    
    # change output pixels 
    output_grid = np.concatenate((output_grid, reversed_input_grid), axis=0)

    return output_grid
```
