# 44f52bb0 • 002 • example_1 • investigate_coder

---
```python
"""
Counts the number of red (2) pixels in the input grid and outputs a 1x1 grid containing a single blue pixel with value equal to this count.
"""

import numpy as np

def transform(input_grid):
    """
    Counts red pixels in the input and represents the count as a blue pixel in the output.
    """
    # Count the number of red (2) pixels.
    red_count = np.sum(input_grid == 2)

    # Create a 1x1 output grid.
    output_grid = np.array([[red_count]])

    return output_grid
```
