# d631b094 • 002 • example_1 • investigate_coder

---
```python
"""
1. Count the number of blue (1) pixels in the input grid.
2. Create an output grid. The number of cells in the output is the same count.
3. Fill all cells output grid with blue (1) pixels.
"""

import numpy as np

def transform(input_grid):
    # Count the number of blue (1) pixels.
    blue_count = np.sum(input_grid == 1)

    # Create an output grid with a width equal to the blue count and height 1.
    output_grid = np.ones((1, blue_count), dtype=int)
    
    return output_grid
```
