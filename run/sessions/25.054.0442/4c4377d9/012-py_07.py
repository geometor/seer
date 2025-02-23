"""
1.  **Mirror:** Create a horizontally mirrored copy of the *original* input grid.  This means reversing the order of the columns.
2.  **Duplicate by Combination:** The output grid is formed by stacking the original input grid on top of the mirrored copy.
"""

import numpy as np

def transform(input_grid):
    # Create a horizontally mirrored copy of the input grid
    mirrored_grid = input_grid[:, ::-1]

    # Stack the original input grid on top of the mirrored copy
    output_grid = np.concatenate((input_grid, mirrored_grid), axis=0)

    return output_grid