# 00d62c1b • 004 • refine_coder

---
```python
"""
1.  **Identify** contiguous blocks of green (3) pixels.  A contiguous block is defined as a set of green pixels where each pixel is directly adjacent (up, down, left, or right) to at least one other pixel in the block.
2. **Identify** the exterior and interior of the block
    - Exterior green pixels are part of the block, but have fewer than four green neighbors.
    - Interior green pixels are not exterior.
3.  **Change** interior pixels to yellow (4).
4. All other pixels are **unchanged**.
"""

import numpy as np

def get_contiguous_blocks(grid, color):
    """Finds contiguous blocks of a given color in the grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    blocks = []

    def dfs(r, c, current_block):
        """Depth-first search to find contiguous pixels."""
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_block.append((r, c))
        dfs(r + 1, c, current_block)
        dfs(r - 1, c, current_block)
        dfs(r, c + 1, current_block)
        dfs(r, c - 1, current_block)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_block = []
                dfs(r, c, current_block)
                blocks.append(current_block)
    return blocks

def count_neighbors(grid, r, c, target_color):
    """Counts the number of neighbors with the target color around a pixel."""
    rows, cols = grid.shape
    count = 0
    # Check above
    if r > 0 and grid[r-1, c] == target_color:
        count += 1
    # Check below
    if r < rows - 1 and grid[r+1, c] == target_color:
        count += 1
    # Check left
    if c > 0 and grid[r, c-1] == target_color:
        count += 1
    # Check right
    if c < cols - 1 and grid[r, c+1] == target_color:
        count += 1
    return count

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify contiguous blocks of green pixels.
    green_blocks = get_contiguous_blocks(input_grid, 3)

    # 2. & 3. Iterate through blocks and change interior pixels to yellow.
    for block in green_blocks:
        for r, c in block:
            # Check if the current pixel is an interior pixel
            if count_neighbors(input_grid, r, c, 3) == 4:
                output_grid[r,c] = 4

    return output_grid
```
