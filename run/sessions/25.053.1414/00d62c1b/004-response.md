# 00d62c1b • 004 • refine_coder

---
```python
"""
1.  **Find Green Pixels:** Locate all pixels within the input grid that have a color value of '3' (green).
2.  **Iterate:** For *each* green pixel found:
    *   **Check Neighbors:** Examine its four immediate neighbors (up, down, left, and right - not diagonal).
    *   **Conditional Change:** For *each* neighboring pixel:
        *   If the neighboring pixel's *original* color is *not* '3' (green), change its color to '4' (yellow).
3. **Preserve Greens**: The green pixels that initiated the checks should remain green.
4.  **Output:** The final output is the grid with the described modifications. All pixels not directly adjacent to a green pixel should retain their original colors. A neighbor that has been changed to yellow, should not change its neighbors.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the proximity of pixels to green (3) pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    added_yellows = []

    # Find Green Pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                # Check Neighbors (up, down, left, right)
                neighbors = []
                if r > 0:
                    neighbors.append((r - 1, c))  # Up
                if r < rows - 1:
                    neighbors.append((r + 1, c))  # Down
                if c > 0:
                    neighbors.append((r, c - 1))  # Left
                if c < cols - 1:
                    neighbors.append((r, c + 1))  # Right

                # Conditional Change for each neighbor
                for nr, nc in neighbors:
                    if input_grid[nr, nc] != 3 and (nr,nc) not in added_yellows:
                        output_grid[nr, nc] = 4
                        added_yellows.append((nr,nc))

    return output_grid
```

