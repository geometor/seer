"""
1.  **Identify Region of Interest:** Focus on the top-left section within rows 0-3 and columns 0-3 of the input grid which is all the values of '7'. All other areas will be ignored.
2.  **Translate Color:** Replace all values in the top left region of '7' to a single color, '3' (green).
3. **Create Output Grid:** Create a new 4x4 grid, representing the focused section in the top left hand corner.
4.  **Populate Output:** Fill the corresponding cells to the area of interest in the output grid. Where color 7 existed in the input grid within the 4x4 section, put colour 3 in the output grid.
5. **Default Background**: If any output cell is outside of the area identified in step one, set the color to 0 (white).
"""

import numpy as np

def transform(input_grid):
    # Create a new 4x4 output grid filled with 0s (white).
    output_grid = np.zeros((4, 4), dtype=int)

    # Iterate through the top-left 4x4 region of the input grid.
    for i in range(min(4, input_grid.shape[0])):
        for j in range(min(4, input_grid.shape[1])):
            # If the input pixel is 7, set the corresponding output pixel to 3.
            if input_grid[i, j] == 7:
                output_grid[i, j] = 3

    return output_grid