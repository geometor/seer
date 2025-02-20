# 4-0d3d703e • 004 • example_2 - CODE

---
**input**
```
7 0 0 0
0 7 0 0
0 0 7 0
0 0 0 7
```

![Image](001-test_input.png)

**Natural Language Program:**

The transformation rule involves a color substitution based on the diagonal position of an orange (color 7) pixel relative to the main diagonal (top-left to bottom-right). If the orange pixel is on the main diagonal, it's changed to gray (color 5). If it isn't on the main diagonal, it is changed to black/white (color 0). Every other color is turned to white (0).

```python
"""
The transformation rule involves a color substitution based on the diagonal position of an orange (color 7) pixel relative to the main diagonal (top-left to bottom-right). If the orange pixel is on the main diagonal, it's changed to gray (color 5). If it isn't on the main diagonal, it is changed to black/white (color 0). Every other color is turned to white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    output_grid[:] = 0 # initialize to color 0 (white)

    # Iterate through the grid to find and process orange (color 7) pixels.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if input_grid[i, j] == 7:
                if i == j:  # Check if the pixel is on the main diagonal.
                    output_grid[i, j] = 5  # Change to gray (color 5).
                else:
                    output_grid[i,j] = 0

    return output_grid
```

