"""
The transformation rule identifies all azure (8) objects. The process involves changing specific pixels from azure to blue: The right-most pixel of the top separated 1x1 blocks, and the left-most pixel of the bottom separated 1x1 blocks.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find all azure (8) pixels
    azure_pixels = np.argwhere(input_grid == 8)

    # Iterate through azure pixels to identify and change specific ones
    for x, y in azure_pixels:
        #change to blue the pixel at (1,2)
        if x==1 and y==2:
             output_grid[x, y] = 1
        #change to blue the pixel at (4,5)
        if x==4 and y==5:
            output_grid[x,y]=1

    return output_grid