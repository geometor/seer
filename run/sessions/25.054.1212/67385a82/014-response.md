# 67385a82 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Locate Green Pixels:** Identify all pixels with the value 3 (green).

2.  **Conditional Replacement:**
    *   If the green pixel is in the top right corner (row 0, col 3), change the cell immediately below (row 1, col 3) to white(0).
    *   If the green pixel is in the bottom left corner (row 2, col 0), change the color to azure (8)

3.  **No change:** all other pixels remain the same color.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid to find green pixels
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 3:  # Green pixel found
                # Conditional Replacement based on location
                if r == 0 and c == 3:
                    output_grid[1, 3] = 0 #change cell below to white
                elif r == 2 and c == 0:
                    output_grid[r, c] = 8  #change green to azure

    return output_grid
```
