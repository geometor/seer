# 3c9b0459 • 004 • refine_coder

---
```python
"""
The input grid is reflected across the diagonal axis running from the top-right corner to the bottom-left corner.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)
    
    # Get the size of the grid (assuming it's square).
    n = input_array.shape[0]

    # Create an empty output array of the same size.
    output_array = np.zeros_like(input_array)

    # Reflect across the top-right to bottom-left diagonal.
    for i in range(n):
        for j in range(n):
            output_array[i, j] = input_array[n - 1 - j, n - 1 - i]

    # Convert the NumPy array back to a list.
    output_grid = output_array.tolist()

    return output_grid
```
