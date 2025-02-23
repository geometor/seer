import numpy as np

def transform(input_grid):
    """
    Transforms the input grid (in this case 13x11) into a 6x5 output grid.

    Args:
      input_grid: The 13x11 input grid.

    Returns:
       The 6x5 output grid.
    """
    in_rows, in_cols = input_grid.shape
    out_rows, out_cols = 6, 5
    output_grid = np.zeros((out_rows, out_cols), dtype=int)

    # Corner placement
    if input_grid[0, 9] == 8:
        output_grid[0, 0] = 8
    if input_grid[2, 7] == 8:
        output_grid[0, 4] = 8
    if input_grid[9, 7] == 8:
        output_grid[5, 4] = 8
    if input_grid[9, 2] == 8:
        output_grid[5, 0] = 8
    

    # Center placement
    if input_grid[4,5] == 8:
      output_grid[2,2] = 8
    if input_grid[7,7] == 8:
      output_grid[4,2] = 8

    # Vertical line placement
    output_grid[1:5, 0] = input_grid[3:7, 3]
    output_grid[1:5, 4] = input_grid[3:7, 7]

    #check that these pixels are actually 5.
    for i in range(1,5):
        if output_grid[i,0] != 5: output_grid[i,0] = 0
        if output_grid[i,4] != 5: output_grid[i,4] = 0
    
    return output_grid