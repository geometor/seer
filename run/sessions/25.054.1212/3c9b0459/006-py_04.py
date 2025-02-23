"""
The input grid is transformed into the output grid by transposing it. Transposing swaps rows and columns. The element at row `i`, column `j` in the input grid becomes the element at row `j`, column `i` in the output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Transpose the array using NumPy's .T attribute.
    output_array = input_array.T

    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()

    return output_grid