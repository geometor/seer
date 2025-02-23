"""
The transformation duplicates the input grid and stacks the original on top of its vertical reflection.
"""

import numpy as np

def transform(input_grid):
    # Create a numpy array from the input grid
    input_np = np.array(input_grid)

    # Vertically reflect the input grid
    reflected_np = np.flipud(input_np)

    # Stack the original grid on top of the reflected grid
    output_np = np.vstack((input_np, reflected_np))

    # Convert the numpy array back to a list
    output_grid = output_np.tolist()
    
    return output_grid