import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero single-cell objects to the last row,
    maintaining their relative horizontal order.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [row[:] for row in input_grid]  # Corrected copying
    last_row = [0] * cols

    # Occupy spaces in last row by multi-cell objects
    for c in range(cols):
      if input_grid[rows-1][c] != 0:
        is_single=True
        for i in range(-1,2):
          for j in range(-1,2):
            if 0 <= rows-1+i < rows and 0 <= c+j < cols:
              if (i!=0 or j!=0) and input_grid[rows-1+i][c+j] == input_grid[rows-1][c]:
                is_single = False
                break
          if not is_single:
            break
        if not is_single:
          last_row[c] = input_grid[rows-1][c]


    # Find and move single-cell non-zero objects
    for c in range(cols):
        for r in range(rows):
            if input_grid[r][c] != 0:
                # Check if it's a single-cell object
                is_single = True
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= r + i < rows and 0 <= c + j < cols:
                            if (i != 0 or j != 0) and input_grid[r + i][c + j] == input_grid[r][c]:
                                is_single = False
                                break
                    if not is_single:
                        break

                # If it's a single-cell object, move it
                if is_single:
                    if last_row[c] == 0:
                      last_row[c] = input_grid[r][c]
                      if r != rows -1:
                        output_grid[r][c] = 0  # Clear original position

    # Replace the last row of the output grid
    output_grid[rows - 1] = last_row

    return output_grid