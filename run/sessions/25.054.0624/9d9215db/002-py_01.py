"""
The input grid's non-white pixels are replicated in a checkered pattern.
Blue(1) pixels are replicated horizontally and vertically in alternating positions,
Red(2) and Azure(8) pixels remain in place relative to the original blue pixels.
"""

import numpy as np

def get_non_white_pixels(grid):
    """
    Finds the coordinates of non-white pixels in the input grid.
    """
    non_white_pixels = []
    for r_idx, row in enumerate(grid):
        for c_idx, val in enumerate(row):
            if val != 0:
                non_white_pixels.append( ((r_idx, c_idx), val))
    return non_white_pixels

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Find non white pixels and their locations
    non_white_pixels = get_non_white_pixels(input_grid)

    # Replicate according to the pattern
    for (r,c), val in non_white_pixels:
        if val == 1:
          for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
              if (i + j) % 2 == (r + c) % 2:
                output_grid[i, j] = 1
        elif val == 2 or val == 8:
            output_grid[r,c] = val


    return output_grid.tolist()