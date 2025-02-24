"""
1.  **Input and Output:** The input is a 5x5 grid, and the output is a 3x3 grid.

2.  **Color Mapping:** Only colors 0 (white) and 5 (gray) appear in the output.

3.  **Conditional Gray Regions:**
    * a. Check for Green Pixels: Check for the presence of green pixels in the overlapping 3x3 regions in the input.
    * If the color green IS present in the input:
        * If any green (3) pixels are present in the bottom-left 3x3 area, the bottom-left cell of the output is gray.
        * If any green (3) pixels are present in the bottom-center 3x3 area, the bottom-center cell of the output is gray.
        * If any green (3) pixels are present in the bottom-right 3x3 area, the bottom-right cell of the output is gray.
        * If any green (3) pixels are in the top-right 3x3 area, the top right output cell is grey.
        * Other pixels in the output are white.
    * If the color green is NOT present:
        * set the output to be a "cross" of grey pixels: top row, center column, and bottom row.

4. **Overlapping Regions:** The 3x3 regions in the input *overlap*. That is, we consider multiple 3x3 slices of the 5x5 input.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as 3x3 with all white (0)
    output_grid = np.zeros((3, 3), dtype=int)

    # Check if green exists in the input grid
    if np.any(input_grid == 3):
        # Check bottom-left 3x3 region
        if np.any(input_grid[2:5, 0:3] == 3):
            output_grid[2, 0] = 5

        # Check bottom-center 3x3 region
        if np.any(input_grid[2:5, 1:4] == 3):
            output_grid[2, 1] = 5

        # Check bottom-right 3x3 region
        if np.any(input_grid[2:5, 2:5] == 3):
            output_grid[2, 2] = 5

        # Check top-right 3x3 region
        if np.any(input_grid[0:3, 2:5] == 3):
            output_grid[0, 2] = 5

    else:
        # Create a gray cross pattern
        output_grid[0, :] = 5  # Top row
        output_grid[1, 1] = 5  # Center pixel
        output_grid[2, :] = 5  # Bottom row

    return output_grid