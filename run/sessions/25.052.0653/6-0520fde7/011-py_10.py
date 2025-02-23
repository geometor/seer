import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to create a 3x3 output grid with red pixels placed
    based on the presence and position of blue and white pixels relative to a
    gray vertical line.
    """
    output_grid = np.zeros((3, 3), dtype=int)
    rows, cols = input_grid.shape

    # Find the column index of the gray line (assuming only one vertical line exists)
    gray_col = -1
    for c in range(cols):
        if np.any(input_grid[:, c] == 5):
            gray_col = c
            break

    if gray_col == -1:  # No gray line found
        return output_grid #return all white cells

    # Case 1: Only gray line
    if gray_col != -1 and not (np.any(input_grid == 1) or np.any(input_grid==0)):
          output_grid[1, 1] = 2
          return output_grid
          
    # Find the relevant blue pixel's row (if it exists)
    blue_row = -1
    if gray_col > 0:  # Ensure there's a column to the left of the gray line
        for r in range(rows):
            if input_grid[r, gray_col - 1] == 1:
                blue_row = r
                # Case 2: Blue pixel to the left of the gray line and white pixel on the left.
                if gray_col > 1 and input_grid[r,gray_col-2] == 0:
                  output_grid[0, 1] = 2
                  output_grid[1, 2] = 2
                  output_grid[2, 1] = 2
                  return output_grid
                # Case 4.
                else:
                  output_grid[1, 0] = 2
                  output_grid[2, 2] = 2
                  return output_grid
            elif input_grid[r, gray_col - 1] == 0: # Case 3
                output_grid[0, 2] = 2
                output_grid[1, 0] = 2
                output_grid[2, 1] = 2
                return output_grid

    return output_grid