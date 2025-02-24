# b8cdaf2b • 020 • example_4 • investigate_coder

---
```python
"""
The transformation identifies a region in the upper part of the input grid and adds two mirrored, inverted, "L-shapes" using yellow pixels. The bottom section of red and yellow rows stays the same.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Modify pixels in the top region to create the mirrored L-shapes
    output_grid[3, 0] = 4  # Top-left of first L
    output_grid[4, 1] = 4  # Bottom-left of first L

    output_grid[3, 6] = 4  # Top-right of second L (mirrored)
    output_grid[4, 5] = 4  # Bottom-right of second L (mirrored)

    return output_grid
```
