# 6e02f1e3 • 020 • example_4 • investigate_coder

---
```python
"""
The input grid is transformed by replacing the top row with the value 5 (gray) and the middle and bottom rows with the value 0 (white). The grid dimensions remain 3x3.
"""

import numpy as np

def transform(input_grid):
    # Create an output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Replace the top row with 5 (gray).
    output_grid[0, :] = 5

    # Replace the middle and bottom rows with 0 (white).
    output_grid[1:, :] = 0

    return output_grid
```
