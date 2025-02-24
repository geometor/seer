# d90796e8 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Key Colors:** Locate all pixels that are green (value 3) or red (value 2).
2.  **Check gray**: do not change any colors if color is gray (5)
3.  **Change Color to Azure:** Change the color of the located green(3) and red(2) to azure (value 8)
4. **Preserve the rest:** All the other pixels remains unchaged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    output_grid = np.copy(input_grid)  # Initialize output as a copy of input
    rows, cols = output_grid.shape

    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is green or red
            if output_grid[r, c] == 3 or output_grid[r, c] == 2:
                output_grid[r, c] = 8  # Change to azure

    return output_grid
```
