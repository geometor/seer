# a416b8f3 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is to duplicate the input grid horizontally. Each column in the input is replicated once, resulting in an output grid twice the width.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by duplicating it horizontally.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The transformed grid, which is a horizontal duplication of the input.
    """
    # Convert input_grid to numpy array for easier manipulation
    input_array = np.array(input_grid)

    # Get dimensions of the input array
    rows, cols = input_array.shape

    # Create a new array with double the width
    output_array = np.zeros((rows, cols * 2), dtype=int)

    # Copy the original grid into the left half of the output
    output_array[:, :cols] = input_array

    # Copy the original grid into the right half of the output
    output_array[:, cols:] = input_array

    # Convert the output array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid
```
