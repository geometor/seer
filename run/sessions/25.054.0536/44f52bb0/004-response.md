# 44f52bb0 • 004 • refine_coder

---
```python
"""
Examines the input grid for red pixels, determines their connectedness, and outputs a 1x1 grid with either a blue (1) or orange (7) pixel based on whether the red pixels form a single connected group.
"""

import numpy as np

def is_fully_connected(grid, red_pixels):
    """
    Checks if a set of red pixels in a grid are fully connected.
    """
    if not red_pixels:
        return True  # No red pixels, vacuously true

    visited = set()
    queue = [red_pixels[0]]
    visited.add(red_pixels[0])

    while queue:
        r, c = queue.pop(0)
        # Check neighbors (up, down, left, right)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in red_pixels and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))

    return len(visited) == len(red_pixels)

def transform(input_grid):
    # Find coordinates of all red pixels
    red_pixels = []
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 2:
                red_pixels.append((r, c))

    # Determine connectedness
    fully_connected = is_fully_connected(input_grid, red_pixels)

    # Create a 1x1 output grid
    output_grid = np.zeros((1, 1), dtype=int)

    # Set output based on connectedness
    if fully_connected:
        output_grid[0, 0] = 1  # Blue
    else:
        output_grid[0, 0] = 7  # Orange

    return output_grid
```
