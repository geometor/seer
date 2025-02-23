"""
The transformation creates a vertically reflected copy of the input grid and stacks it on top of the original input grid.
"""

import numpy as np

def transform(input_grid):
    # Create a numpy array from the input grid
    input_np = np.array(input_grid)

    # Vertically reflect the input grid
    reflected_np = np.flipud(input_np)

    # Stack the reflected grid on top of the original grid
    output_np = np.vstack((reflected_np, input_np))

    # Convert the numpy array back to a list
    output_grid = output_np.tolist()
    
    return output_grid