# a8d7556c • 018 • refine_coder

---
```python
"""
1. Identify all white (0) pixels.
2. For each white pixel, check for orthogonal adjacency (up, down, left, right) to a gray (5) pixel.
3. If a white pixel is orthogonally adjacent to a gray pixel, change its color to red (2).
4. All other pixels remain unchanged.
"""

import numpy as np

def is_adjacent_to_gray(grid, r, c):
    """
    Checks if a pixel at (r, c) is orthogonally adjacent to a gray (5) pixel.
    """
    rows, cols = grid.shape
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 5:
            return True
    return False

def transform(input_grid):
    """
    Transforms the input grid by changing white pixels to red if they are adjacent to gray pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is white
            if output_grid[r, c] == 0:
                # Check for adjacency to gray
                if is_adjacent_to_gray(output_grid, r, c):
                    # Change white pixel to red
                    output_grid[r, c] = 2

    return output_grid
```

