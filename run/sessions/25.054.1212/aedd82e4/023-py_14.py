"""
1.  Identify Red Pixels: Locate all pixels with the color red (value 2).
2.  Check for Left Adjacency to Black: For each red pixel, determine if a black pixel (value 0) is directly to its left.
3.  Change Color to Blue: If a red pixel has a black pixel directly to its left, change the red pixel's color to blue (value 1).
4.  Leave other Pixels Unchanged: All other pixels that do not meet the above rule should not be modified.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms an input grid by changing red pixels to blue if they are directly to the right of a black pixel.
    """
    output_grid = np.copy(input_grid)  # Create a copy to modify
    rows, cols = input_grid.shape

    # Iterate through each pixel of the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is red
            if input_grid[r, c] == 2:
                # Check for left adjacency to black
                if c > 0 and input_grid[r, c - 1] == 0:
                    # Change the red pixel to blue
                    output_grid[r, c] = 1

    return output_grid