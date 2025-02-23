import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a modified checkerboard pattern to the blue and orange rectangles.
    
    Args:
        input_grid (numpy.ndarray): The input grid.
    
    Returns:
        numpy.ndarray: The transformed output grid.
    """
    output_grid = np.copy(input_grid)
    
    # Blue rectangle
    blue_rows, blue_cols = np.where(input_grid == 1)
    if blue_rows.size > 0:  # Check if blue exists
      blue_min_row, blue_max_row = np.min(blue_rows), np.max(blue_rows)
      blue_min_col, blue_max_col = np.min(blue_cols), np.max(blue_cols)

      for i in range(blue_min_row, blue_max_row + 1):
          for j in range(blue_min_col, blue_max_col + 1):
              if (i + j) % 2 != 0:
                  output_grid[i, j] = 0

    # Orange rectangle
    orange_rows, orange_cols = np.where(input_grid == 7)
    if orange_rows.size > 0:  # Check if orange exists
      orange_min_row, orange_max_row = np.min(orange_rows), np.max(orange_rows)
      orange_min_col, orange_max_col = np.min(orange_cols), np.max(orange_cols)

      for i in range(orange_min_row, orange_max_row + 1):
          for j in range(orange_min_col, orange_max_col + 1):
              if (i + j) % 2 != 0 :
                  output_grid[i, j] = 0

    return output_grid