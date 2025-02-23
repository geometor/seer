# 5bd6f4ac • 002 • example_1 • investigate_coder

---
```python
"""
Extract a 3x3 sub-grid from the input grid, starting at row 0, column 6.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier slicing.
    input_array = np.array(input_grid)

    # Extract the 3x3 sub-grid.
    output_array = input_array[0:3, 6:9]

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid
```

