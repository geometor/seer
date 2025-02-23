# 8be77c9e • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Mirror:** Take the input grid and create a vertically mirrored copy of it.
2.  **Concatenate:** Vertically concatenate the mirrored copy below the original input grid to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    # Create a vertically mirrored copy of the input grid
    mirrored_grid = np.flipud(input_grid)
    
    # Vertically concatenate the mirrored copy below the original input grid
    output_grid = np.concatenate((input_grid, mirrored_grid), axis=0)
    
    return output_grid
```
