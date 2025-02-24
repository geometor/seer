"""
1. **Reduction:** The input grid (8x4) is reduced to an output grid (4x4). The reduction is performed by taking 2x1 blocks of the input and making them a single pixel.

2.  **Disappearance:** The blue and the green regions disappear

3. **Red Region Creation:** The red regions are created on the output grid based on following this algorithm:
   *   Iterate every 2 rows, for every 4 columns on each row.
   *   If any of the pixel with value 3 (green) is detected within that 2 x 4 sub-grid, put a red pixel (value 2) at the coordinate of the input sub-grid divided by 2.
   *   if any pixel with value 1 is detected, and no pixel with value 3 is detected, and the blue pixel is the last value within that block, put a red pixel with value 2 at the top left coordinate of the input subgrid divided by 2.
4. **Background:** The white background (0) remains unchanged where there are no red pixels.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows // 2, cols), dtype=int)

    for i in range(0, rows, 2):
        for j in range(0, cols):
            subgrid = input_grid[i:i+2, j:j+1]
            
            #Check for green pixel
            if 3 in subgrid:
              output_grid[i // 2, j] = 2
            #Check for blue pixel as the last non-zero entry
            elif 1 in subgrid:
                non_zero_indices = np.nonzero(subgrid)
                if non_zero_indices[0].size > 0: # Check If there are any non zero values
                    last_non_zero_index = (non_zero_indices[0][-1], non_zero_indices[1][-1])
                    if subgrid[last_non_zero_index] == 1:
                       output_grid[i//2, j ] = 2

    return output_grid.tolist()