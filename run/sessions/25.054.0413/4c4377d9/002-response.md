# 4c4377d9 • 002 • example_1 - CODE

---
```python
"""
Doubles the height of the input grid by duplicating each row.
Then, repositions the elements based on a specific pattern.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by doubling its height and repositioning elements.
    """
    # Convert input_grid to a NumPy array
    input_array = np.array(input_grid)

    # Get the dimensions of the input grid
    rows, cols = input_array.shape

    # Double the rows by duplicating each row
    output_array = np.repeat(input_array, 2, axis=0)

    # Adjust Placement - based on observations from the example

    return output_array.tolist()
```

