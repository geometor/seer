# 00d62c1b • 012 • refine_coder

---
```python
"""
1.  **Identify the Shape:** Locate all contiguous blocks of green (3) pixels within the input grid. Consider this the green shape.
2.  **Identify perimeter:** find the set of pixels that are on the perimeter of the shape
3. **Modify Interior Pixels:** Iterate through all green pixels, if they are not in the shape perimeter, change the pixel to yellow.
4.  **Preserve Remainder:** The output grid is the same size as the input grid. Copy the data from the input grid, modifying the green to yellow as identified.
"""

import numpy as np

def find_contiguous_blocks(grid, color):
    """
    Finds contiguous blocks of a specified color in a grid.
    Returns a list of sets, where each set contains the coordinates of a contiguous block.
    """
    visited = set()
    blocks = []

    def dfs(r, c, current_block):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_block.add((r, c))
        dfs(r + 1, c, current_block)
        dfs(r - 1, c, current_block)
        dfs(r, c + 1, current_block)
        dfs(r, c - 1, current_block)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if (r, c) not in visited and grid[r, c] == color:
                current_block = set()
                dfs(r, c, current_block)
                blocks.append(current_block)
    return blocks

def find_perimeter(block, rows, cols):
    """
    Finds the perimeter pixels of a contiguous block.
    """
    perimeter = set()
    for r, c in block:
        # Check if it's on the edge of the grid
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            perimeter.add((r, c))
            continue

        # Check neighbors for a different color or out of bounds
        is_perimeter = False
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if (nr, nc) not in block:
                    is_perimeter = True
                    break
            if is_perimeter:
                break
        if is_perimeter:
            perimeter.add((r, c))
    return perimeter

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify the Shape (all green blocks)
    green_blocks = find_contiguous_blocks(input_grid, 3)

    # Combine all blocks into one shape
    green_shape = set()
    for block in green_blocks:
      green_shape.update(block)

    # Find the perimeter of combined shape
    perimeter = find_perimeter(green_shape, rows, cols)

    # Modify Interior Pixels
    for r, c in green_shape:
        if (r,c) not in perimeter:
            output_grid[r, c] = 4

    return output_grid
```
