"""
The output grid is always 1x5. The number of blue pixels in the output is determined by the number of blue pixels in the input:

1. Calculate the number of blue pixels in the input grid.
2. If the number of blue pixels is less than or equal to 3, output is = input // 2
3. If the number of blue pixels is greater than 3, output grid has 4 blue pixels.
4. Fill the remaining cells in the 1x5 output grid with white pixels (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 1x5 array filled with zeros (white)
    output_grid = np.zeros((1, 5), dtype=int)

    # Count blue pixels (value 1) in the input grid
    blue_count = np.count_nonzero(input_grid == 1)

    # Determine the number of blue pixels in the output
    if blue_count <= 3:
        output_blue_count = blue_count // 2
    else:
        output_blue_count = 4

    # Fill the output grid with the determined number of blue pixels
    output_grid[0, :output_blue_count] = 1

    return output_grid