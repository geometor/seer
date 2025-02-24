"""
Transforms a single-row grid into a multi-row grid where a non-zero pixel is replicated diagonally downwards and to the right.
"""

import numpy as np

def transform(input_grid):
    # Find the non-zero pixel and its color
    non_zero_pixels = np.nonzero(input_grid)[1]  # Get column indices of non-zero elements
    first_non_zero_color = input_grid[0, non_zero_pixels[0]] if non_zero_pixels.size > 0 else 0
        
    red_pixels_count = np.count_nonzero(input_grid == first_non_zero_color)


    # Initialize output grid
    output_rows = red_pixels_count
    output_cols = input_grid.shape[1]
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Replicate the non-zero pixel diagonally
    if non_zero_pixels.size > 0 :
        for i in range(output_rows):
            output_grid[i, :i+1] = first_non_zero_color
        

    return output_grid