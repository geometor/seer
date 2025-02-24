"""
Shift all contiguous non-zero color blocks down, filling the spaces, but keep the bottom row fixed.
"""

import numpy as np

def find_blocks(grid):
    """
    Finds contiguous blocks of non-zero pixels in the grid.
    Returns a list of blocks, where each block is a list of (row, col) coordinates.
    """
    blocks = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_block, color):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_block.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, current_block, color)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                current_block = []
                dfs(r, c, current_block, grid[r, c])
                blocks.append(current_block)
    return blocks

def shift_block_down(grid, block):
    """
    Shifts a single block down as far as possible within the grid.
    Returns the new block coordinates after shifting.
    """
    rows, cols = grid.shape
    max_shift = rows  # Maximum possible downward shift

    # Find the minimum shift allowed by obstacles or grid boundaries
    for r, c in block:
        for shift in range(1, rows - r):
            if r + shift + 1 == rows:
                max_shift = shift + 1
                break
            if grid[r + shift +1,c] != 0 :                
                max_shift = min(max_shift, shift)
                break    
            
        
    # Create new block coordinates after shifting
    new_block = [(r + max_shift, c) for r, c in block]
    return new_block
    

def transform(input_grid):
    """
    Transforms the input grid by shifting non-zero color blocks down.
    """
    grid = np.array(input_grid)  # Convert to NumPy array for easier manipulation
    rows, cols = grid.shape
    output_grid = np.zeros_like(grid)
    
    # 1. keep the bottom row
    output_grid[-1,:] = grid[-1,:]

    # 2. Find blocks in the input grid (excluding the fixed bottom row)
    blocks = find_blocks(grid[:-1,:])

    # 3. Shift each block down and update the output grid
    for block in blocks:
      new_block = shift_block_down(grid, block)
      for r, c in new_block:
          output_grid[r, c] = grid[block[0][0], block[0][1]]  # Use original color

    return output_grid.tolist()