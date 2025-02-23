"""
The transformation rule is as follows:
The central red object exchanges its position type with the gray objects, becoming the corners.
The gray object moves to the center cross.
The background (color 0) remains unchanged.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions and background color
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Define corner and cross positions
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    cross = [(0, 1), (1, 0), (1, 2), (2, 1)]

    # Fill output grid based on input positions
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r,c] == 2:
                for corner in corners:
                  output_grid[corner] = 2
            if input_grid[r,c] == 5:
                for cr in cross:
                  output_grid[cr]=5
    return output_grid