# 3c9b0459 • 020 • example_4 • investigate_coder

---
```python
"""
Swap the values of the cells at positions (0, 1) and (2, 0) with cell (2,1) circularly. All other cells remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by swapping the values of cells (0, 1) and (2,0) 
    circularly with cell (2,1).
    """
    output_grid = np.copy(input_grid)

    # Store original values
    val_0_1 = input_grid[0, 1]
    val_2_0 = input_grid[2, 0]
    val_2_1 = input_grid[2, 1]

    # Perform swaps
    output_grid[0, 1] = val_2_0  # (0,1) <- (2,0)
    output_grid[2, 0] = val_2_1  # (2,0) <- (2,1)
    output_grid[2, 1] = val_0_1   # (2,1) <- (0,1)

    return output_grid
```
