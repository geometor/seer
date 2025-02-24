"""
1.  **Identify Target Region:** A 4x4 region is being extracted and represented in the output grid

2.  **Consolidate Colors:** Within this, all colors, besides the '0' in the corner and a diagonal are changed to '3' (green).

3  **Preserve '0'** if the '0' in the input appears isolated in the top right corner of the target area.

4.  **Output:** The resulting 4x4 grid filled with '3's, with a possible preserved '0', is the output.
"""

import numpy as np

def get_top_left_4x4(grid):
    """Extracts the top-left 4x4 subgrid."""
    return grid[:4, :4]

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""

    # Initialize a 4x4 output grid filled with 3s.
    output_grid = np.full((4, 4), 3, dtype=int)

    # Extract the top-left 4x4 region from the input.
    target_region = get_top_left_4x4(input_grid)
    
    # Check for the isolated '0' in the top-right corner of the target region.

    if target_region[0,3] == 0:
      output_grid[0,3] = 0
    if target_region[3,0] == 0:
      output_grid[3,0]=0
    # if input_grid.shape[0] >= 4 and input_grid.shape[1] >=4:
    #   if input_grid[3,0] == 0:
    #     output_grid[3,0] = 0


    return output_grid