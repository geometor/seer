"""
The input grid is reflected vertically (flipped along the horizontal axis).  This means the top row of the input becomes the bottom row of the output, the second row from the top becomes the second row from the bottom, and so on. The colors and number of pixels of each color in the input grid are identical to the output grid.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)
    
    # Reverse the order of rows to achieve vertical reflection.
    output_array = input_array[::-1]
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()
    
    return output_grid