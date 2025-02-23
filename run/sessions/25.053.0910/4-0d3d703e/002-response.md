# 4-0d3d703e • 002 • example_1 - CODE

---
```python
"""
The transformation rule is a simple color substitution. 
- Blue(1) becomes gray(5).
- Red(2) becomes magenta(6).
- Green(3) becomes yellow(4).
The spatial arrangement of pixels remains constant.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color substitution.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Apply the color substitution:
    # - Blue (1) becomes gray (5)
    # - Red (2) becomes magenta (6)
    # - Green (3) becomes yellow (4)
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6
    output_grid[input_grid == 3] = 4

    return output_grid
```

