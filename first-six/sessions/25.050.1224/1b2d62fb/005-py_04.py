import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of blue pixels in each row.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 1:
                if j in [0, 1, 2]:
                    output_grid[i,0] = 8
                if j == 3:
                    output_grid[i,1] = 8
                if j in [4,5,6]:
                    output_grid[i,2] = 8

    return output_grid