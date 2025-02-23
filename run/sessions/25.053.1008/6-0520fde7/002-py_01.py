"""
1.  **Locate Center:** Find the central 3x3 subgrid within the input grid.
2.  **Extract Subgrid:** Extract this 3x3 subgrid.
3. **Recolor Center:** Change the center of the output grid to red.
4. **Set Surroundings** Set all pixels not changed by the prior rule to be white.
5. output the smaller grid
"""

import numpy as np

def get_center_subgrid(grid, subgrid_size=3):
    """Extracts the central subgrid of a given size."""
    rows, cols = grid.shape
    center_row = rows // 2
    center_col = cols // 2
    row_start = center_row - subgrid_size // 2
    row_end = row_start + subgrid_size
    col_start = center_col - subgrid_size // 2
    col_end = col_start + subgrid_size
    return grid[row_start:row_end, col_start:col_end]

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)

    # get the centermost 3x3 grid
    center_subgrid = get_center_subgrid(input_grid)

    #  recolor the center of input to red, which will propigate to the center of the output
    center_row, center_col = center_subgrid.shape[0] // 2, center_subgrid.shape[1] // 2
    
    
    # change the center to red
    output_grid[center_row,center_col] = 2

    return output_grid