"""
Transforms the input grid by extracting a specific sub-region based on identified patterns:
1. Alternating colors: If colors alternate in both rows and columns, extract the top-left pixel.
2. Repeating 2x1 Horizontal Blocks: If the first two rows show horizontally repeating 2x1 blocks, extract the central 2x1 block.
3. Default 2x2: Otherwise, extract the central 2x2 block.
"""

import numpy as np

def is_alternating(input_grid):
    """Checks if the grid has alternating colors in both rows and columns."""
    grid = np.array(input_grid)
    rows, cols = grid.shape

    for r in range(rows):
        for c in range(cols):
            if r + 1 < rows and grid[r, c] == grid[r + 1, c]:
                return False
            if c + 1 < cols and grid[r, c] == grid[r, c + 1]:
                return False
    return True

def has_repeating_2x1_horizontal(input_grid):
    """Checks for repeating 2x1 horizontal blocks in the first two rows."""
    grid = np.array(input_grid)
    rows, cols = grid.shape

    if rows < 2 or cols < 2:  # Need at least 2x2 for a 2x1 block.
        return False

    first_block = grid[0, 0:2]
    if first_block[0] == first_block[1]:
      return False

    for r in range(0, rows, 2): # step by 2 because pattern repeats every two rows
      for c in range(0, cols -1, 2):
        if r+1 >= rows:
          continue
        current_block = grid[r, c:min(c+2, cols)]  # Handle edge case near boundary
        if len(current_block) < 2:
          continue
        if not np.array_equal(current_block, first_block):
          return False
        if r + 1 < rows:
          if not np.array_equal(grid[r + 1, c: min(c+2,cols)], grid[1,0:2]): # check against second row
            return False

    return True

def get_central_2x1(input_grid):
    """Extracts the central 2x1 block."""
    grid = np.array(input_grid)
    rows, cols = grid.shape
    start_row = (rows - 2) // 2
    start_col = (cols - 1) // 2
    return grid[start_row:start_row + 2, start_col:start_col + 1].tolist()

def get_central_2x2(input_grid):
    """Extracts the central 2x2 block."""
    grid = np.array(input_grid)
    rows, cols = grid.shape
    start_row = (rows - 2) // 2
    start_col = (cols - 2) // 2
    return grid[start_row:start_row + 2, start_col:start_col + 2].tolist()

def transform(input_grid):
    """Transforms the input grid based on identified patterns."""

    # Check for alternating colors.
    if is_alternating(input_grid):
        return [[input_grid[0][0]]]

    # Check for repeating 2x1 horizontal blocks.
    if has_repeating_2x1_horizontal(input_grid):
        return get_central_2x1(input_grid)

    # Default to 2x2 central block.
    return get_central_2x2(input_grid)