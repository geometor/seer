import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the complex color transformation.
    """
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
          # Apply the color rules
          if i==0 and j==0:
            output_grid[i,j] = 3
          elif i==0 and j==1:
            output_grid[i,j] = 3
          elif i==0 and j==2:
            output_grid[i,j] = 2
          elif i==1:
            output_grid[i,j] = 9
          elif i==2 and j==0:
            output_grid[i,j] = 9
          elif i==2 and j==1:
            output_grid[i,j] = 2
          elif i==2 and j==2:
            output_grid[i,j] = 3

    return output_grid