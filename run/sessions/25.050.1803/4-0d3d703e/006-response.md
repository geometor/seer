# 4-0d3d703e • 006 • example_3 - CODE

---
**input**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 9
0 0 0 0 0 0
```

![Image](003-test_input.png)

**Natural Language Program:**

The transformation rule involves a color substitution based on a single instance of color 9 (maroon) present in the input grid.  Specifically, the maroon pixel is replaced with color 8 (azure). All other colors are unchanged, remaining 0 (white) in this case.

```python
"""
The transformation rule involves a color substitution based on a single instance of color 9 (maroon) present in the input grid.
Specifically, the maroon pixel is replaced with color 8 (azure). All other colors are unchanged, remaining 0 (white) in this case.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through the grid to find and change the color 9 (maroon) pixel to color 8 (azure).
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 9:
                output_grid[i, j] = 8

    return output_grid
```

