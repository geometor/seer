# 3c9b0459 • 006 • refine_coder

---
```python
"""
The input grid is rotated by -90 degrees (270 degrees clockwise). The rows of the input become the columns of the output in reversed order, and columns become rows. Consider the center of the grid as center of rotation.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by -90 degrees (270 degrees clockwise).

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The rotated grid.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Rotate the array by -90 degrees (270 clockwise).
    rotated_array = np.rot90(input_array, k=3)  # k=3 for 270-degree rotation

    # Convert the rotated array back to a list of lists.
    output_grid = rotated_array.tolist()

    return output_grid
```
