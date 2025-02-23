"""
The transformation takes specific object from the input, detects its size, and replaces it by a new object color. The output grid is all zeros (background color) except for two cells with color 2, positioned based on where the ends of a line of color 5 would map onto a 3x3 grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 numpy array filled with zeros.
    output_grid = np.zeros((3, 3), dtype=int)
    
    # Find the positions of color 5 (gray) in the input grid.
    gray_positions = np.argwhere(input_grid == 5)
    
    #If gray color exists
    if len(gray_positions) >0:
        # Get the first and last y-coordinates of the gray object.
        first_gray_y = gray_positions[0][0]
        last_gray_y = gray_positions[-1][0]

        # Map these y-coordinates to the 3x3 output grid.
        output_y1 = int(first_gray_y * (3 / input_grid.shape[0]))
        output_y2 = int(last_gray_y * (3/ input_grid.shape[0]))

        # Determine the corresponding x-coordinates on the 3x3.
        output_x1 = 0
        output_x2 = 2


        # Place the color 2 (red) in the calculated positions.
        output_grid[output_y1, output_x1] = 2
        output_grid[output_y2, output_x2] = 2

    return output_grid