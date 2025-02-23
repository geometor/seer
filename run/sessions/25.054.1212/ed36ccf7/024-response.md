# ed36ccf7 • 024 • refine_coder

---
```python
"""
The transformation rule is a 90-degree clockwise rotation of the grid. The colors in the rotated grid are the same as the corresponding cells in the input grid before rotation.

1.  **Rotate:** Rotate the whole grid by 90-degree clockwise
2.  **Preserve Colors**:  No change is required, colors are preserved after the rotation.
"""

import numpy as np

def rotate_grid_90_clockwise(grid):
    return np.rot90(grid, k=-1)

def transform(input_grid):
    # initialize output_grid by rotating the input
    output_grid = rotate_grid_90_clockwise(np.array(input_grid))

    return output_grid.tolist()
```
