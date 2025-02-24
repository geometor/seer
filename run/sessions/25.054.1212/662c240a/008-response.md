# 662c240a • 008 • example_2 • investigate_coder

---
```python
"""
Extracts a 3x3 sub-grid from the input grid. The sub-grid starts at row 4 (index 3) and ends at row 6 (index 5), spanning columns 1 to 3 (indices 0 to 2).
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier slicing.
    input_array = np.array(input_grid)

    # Extract the 3x3 sub-grid.  Numpy slicing is exclusive of the end index.
    output_array = input_array[3:6, 0:3]

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid
```
