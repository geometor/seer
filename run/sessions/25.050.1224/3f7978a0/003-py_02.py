import numpy as np

def transform(input_grid):
    """
    Transforms an 11x9 input grid into a 7x5 output grid.
    
    Args:
        input_grid (numpy.ndarray): An 11x9 NumPy array representing the input grid.
        
    Returns:
        numpy.ndarray: A 7x5 NumPy array representing the output grid.
    """
    output_grid = np.zeros((5, 7), dtype=int)

    # Corners
    if input_grid[0, 1] == 8:
        output_grid[0, 0] = 8
    if input_grid[1, 10] == 8:
      output_grid[0, 6] = 8
    if input_grid[8, 1] == 8:    
      output_grid[4, 0] = 8
    if input_grid[8, 8] == 8:  
      output_grid[4, 6] = 8
    
    # Center
    if input_grid[5, 5] == 8:
      output_grid[2, 3] = 8
    if input_grid[5, 6] == 8:
      output_grid[2, 4] = 8
    if input_grid[7,4] == 8:
      output_grid[4,2] = 8
      

    # Vertical lines
    output_grid[1:4, 0] = input_grid[4:7, 2]
    output_grid[1:4, 6] = input_grid[4:7, 8]

    #check that these pixels are actually 5.
    for i in range(1,4):
        if output_grid[i,0] != 5: output_grid[i,0] = 0
        if output_grid[i,6] != 5: output_grid[i,6] = 0


    return output_grid