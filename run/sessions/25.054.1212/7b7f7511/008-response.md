# 7b7f7511 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation extracts every other column from the input grid, starting from the first column. It's equivalent to keeping the first, third, fifth, etc. columns and discarding the rest. The remaining columns form the output grid, preserving the row structure.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by selecting every other column, starting from the first.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The transformed grid with selected columns.
    """
    # Convert input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Get the number of columns in the input grid
    num_cols = input_array.shape[1]

    # Create a list to store the indices of the columns to keep
    cols_to_keep = []
    for i in range(num_cols):
        if i % 2 == 0:  # Check if the column index is even (0, 2, 4, ...)
            cols_to_keep.append(i)

    # Use NumPy's column indexing to select the desired columns
    output_array = input_array[:, cols_to_keep]

    # Convert the NumPy array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid
```
