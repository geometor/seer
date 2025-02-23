"""
1. Locate 4x4 Block: Find the 4x4 block of pixels in the lower-right region of the input grid. This block contains all or most of the non-background (non-zero) colors present in the entire input grid.
2. Extract Rows: Extract each row of the 4x4 block as a separate list.
3. Drop Row: If the first and second rows of the input 4x4 block contain all the same values, and those are the background color, drop the first row.
4. Circular Shift Right: For each extracted row (after potentially dropping one), perform a circular shift to the right.  This means moving the last element of the row to the beginning.
5. Construct Output Grid: Create the output grid by combining the shifted rows.
"""

import numpy as np

def find_4x4_block(grid):
    # Find the 4x4 block in the bottom-right containing all/most non-zero colors.
    rows, cols = grid.shape
    all_colors = set(np.unique(grid)) - {0}  # Exclude background color
    for r in range(rows - 4, -1, -1):
        for c in range(cols - 4, -1, -1):
            block = grid[r:r+4, c:c+4]
            block_colors = set(np.unique(block))
            if all_colors.issubset(block_colors):  # Check if block contains all non-zero
                return r, c
    return None, None # no block found

def circular_shift_right(row):
    # shift last element to the start
    return [row[-1]] + row[:-1]

def drop_row_if_needed(rows):
  if len(rows) > 1:
    first_row_values = set(rows[0])
    second_row_values = set(rows[1])
    if len(first_row_values) == 1 and list(first_row_values)[0] == 0:
       if len(second_row_values) == 1 and list(second_row_values)[0] == 0:
        return rows[1:]

  return rows


def transform(input_grid):
    # Convert to numpy array
    grid = np.array(input_grid)

    # 1. Locate 4x4 Block
    start_row, start_col = find_4x4_block(grid)
    output_grid = []

    if start_row is not None and start_col is not None:
      # 2. Extract Rows
      block = grid[start_row:start_row + 4, start_col:start_col + 4]
      rows = [list(row) for row in block]

      # 3. Drop Row (if needed)
      rows = drop_row_if_needed(rows)

      # 4. Circular Shift Right
      shifted_rows = [circular_shift_right(row) for row in rows]

      # 5. Construct Output Grid
      output_grid = shifted_rows
    else:
      output_grid = np.zeros((4,4), dtype=int).tolist() # return zero array if no block found

    return output_grid