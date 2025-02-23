"""
The transformation rule is a 90-degree *counter-clockwise* rotation of the input grid. Each pixel retains its original color, but its position is changed according to the counter-clockwise rotation.
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid 90 degrees counter-clockwise.
    """
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)

    # Rotate the array 90 degrees counter-clockwise. k=1 for counter-clockwise.
    output_np = np.rot90(input_np, k=1)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid