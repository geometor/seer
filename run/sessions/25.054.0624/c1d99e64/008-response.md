# c1d99e64 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Initialization:** Start with the input grid.
2.  **Identify Target Pixels:** Identify all pixels in the grid that meet *both* of the following conditions:
    *   The pixel's color is white (0).
    *   The pixel's column index follows the pattern: column index mod 5 equals 4. That is starting at index 4 increment by 5 (4, 9, 14, 19, ...) .
3.  **Color Replacement:** For every pixel identified in step 2, change its color from white (0) to red (2).
4  **Preserve Other:** All other pixels retain their original color.
5.  **Output:** The modified grid is the output.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by changing white pixels to red in every 5th column, starting from the 5th."""
    output_grid = np.copy(input_grid)  # Initialize output grid
    rows, cols = output_grid.shape

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Check conditions: color is white and column index mod 5 is 4
            if output_grid[r, c] == 0 and c % 5 == 4:
                # Replace white with red
                output_grid[r, c] = 2

    return output_grid
```
