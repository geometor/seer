# 6430c8c4 • 018 • refine_coder

---
```python
"""
The input grid is scanned for 2x2 blocks of identical, non-white pixels.  For each such block found, a green (3) pixel is placed in the 4x4 output grid. The location of that pixel is determined by the top-left coordinate of the 2x2 block in the input. The mapping rule is: Input(r, c) -> Output(r // 2, c // 2).
"""

import numpy as np

def find_2x2_blocks(grid):
    """
    Finds all 2x2 blocks of the same non-white color in the grid.
    Returns a list of (row, col) tuples representing the top-left corner of each block.
    """
    blocks = []
    rows, cols = len(grid), len(grid[0])
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r][c] != 0 and \
               grid[r][c] == grid[r+1][c] == grid[r][c+1] == grid[r+1][c+1]:
                blocks.append((r, c))
    return blocks

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((4, 4), dtype=int)

    # Find all 2x2 blocks
    blocks = find_2x2_blocks(input_grid)

    # Map each block to the output grid
    for r, c in blocks:
        output_row = r // 2
        output_col = c // 2
        if(output_row < 4 and output_col < 4):
            output_grid[output_row, output_col] = 3

    return output_grid.tolist()
```
