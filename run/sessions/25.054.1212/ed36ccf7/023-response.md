# ed36ccf7 • 023 • refine_coder

---
```python
"""
Identify contiguous blocks of non-zero pixels. Rotate the input grid 90 degrees clockwise to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid 90 degrees clockwise.
    """
    # Convert input_grid to a NumPy array for easier manipulation.
    input_grid = np.array(input_grid)

    # Rotate the grid 90 degrees clockwise.
    output_grid = np.rot90(input_grid, k=-1)

    return output_grid.tolist()
```
