"""
The input grid is transformed into the output grid by adding 3 to each element of the input grid. The spatial structure (3x3 grid) is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by adding 3 to each element.
    """
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)
    
    # Add 3 to each element of the array.
    output_array = input_array + 3
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()
    
    return output_grid