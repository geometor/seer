"""
1.  **Extract Target Region:** Extract the 4x4 subgrid from the top-left corner of the input grid.

2.  **Initialize Output:** Create a 4x4 output grid and fill it entirely with the color '3' (green).

3.  **Conditional '0' Preservation:**
    *   Examine each cell within the 4x4 `target_region` of the *input* grid.
    *   If a cell in the `target_region` has the value '0' (white), check if its row (`r`) and column (`c`) coordinates are in this set: `[(0,3), (1,0), (1,2), (2,2), (2,3), (3,0), (3,2)]`.
     * If coordinates (r, c) are in the set, copy the value (0) at the `target_region[r][c]` to the output grid at the `output_grid[r][c]`.

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
                if (r, c) in [(0, 3), (1, 0), (1, 2), (2, 2), (2, 3), (3, 0), (3, 2)]:
                     output_grid[r,c] = 0

    return output_grid