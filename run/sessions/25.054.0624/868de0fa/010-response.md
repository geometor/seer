# 868de0fa • 010 • refine_coder

---
```python
"""
1.  **Identify Blue Blocks:** Examine the input grid. Identify all contiguous blocks of blue (1) pixels. A contiguous block consists of one or more blue pixels connected horizontally, vertically, or diagonally.
2.  **Categorize Blocks:** Determine if each blue block is a "top-row block." A block is a "top-row block" if *any* of its pixels are located in row 0 or row 1 of the grid.
3.  **Transform Top-Row Blocks:**
    *   If the top-row block starts at row 1, column 1 and the second element is 1, set the color of (1,1) to orange (7). Check the next two down and one to the right, and two to the right. Set these to orange as well if they exist.
    *  Scan the top two rows. For every blue pixel that is part of a top-row block, trace to see if other blue pixels are connected, within the top two rows, by skipping a cell. Replace all skipped cells with orange (7).
    *   If a contiguous block of blue pixels with 3 or more pixels *only* exists in the top two rows, and is not transformed to orange by skipping, do not transform it.
4.  **Transform Other Blocks:** For blue blocks that are *not* top-row blocks:
    *   If a block has 3 or more pixels, change all pixels in that block to red (2).
5.  **Preserve White Pixels:** White (0) pixels always remain unchanged.
"""

import numpy as np

def find_contiguous_blocks(grid, color):
    visited = set()
    blocks = []

    def dfs(row, col, current_block):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_block.append((row, col))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_block)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_block = []
                dfs(row, col, current_block)
                blocks.append(current_block)
    return blocks

def is_top_row_block(block):
    for row, _ in block:
        if row in (0, 1):
            return True
    return False

def transform_top_row_blocks(grid, blocks):
    output_grid = grid.copy()

    # Handle (1,1) special case
    if grid[1, 1] == 1 and grid[1,2] == 1:
        output_grid[1, 1] = 7
        if grid.shape[0] > 3 and grid[3,2] == 1:
          output_grid[3,2] = 7
        if grid.shape[1] > 3 and grid[1,3] ==1:
            output_grid[1,3] = 7

    for r in range(2):
        for c in range(grid.shape[1]):
            if grid[r,c] == 1:
              #skip transform
                if r==0 and c+2 < grid.shape[1] and grid[r, c+2] == 1:
                    output_grid[r,c+1] = 7
                if r==1 and c+2 < grid.shape[1] and grid[r, c+2] == 1:
                    output_grid[r,c+1] = 7
                if c-2 >= 0 and grid[r, c-2] == 1:
                    output_grid[r,c-1] = 7

    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()

    # Find all blue blocks
    blue_blocks = find_contiguous_blocks(input_grid, 1)

    # Categorize blocks
    top_row_blocks = [block for block in blue_blocks if is_top_row_block(block)]
    other_blocks = [block for block in blue_blocks if not is_top_row_block(block)]

    # Transform top-row blocks
    output_grid = transform_top_row_blocks(output_grid, top_row_blocks)
    
    # Transform other blocks
    for block in other_blocks:
        if len(block) >= 3:
            for row, col in block:
                output_grid[row, col] = 2

    return output_grid
```
