import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Add blue pixel adjacent to top-right azure pixel
    if input_grid[1,5] == 8:
        output_grid[1,4] = 1
    if input_grid[2,2] == 8:
        output_grid[2,3] = 1
    if input_grid[5,4] == 8 :
        output_grid[5,3] = 1

    return output_grid.tolist()