import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            if output_grid[x, y] == 2:
                output_grid[x, y] = 6
            else:
                output_grid[x,y] = max(0, output_grid[x,y]-1)
    return output_grid