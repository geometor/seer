# f2829549 • 020 • example_4 • investigate_coder

---
```python
"""
1.  **Focus on a Sub-region:** Examine the leftmost 3x3 sub-grid within the 4x7 input grid.
2. **Color Mapping**:
    *   If any cell in column 1,2 or 3 is orange (7), in the same row set that cell to green (3).
    *   Otherwise if cell is 0,1,5 keep color as white(0).
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((4, 3), dtype=int)

    # change output pixels 
    for i in range(4):
        for j in range(3):
            if input_grid[i][j] == 7:
                output_grid[i][j] = 3
            else:
                output_grid[i][j] = 0


    return output_grid
```
