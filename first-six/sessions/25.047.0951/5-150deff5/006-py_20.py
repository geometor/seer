import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the bounding box of the object
    coords = np.argwhere(input_grid == 5)
    if coords.size == 0:
        return output_grid.tolist()

    min_row, min_col = coords.min(axis=0)
    max_row, max_col = coords.max(axis=0)
    
    # Vertical bar
    for r in range(min_row, max_row+1):
        if input_grid[r, min_col] == 5:
            output_grid[r, min_col] = 2

    # Top bar
    top_bar_cols = []
    for c in range(min_col, max_col + 1):
        if input_grid[min_row, c] == 5:
            top_bar_cols.append(c)
            
    if len(top_bar_cols) >=2:
      output_grid[min_row, top_bar_cols[-2]:top_bar_cols[-1]+1] = 8
      
      
    # Find and transform middle bars.
    for r in range(min_row + 1, max_row):
        mid_bar_cols = []
        for c in range(min_col, max_col+1):
          if input_grid[r,c] == 5:
            mid_bar_cols.append(c)

        if len(mid_bar_cols) >= 2 :
            output_grid[r, mid_bar_cols[-2]:mid_bar_cols[-1]+1] = 8

    return output_grid.tolist()