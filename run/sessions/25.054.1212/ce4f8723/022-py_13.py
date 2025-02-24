"""
1.  **Extract Target Region:** Extract the 4x4 subgrid from the top-left corner of the input grid.

2.  **Initialize Output:** Create a 4x4 output grid and fill it entirely with the color '3' (green).

3.  **Conditional '0' Preservation:**
    *   Examine each cell within the 4x4 `target_region` of the *input* grid.
    *   If a cell in the `target_region` has a value of '0', check its row (`r`) and column (`c`) indices.
    *   If `r` and `c` correspond to the locations (0,3), (1,2), (2,1) or (3,0) within target_region, then set output_grid[r,c] = 0.
    * if the `target_region` has a value of '0' on the main diagonal (\, where r == c ) or cross-diagonal (/, where r+c == 3) , copy the input values to output_grid.

4.  **Output:** The resulting 4x4 `output_grid` is the final output.
"""

import numpy as np

def get_top_left_4x4(grid):
    """Extracts the top-left 4x4 subgrid."""
    return grid[:4, :4]

def transform(input_grid):
    # Initialize output_grid with 3s
    output_grid = np.full((4, 4), 3, dtype=int)

    # Extract the 4x4 target region
    target_region = get_top_left_4x4(input_grid)

    # Conditionally preserve '0' based on its position in the input
    for r in range(4):
        for c in range(4):
            if target_region[r, c] == 0:
                if (r, c) in [(0, 3), (1, 2), (2, 1), (3, 0)]:
                     output_grid[r,c] = 0
                elif r == c:
                    output_grid[r,c] = 0
                elif r + c == 3:
                    output_grid[r,c] = 0


    return output_grid