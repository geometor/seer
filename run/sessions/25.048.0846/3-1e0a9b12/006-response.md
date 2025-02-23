# 3-1e0a9b12 • 006 • Response

---

*text:*

*text:*
```python
"""
Moves non-white cells to the last row if they are not already in the rows where non-white objects are present,
preserving their original horizontal order, and setting all other cells to white. Objects that are in rows containing
non-white objects should maintain position.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-white objects to the bottom row,
    preserving their horizontal order, or keeping them in existing rows if non-white
    objects are already present.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find non-white cells and their column indices
    non_white_cells = []
    rows_with_non_white = set()

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_white_cells.append((r, c, input_grid[r, c]))
                rows_with_non_white.add(r)


    # copy objects in rows with existing colors
    for r in rows_with_non_white:
        for c in range(cols):
            if input_grid[r,c] != 0:
               output_grid[r,c]= input_grid[r,c]

    # Sort non-white cells by their column index (original horizontal order)
    non_white_cells_to_move = []

    for r, c, color in non_white_cells:
      if  not any(input_grid[r,i]!=0 for i in range(cols)  if r!= rows-1):
          non_white_cells_to_move.append( (c, color) )

    non_white_cells_to_move.sort()


    # Place non-white cells in the last row of the output grid
    current_col = 0
    for _, color in non_white_cells_to_move:
        while(output_grid[rows-1, current_col]!=0):
          current_col = current_col + 1
        output_grid[rows - 1, current_col] = color

    return output_grid.tolist()
```

