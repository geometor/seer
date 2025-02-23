# 5582e5ca • 002 • example_1 • investigate_coder

---
```python
"""
1. Identify Target Color: Find the color yellow (represented by the integer 4) within the input grid.
2. Create Output Grid: Create a new grid with the same dimensions as the input grid.
3. Fill Output Grid: Fill every cell of the output grid with the target color (yellow/4).
"""

import numpy as np

def transform(input_grid):
    # Create an output grid with the same dimensions as the input.
    output_grid = np.full(input_grid.shape, 4)  # Fills with yellow (4)

    return output_grid
```
