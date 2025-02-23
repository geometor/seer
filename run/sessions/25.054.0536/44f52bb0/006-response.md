# 44f52bb0 • 006 • refine_coder

---
```python
"""
Identifies groups of connected red pixels in the input grid and outputs a 1x1 grid with either a blue (1) or orange (7) pixel, based on the number of distinct groups.
"""

import numpy as np

def get_red_pixel_groups(grid):
    """
    find the groups of connected red pixels
    """
    red_pixels = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] == 2:
                red_pixels.append((r,c))

    groups = []
    ungrouped = red_pixels[:]

    while ungrouped:
        group = set()
        to_process = [ungrouped.pop(0)]
        group.add(to_process[0])
        while to_process:
            r, c = to_process.pop()
            # Check neighbors (up, down, left, right)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in ungrouped:
                    ungrouped.remove((nr,nc))
                    to_process.append((nr,nc))
                    group.add((nr,nc))
        groups.append(group)
    return groups

def transform(input_grid):
    # Find groups of connected red pixels
    groups = get_red_pixel_groups(input_grid)

    # Create a 1x1 output grid
    output_grid = np.zeros((1, 1), dtype=int)

    # Set output based on the number of groups
    if len(groups) > 1:
        output_grid[0, 0] = 7  # Orange
    else:
        output_grid[0, 0] = 1  # Blue

    return output_grid
```
