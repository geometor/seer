"""
The input grid is rotated 90 degrees counter-clockwise. The numbers change positions as if the entire grid was a single object being physically rotated by that angle.
"""

import numpy as np

def transform(input_grid):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)
    
    # Rotate the grid 90 degrees counter-clockwise.
    output_np = np.rot90(input_np)
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid