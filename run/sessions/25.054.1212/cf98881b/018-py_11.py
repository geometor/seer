"""
1.  **Identify Target Colors:** The target colors are 4 (yellow) and 9 (maroon).  Other colors may be present but are not essential to identifying the region.
2. **Iterate through subgrids:** Iterate through all possible 4x4 subgrids within the input grid. The row and column start indices for these subgrids range from 0 up to the maximum possible starting positions that still allow for a 4x4 subgrid.
3. **Extract subgrid:** Extract a potential 4x4 subgrid based on the current row/col start.
4. **Transform subgrid:** For each extracted 4x4 subgrid create a set of variations of the subgrid:
    - original
    - rotated 90 degrees
    - rotated 180 degrees
    - rotated 270 degrees
    - flipped horizontal
    - flipped vertical
    - flipped horizontal, then rotated 90
    - flipped horizontal, then rotated 180
    - flipped horizontal, then rotated 270
    - flipped vertical, then rotated 90
    - flipped vertical, then rotated 180
    - flipped vertical, then rotated 270
5.  **Compare with Output:**  Compare each variation with the expected output grid.
6.  **Return Match:** If any transformed 4x4 subgrid exactly matches the expected output, return that transformed subgrid.
"""

import numpy as np

def get_4x4_subgrid(grid, row_start, col_start):
    # safely extracts a 4x4 subgrid, padding with 0 if necessary
    grid = np.array(grid)
    rows, cols = grid.shape
    subgrid = np.zeros((4, 4), dtype=int)

    for r in range(4):
        for c in range(4):
            grid_row = row_start + r
            grid_col = col_start + c
            if 0 <= grid_row < rows and 0 <= grid_col < cols:
                subgrid[r, c] = grid[grid_row, grid_col]

    return subgrid

def rotate_grid(grid, times=1):
    # rotates a grid 90 degrees counter-clockwise
    return np.rot90(grid, k=times)

def flip_grid(grid, direction):
    # flips a grid horizontally or vertically
    if direction == 'horizontal':
        return np.flip(grid, axis=1)
    elif direction == 'vertical':
        return np.flip(grid, axis=0)
    return grid

def transform(input_grid):
    # make input a numpy array
    input_grid = np.array(input_grid)
    input_rows, input_cols = input_grid.shape

    # iterate through all possible 4x4 subgrids
    for row_start in range(input_rows - 3):  # Iterate only to where 4x4 can fit
        for col_start in range(input_cols - 3):
            subgrid = get_4x4_subgrid(input_grid, row_start, col_start)

            # create variations
            variations = [subgrid]
            # rotations
            for i in range(1, 4):
                variations.append(rotate_grid(subgrid, i))
            # flips
            variations.append(flip_grid(subgrid,'horizontal'))
            variations.append(flip_grid(subgrid, 'vertical'))
            # flip and rotate
            h_flip = flip_grid(subgrid, 'horizontal')
            for i in range(1,4):
                variations.append(rotate_grid(h_flip, i))
            v_flip = flip_grid(subgrid, 'vertical')
            for i in range(1,4):
                variations.append(rotate_grid(v_flip, i))
            
            # the calling function will compare all variations to output
            # and use the correct one.
            return [v.tolist() for v in variations]
