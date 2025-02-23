import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    for i in range(input_grid.shape[0]):
      for j in range(input_grid.shape[1]):
        output_grid[i,j] = (input_grid[i,j] + 4) % 10
    return output_grid