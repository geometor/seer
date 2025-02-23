# 74dd1130 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is a 90-degree clockwise rotation of the grid.

1.  Consider the input grid.
2.  Imagine rotating the entire grid 90 degrees in a clockwise direction.
3.  The resulting arrangement of elements after the rotation is the output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input list of lists to a NumPy array
    input_np = np.array(input_grid)

    # Rotate the array 90 degrees clockwise
    output_np = np.rot90(input_np, k=-1)

    # Convert the NumPy array back to a list of lists
    output_grid = output_np.tolist()

    return output_grid
```
