# beb8660c • 002 • example_1 • investigate_coder

---
```python
"""
The input grid is rotated 90 degrees clockwise to produce the output grid.
"""

import numpy as np

def rotate_grid_clockwise(grid):
    """Rotates a 2D numpy array 90 degrees clockwise."""
    return np.rot90(grid, k=-1)

def transform(input_grid):
    """
    Transforms the input grid by rotating it 90 degrees clockwise.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Rotate the array 90 degrees clockwise.
    output_array = rotate_grid_clockwise(input_array)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid
```
