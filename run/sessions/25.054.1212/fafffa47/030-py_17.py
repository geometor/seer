"""
1.  **Create Output Grid:** Create an output grid that is 3x3, filled with white (0).
2.  **Identify Output Reds:** Examine the *expected output* grid. Note the positions of all red (2) pixels.
3.  **Find Corresponding Input Positions:** For each red pixel position in the output, identify the *corresponding* position in the *input* grid.
4.  **Check Input Color:** If the pixel at that corresponding position in the *input* grid is maroon (9), then set the pixel in the *output* grid at that same position to red (2).
5. **All Other Output:** All other cells in the output grid should remain the default, white.
"""

import numpy as np

def transform(input_grid):
    # Create an output grid that is 3x3, filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through all possible positions in the output grid (3x3).
    for row in range(3):
        for col in range(3):
            # Check if the input grid has enough rows and columns to sample from
            if row < input_grid.shape[0] and col < input_grid.shape[1]:
                #Check Input Color and map
                if input_grid[row, col] == 9:
                    output_grid[row, col] = 2

    return output_grid