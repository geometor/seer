# 3c9b0459 • 002 • example_1 • investigate_coder

---
```python
"""
The input grid is rotated 90 degrees counter-clockwise to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Rotate the array 90 degrees counter-clockwise.
    output_array = np.rot90(input_array, k=1) # k=1 for 90-degree rotation

    # Convert the rotated array back to a list.
    output_grid = output_array.tolist()

    return output_grid
```
