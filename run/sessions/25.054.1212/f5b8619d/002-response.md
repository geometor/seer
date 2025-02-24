# f5b8619d • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Initialization:** Start with the 3x3 input grid.
2.  **Expansion:** Create a new 6x6 grid.
3.  **Replication with insertion**: For every value on the original grid, copy the value to the new grid in the same relative position as the original, using a 2x2 offset (row *2, col *2).
4. **Border Insertion**: For any position in the new 6x6 grid, If the position does not match any of the co-ordinates created by the above step, insert 8
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 6x6 array filled with 8s.
    output_grid = np.full((6, 6), 8, dtype=int)

    # Iterate through the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Copy each value from input_grid to output_grid with a 2x2 offset.
            output_grid[i*2, j*2] = input_grid[i, j]

    return output_grid
```
