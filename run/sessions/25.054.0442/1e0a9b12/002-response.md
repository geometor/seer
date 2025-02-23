# 1e0a9b12 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is to collect all non-zero elements from the input grid and place them, maintaining their original horizontal order, in the last row of the output grid. The remaining cells of the output grid are filled with zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the bottom row,
    maintaining their original horizontal order, and filling the rest with zeros.
    """
    # Initialize the output grid with the same dimensions as the input, filled with zeros.
    output_grid = np.zeros_like(input_grid)

    # Extract all non-zero elements from the input grid.
    non_zero_elements = [val for row in input_grid for val in row if val != 0]

    # Place the non-zero elements in the last row of the output grid.
    output_grid[-1, :len(non_zero_elements)] = non_zero_elements

    return output_grid
```
