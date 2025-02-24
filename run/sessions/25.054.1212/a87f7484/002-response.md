# a87f7484 • 002 • example_1 • investigate_coder

---
```python
"""
Examine the input grid and identify all contiguous rectangular blocks of pixels with the same color.
Of the blocks identified, locate any block that has other blocks above it.
Extract the located block.
The extracted block is the output.
"""

import numpy as np

def find_blocks(grid):
    # find 3x3 blocks
    blocks = []
    for i in range(0, len(grid) - 2):
        for j in range(0, len(grid[0]) - 2):
          color = grid[i][j]
          if (grid[i+1][j] == color and grid[i+2][j] == color and
              grid[i][j+1] == color and grid[i][j+2] == color and
              grid[i+1][j+1] == color and grid[i+1][j+2] == color and
              grid[i+2][j+1] == color and grid[i+2][j+2] == color):
            blocks.append(((i, j), color))
    return blocks

def find_bottom_block(blocks):
    # find the block that at lowest position
    bottom_block = None
    max_row = -1
    for (row, col), color in blocks:
        if row > max_row:
            max_row = row
            bottom_block = ((row, col), color)
    return bottom_block
    

def transform(input_grid):
    # Convert input grid to numpy array
    grid = np.array(input_grid)

    # Find all 3x3 blocks
    blocks = find_blocks(grid)
    
    # Find the bottom block
    bottom_block_coords, _ = find_bottom_block(blocks)

    # Extract bottom block
    row, col = bottom_block_coords
    output_grid = grid[row:row+3, col:col+3]
    
    return output_grid.tolist()
```
