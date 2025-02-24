# 99fa7670 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Non-zero Pixels:** Locate all pixels in the input grid that have a non-zero value (i.e., not white).
2.  **Horizontal Expansion:** For each non-zero pixel, extend its color horizontally across its entire row, replacing any 0 values.
3. **Fill Down:** For each non-zero pixel, starting at their initial location, expand vertically down to the bottom of the grid.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify non-zero pixels and their positions
    non_zero_pixels = []
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] != 0:
                non_zero_pixels.append((r, c, output_grid[r, c]))

    # Horizontal Expansion and fill down
    for r, c, color in non_zero_pixels:
        # Horizontal Expansion
        output_grid[r, :] = color
        # Fill Down.
        for i in range(r, rows):
            output_grid[i,c] = color
            
    return output_grid
```
