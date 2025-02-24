"""
The output grid is created from the input grid by performing a reflection across the main diagonal (top-left to bottom-right). This is equivalent to transposing the grid. The colors of the pixels are preserved during the transposition.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by reflecting it across the main diagonal (transposing it).
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)

    # Transpose the array.  This swaps rows and columns.
    output_array = input_array.T

    # Convert the transposed array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid