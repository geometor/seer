# 1a07d186 • 010 • refine_coder

---
```python
"""
1.  **Identify Horizontal Lines:** Find all horizontal lines, defined as contiguous sequences of two or more pixels of the same color.
2.  **Identify Singletons:** Find all single-pixel objects (singletons), defined as pixels that are not horizontally or vertically adjacent to a pixel of the same color.
3.  **Process by Color:**
    * If there are any singletons, these should be deleted.
"""

import numpy as np

def find_horizontal_lines(grid):
    lines = {}
    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            if pixel != 0:
                if x == 0 or grid[y, x-1] != pixel:
                    # Start of a potential line
                    line_length = 0
                    for x2 in range(x, grid.shape[1]):
                        if grid[y, x2] == pixel:
                            line_length += 1
                        else:
                            break
                    if line_length > 1: # Consider it a line only if longer than 1 pixel
                        if pixel not in lines:
                            lines[pixel] = []
                        lines[pixel].append((y, x, line_length))
    return lines

def find_singletons(grid):
    singletons = []
    for y, row in enumerate(grid):
        for x, pixel in enumerate(row):
            if pixel != 0:
                # Check if it's a singleton
                is_singleton = True
                if x > 0 and grid[y, x-1] == pixel:
                    is_singleton = False
                if x < grid.shape[1] - 1 and grid[y, x+1] == pixel:
                    is_singleton = False
                if y > 0 and grid[y-1, x] == pixel:
                    is_singleton = False
                if y < grid.shape[0] - 1 and grid[y+1, x] == pixel:
                    is_singleton = False
                if is_singleton:
                    singletons.append((y, x, pixel))
    return singletons

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find horizontal lines
    lines = find_horizontal_lines(input_grid)

    # Find singletons and remove from output_grid
    singletons = find_singletons(input_grid)
    for y,x, color in singletons:
        output_grid[y,x] = 0

    return output_grid
```
