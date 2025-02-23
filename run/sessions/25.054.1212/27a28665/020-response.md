# 27a28665 • 020 • example_4 • investigate_coder

---
```python
"""
Counts the number of blue pixels (value 1) in the input grid and returns the count.
"""

import numpy as np

def transform(input_grid):
    """
    Counts the number of blue pixels (value 1) in the input grid.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        int: The count of blue pixels.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Count the number of pixels with value 1 (blue pixels).
    count = np.count_nonzero(input_array == 1)

    return count
```

