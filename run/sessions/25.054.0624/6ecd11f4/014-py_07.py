"""
1. Locate the 4x4 multi-colored block in the lower right of the input grid.
2. Extract the values from each row from this 4x4 block.
3. Circular Shift Right: For each extracted row, shift the last element of each row and insert to first position.
4. Construct the output grid with these modified rows.
"""

import numpy as np

def find_multicolor_block(grid):
    # Find the bounding box of the non-zero, non-background color region in the bottom right
    rows, cols = grid.shape
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if grid[r, c] != 0:
                # Check for 4x4 block
                if r >= 3 and c >= 3:
                   block = grid[r-3:r+1, c-3:c+1]
                   unique_colors = np.unique(block)
                   if len(unique_colors) > 4: # heuristic for multicolor
                       return r-3,c-3
    return None, None

def circular_shift_right(row):
    # shift last element to the start
    return [row[-1]] + row[:-1]

def transform(input_grid):
    """
    Transforms an input grid by extracting a 4x4 multicolor block,
    circularly shifting elements in the row to the right, and returning smaller grid.
    """
    # Convert to numpy array
    grid = np.array(input_grid)

    # Find the top-left corner of multi colored 4x4 block
    start_row, start_col = find_multicolor_block(grid)
    output_grid = []

    if start_row is not None and start_col is not None:
      # Extract the 4x4 block
      block = grid[start_row:start_row + 4, start_col:start_col + 4]

      #  Circular shift each row and construct output
      for row in block:
          output_grid.append(circular_shift_right(list(row)))
    else:
      output_grid = np.zeros((4,4), dtype=int).tolist()

    return output_grid