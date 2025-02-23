import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    for x in range(input_grid.shape[0]):
        for y in range(input_grid.shape[1]):
            if input_grid[x, y] == 5:
                output_grid[x, y] = (input_grid[x, y] + 6) % 10
            elif input_grid[x, y] == 6:
                output_grid[x, y] = (input_grid[x, y] - 4) % 10
            elif input_grid[x,y] == 2:
                output_grid[x,y] = (input_grid[x,y] + 4) % 10
            else:
                output_grid[x, y] = (input_grid[x, y] + 1) % 10
    return output_grid