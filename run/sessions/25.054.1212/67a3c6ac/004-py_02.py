"""
The transformation involves transposing the input grid. The columns of the input become the rows of the output, and vice versa.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Transpose the array
    output_array = input_array.T

    # Convert the transposed array back to a list of lists
    output_grid = output_array.tolist()

    return output_grid