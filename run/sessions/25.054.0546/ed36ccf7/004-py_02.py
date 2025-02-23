"""
The transformation rule involves reflecting the input grid across its main diagonal (top-left to bottom-right).
"""

import numpy as np

def transform(input_grid):
    """
    Reflects the input grid across its main diagonal.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Reflect the array across the main diagonal (transpose).
    output_array = np.transpose(input_array)

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()
    return output_grid