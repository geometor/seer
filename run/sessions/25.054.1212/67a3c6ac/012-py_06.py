"""
The input grid is transformed into the output grid by reflecting it across the anti-diagonal (from bottom-right to top-left). The colors of the pixels are preserved during the reflection. This can be implemented programmatically by reversing the order of the rows and then reversing the order of elements within each row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by reflecting it across the anti-diagonal (bottom-right to top-left).
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Reverse the order of rows and columns.
    flipped_array = np.flip(input_array)
    
    # Convert the flipped array back to a list of lists.
    output_grid = flipped_array.tolist()

    return output_grid