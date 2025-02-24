"""
Transform the input grid by selectively replacing '5' (gray) pixels with '3' (green) pixels based on their position within each row and relative to other '5' pixels. '0' (white) pixels remain unchanged. The transformation rule depends on the total number of gray pixels in each row and their indices.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each row.
    for i in range(rows):
        # Locate all gray pixels (value 5) in the current row.
        fives = np.where(output_grid[i] == 5)[0]
        num_fives = len(fives)

        # Apply transformation rules based on the number of gray pixels.
        if num_fives > 0:
            if num_fives == 1:
                # output_grid[i, fives[0]] = 3 #no change
                pass
            elif num_fives == 2:
                output_grid[i, fives[0]] = 3  # Change the first
            elif num_fives == 3:
                output_grid[i, fives[1]] = 3  # Change the second
            elif num_fives == 4:
                output_grid[i, fives[1]] = 3   # Change the 2,3,4
                output_grid[i, fives[2]] = 3
                output_grid[i, fives[3]] = 3
            elif num_fives == 5:
                output_grid[i, fives[0]] = 3 # change 1,2,3,5
                output_grid[i, fives[1]] = 3
                output_grid[i, fives[2]] = 3
                output_grid[i, fives[4]] = 3
            elif num_fives == 6:             # change 2,3,4,5
                output_grid[i, fives[1]] = 3
                output_grid[i, fives[2]] = 3
                output_grid[i, fives[3]] = 3
                output_grid[i, fives[4]] = 3


    return output_grid