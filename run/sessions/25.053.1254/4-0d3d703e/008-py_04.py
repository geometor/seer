"""
The input grid is transformed into the output grid by adding the constant value 3 to each element of the input grid. The result of each addition is then subjected to a modulo 10 operation. This means that if the sum is greater than or equal to 10, 10 is subtracted from it. The spatial arrangement (3x3 grid) of the pixels is preserved.
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