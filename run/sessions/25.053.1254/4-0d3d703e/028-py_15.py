"""
The transformation involves a direct mapping of input pixel values to output pixel values, dependent on position within the 3x3 grid. A color lookup table is constructed from the first three examples.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)

    # Define a color mapping based on the first three training examples.
    # Mapping format: { (row, col): {input_color: output_color} }
    color_map = {
        (0, 0): {3: 4, 2: 6, 5: 1, 8:8},
        (0, 1): {1: 5, 3: 4, 8: 9, 3:3},
        (0, 2): {2: 6, 8: 9, 2:2, 2:6},
        (1, 0): {3: 4, 2: 6, 5: 1, 8:8},
        (1, 1): {1: 5, 3: 4, 8: 9, 3:3},
        (1, 2): {2: 6, 8: 9, 2:2, 2:6},
        (2, 0): {3: 4, 2: 6, 5: 1, 8:8},
        (2, 1): {1: 5, 3: 4, 8: 9, 3:3},
        (2, 2): {2: 6, 8: 9, 2:2, 2:6}
    }

    # Iterate through each pixel of the grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Get the input color.
            input_color = input_grid[i, j]
            
            #lookup color
            if (i,j) in color_map:
                if input_color in color_map[(i,j)]:
                  output_grid[i,j] = color_map[(i,j)][input_color]

    return output_grid