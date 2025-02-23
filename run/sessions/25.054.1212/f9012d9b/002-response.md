# f9012d9b • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Region:** Focus on the top-left 2x2 subgrid of the input grid.
2.  **Extract Subgrid**: Copy the color values from the top left 2x2 of input into output
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by extracting the top-left 2x2 subgrid.
    """
    # Initialize the output grid as a 2x2 array.
    output_grid = np.zeros((2, 2), dtype=int)

    # Extract the top-left 2x2 subgrid from the input grid.
    output_grid[0:2, 0:2] = input_grid[0:2, 0:2]

    return output_grid
```
