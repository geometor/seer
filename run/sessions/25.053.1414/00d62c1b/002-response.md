# 00d62c1b • 002 • example_1 - CODE

---
```python
"""
1.  **Identify:** Locate all pixels within the input grid that have a value of '3' (green).
2.  **Iterate:** For each pixel found in step 1, examine its four immediate neighbors (up, down, left, and right). Do not consider diagonal neighbors.
3.  **Modify:** If a neighboring pixel's value is not '3', change it to '4' (yellow).
4. **Preserve:** The original pixel that was found having the value '3' should keep it's same '3' value.
5.  **Output:** Produce the modified grid. All other pixels retain their original values.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing the color of pixels adjacent to '3' (green)
    pixels to '4' (yellow), while keeping other pixels unchanged.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify pixels with value '3'
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                # Iterate through neighbors (up, down, left, right)
                neighbors = []
                if r > 0:
                    neighbors.append((r - 1, c))  # Up
                if r < rows - 1:
                    neighbors.append((r + 1, c))  # Down
                if c > 0:
                    neighbors.append((r, c - 1))  # Left
                if c < cols - 1:
                    neighbors.append((r, c + 1))  # Right

                # Modify neighbors to '4' if they are not '3'
                for nr, nc in neighbors:
                    if output_grid[nr, nc] != 3:
                        output_grid[nr, nc] = 4

    return output_grid
```
