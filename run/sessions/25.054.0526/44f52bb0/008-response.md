# 44f52bb0 • 008 • example_2 • investigate_coder

---
```python
"""
Counts the number of cells with the value '2' (red cells) in the input grid.
If the count is 3, the function returns 7.
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to numpy array for easier processing
    input_grid = np.array(input_grid)

    # Count the number of cells with value 2
    red_cells_count = np.sum(input_grid == 2)

    # return specific value
    if red_cells_count == 3:
      output = 7
    else:
      output = 0 # place holder
    
    return output
```

