# d037b0a7 • 002 • example_1 • investigate_coder

---
```python
"""
Fill the rightmost column with magenta (6), while leaving all other input pixels unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Get the width of the grid.
    width = output_grid.shape[1]

    # Fill the rightmost column with magenta (6).
    output_grid[:, width - 1] = 6

    return output_grid
```

