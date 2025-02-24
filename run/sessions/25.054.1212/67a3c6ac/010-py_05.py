"""
The input grid is transformed into the output grid by reflecting it across the anti-diagonal (top-right to bottom-left). The colors of the pixels are preserved during this reflection.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by reflecting it across the anti-diagonal (top-right to bottom-left).
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Flip the array both horizontally and vertically to achieve anti-diagonal reflection.
    flipped_array = np.fliplr(np.flipud(input_array))

    # Convert the flipped array back to a list of lists.
    output_grid = flipped_array.tolist()

    return output_grid