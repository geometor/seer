"""
The transformation rule is a simple color replacement. Each pixel's numerical value in the input grid is replaced with a new value according to the following mapping:

*   Red (2) becomes Magenta (6).
*   Green (3) becomes Yellow (4).
*   Azure (8) becomes Maroon (9).

The spatial arrangement of the pixels remains unchanged; only their values are altered based on this fixed mapping.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by replacing pixel values based on a predefined mapping.
    """
    # Create a mapping dictionary for color replacement
    mapping = {
        2: 6,  # Red to Magenta
        3: 4,  # Green to Yellow
        8: 9   # Azure to Maroon
    }

    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate through the input grid and apply the mapping
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            input_val = input_grid[i, j]
            if input_val in mapping:
                output_grid[i, j] = mapping[input_val]

    return output_grid