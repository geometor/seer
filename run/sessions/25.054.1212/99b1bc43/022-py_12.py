"""
1.  **Consolidate Colors:** Replace all non-zero color values (except 0) in the input grid with the color green (3).
2.  **Fixed Output Size:** The output grid is always a 4x4 grid.
3. **Divide Input:** Mentally divide the Input into 4x4 subgrids.
4.  **Relative Positioning:** The green (3) blocks in the output grid maintain position as observed in the input subgrids. The white '0' cells remain '0' in Output.
5.  **Output:** Generate a 4x4 output grid where the positions of '3's correspond to the colors (other than '0') positions of the input grid, and the '0' cells in input, remain '0' in the output.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    # Initialize the output grid as a 4x4 array filled with 0s (white).
    output_grid = np.zeros((4, 4), dtype=int)

    # Iterate through the input grid, up to a maximum of 4x4.
    for i in range(min(input_grid.shape[0], 4)):
        for j in range(min(input_grid.shape[1], 4)):
            # If the input pixel is not 0, set the corresponding output pixel to 3.
            if input_grid[i, j] != 0:
                output_grid[i, j] = 3

    return output_grid