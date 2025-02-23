# 29ec7d0e • 020 • example_4 • investigate_coder

---
```python
"""
The transformation rule is to remove all pixels of the color white (0). The input grid is iterated, and if a cell has color white it gets removed in the new output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the indices of all white (0) pixels.
    white_indices = np.where(output_grid == 0)

    # change output pixels
    # Set all white pixels to some impossible value -1 to make them invisble.
    output_grid[white_indices] = -1

    return output_grid
```
