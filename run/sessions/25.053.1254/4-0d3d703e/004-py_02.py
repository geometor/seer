"""
The input grid is transformed into the output grid by adding 3 to each element of the input grid. If the result of the addition is greater than 9, subtract 10 from the sum to get the output color value. The spatial structure (3x3 grid) is preserved. In other words, we are performing modulo 10 addition.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by adding 3 to each element, modulo 10.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)
    
    # Add 3 to each element and take the modulo 10.
    output_array = (input_array + 3) % 10
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()
    
    return output_grid