# 00d62c1b • 006 • refine_coder

---
```python
"""
1.  **Copy Input:** Create a copy of the input grid. This copy will serve as the reference for the original state.
2.  **Find Green Pixels:** In the *original* grid (the copy), locate all pixels with a color value of '3' (green).
3.  **Iterate:** For *each* green pixel found in the original grid:
    *   **Check Neighbors:** Examine its four immediate neighbors (up, down, left, right - not diagonal) *in the original grid*.
    *   **Conditional Change:** For *each* neighboring pixel in the original input grid:
        *   If the neighboring pixel's color *in the original grid* is *not* '3' (green), change the corresponding pixel's color in the *output* grid to '4' (yellow).
4.  **Preserve Greens:** The green pixels that initiated the checks should remain green in the output grid.
5.  **Output:** The final output is the modified grid, where only non-green pixels directly adjacent to green pixels in the *original* input grid have been changed to yellow. All other pixels should retain their original colors from the input.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the proximity of pixels to green (3) pixels,
    using the original grid as the reference for neighbor checks.
    """
    original_grid = np.copy(input_grid)  # Create a copy for reference
    output_grid = np.copy(input_grid)
    rows, cols = original_grid.shape

    # Find Green Pixels in the original grid
    for r in range(rows):
        for c in range(cols):
            if original_grid[r, c] == 3:
                # Check Neighbors (up, down, left, right) in the original grid
                neighbors = []
                if r > 0:
                    neighbors.append((r - 1, c))  # Up
                if r < rows - 1:
                    neighbors.append((r + 1, c))  # Down
                if c > 0:
                    neighbors.append((r, c - 1))  # Left
                if c < cols - 1:
                    neighbors.append((r, c + 1))  # Right

                # Conditional Change for each neighbor in the original grid
                for nr, nc in neighbors:
                    if original_grid[nr, nc] != 3:
                        output_grid[nr, nc] = 4  # Change in the output grid

    return output_grid
```

