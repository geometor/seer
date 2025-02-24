# d23f8c26 • 008 • example_2 • investigate_coder

---
```python
"""
Copies the center column of the input grid to the output grid, setting all other cells to 0.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by keeping only the center column and setting all other cells to 0.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The transformed grid.
    """
    # Convert input to numpy array for easier handling
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Initialize output_grid as a zero-filled array of the same dimensions
    output_array = np.zeros_like(input_array)

    # Check if the grid has a center column (odd number of columns)
    if cols % 2 != 0:
        center_col = cols // 2

        # Copy the center column from the input to the output
        output_array[:, center_col] = input_array[:, center_col]

    # convert the output numpy array to output_grid
    output_grid = output_array.tolist()
    return output_grid
```
