# 4-0d3d703e • 008 • example_4 - CODE

---
```python
"""
The program performs a one-to-one mapping of pixel values in a 3x3 grid.  Each input value is replaced by a corresponding output value according to the following rule:

1.  If the input pixel is 9, replace it with 8.
2.  If the input pixel is 4, replace it with 3.
3.  If the input pixel is 2, replace it with 6.

The spatial structure of the grid remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a grid by mapping specific input values to output values.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)
    
    # Apply the mapping rules:
    output_grid[input_grid == 9] = 8  # Replace 9 with 8
    output_grid[input_grid == 4] = 3  # Replace 4 with 3
    output_grid[input_grid == 2] = 6  # Replace 2 with 6
    
    return output_grid
```

