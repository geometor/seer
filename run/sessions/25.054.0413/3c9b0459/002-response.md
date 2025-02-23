# 3c9b0459 • 002 • example_1 - CODE

---
```python
"""
The input grid is rotated by 180 degrees to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by 180 degrees.

    Args:
        input_grid (list of lists): A 2D list representing the input grid.

    Returns:
        list of lists: The rotated grid.
    """
    # Convert the input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Rotate the array by 180 degrees using numpy's rot90 function twice
    rotated_array = np.rot90(input_array, 2)

    # Convert the rotated array back to a list of lists
    output_grid = rotated_array.tolist()

    return output_grid
```
