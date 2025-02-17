import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    non_zero_elements = []

    # Collect non-zero elements with their column indices
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] != 0:
                non_zero_elements.append((j, input_grid[i, j]))  # (column, value)

    # Sort by column index
    non_zero_elements.sort()

    # Fill the output grid from the bottom up
    row = output_grid.shape[0] - 1
    col_index = 0
    for col, value in non_zero_elements:
        while output_grid[row, col] != 0 and row > 0 :
          row -= 1
        output_grid[row, col] = value
          

    return output_grid