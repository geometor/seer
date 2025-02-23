# 6d0aefbc • 004 • refine_coder

---
```python
"""
The transformation rule duplicates the input grid by appending a mirrored version of the original columns.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by appending a mirrored version of its columns.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed grid with mirrored columns appended.
    """
    # Convert the input grid to a NumPy array
    input_array = np.array(input_grid)

    # Reverse the order of columns
    reversed_array = input_array[:, ::-1]

    # Concatenate the original and reversed arrays along the column axis (axis=1)
    output_array = np.concatenate((input_array, reversed_array), axis=1)

    # Convert the output NumPy array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid
```
