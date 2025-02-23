import numpy as np

def transform2(input_grid):

    output_grid = np.copy(input_grid)

    #Diagonal blue
    for i in range(6):
        output_grid[1+i,i] = 1
    #Diagonal red
    output_grid[2,5] = 2
    output_grid[3,6] = 2
    output_grid[4,7] = 2
    output_grid[5,8] = 2
    output_grid[7,9] = 2

    return output_grid
