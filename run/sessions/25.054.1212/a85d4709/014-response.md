# a85d4709 • 014 • example_3 • investigate_coder

---
```python
"""
Transforms a 3x3 input grid of gray (5) and white (0) pixels to an output grid of red (2) and yellow (4) pixels. 
Gray pixels on the middle row become yellow, while gray pixels on the top/bottom rows and all white pixels become red.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    output_grid = np.zeros_like(input_grid)  # Initialize output grid

    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] == 5:  # Gray pixel
                if i == 1:  # Middle row
                    output_grid[i, j] = 4  # Yellow
                else:  # Top or bottom row
                    output_grid[i, j] = 2  # Red
            elif input_grid[i, j] == 0:  # White pixel
                output_grid[i, j] = 2  # Red

    return output_grid
```
