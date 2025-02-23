"""
1.  **Identify Azure (8) Pixels:** Locate all pixels that are azure (color 8).
2.  **Conditional Changes based on adjacent colors**
    *   If an azure (8) pixel is adjacent to the edge of an object of color 4, the
        azure pixel might change to a different color, such as 3,5,9, based on
        relative position.
    *   If a pixel of color 4 is adjacent to an object of color 6, change to a 1.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """Gets the neighbors of a pixel, including diagonals."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if (i, j) != (r, c):
                neighbors.append(grid[i, j])
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Conditional changes for Azure (8) pixels
            if input_grid[r, c] == 8:
                neighbors = get_neighbors(input_grid, r, c)
                adjacent_to_4 = 4 in neighbors
                
                if adjacent_to_4:
                    # Determine relative position for changes.  This is still a guess,
                    # but it's based on local interaction, not global coordinates.

                    # check color 4 neighbors.
                    color_4_neighbors = []
                    for i in range(max(0, r - 1), min(rows, r + 2)):
                        for j in range(max(0, c - 1), min(cols, c + 2)):
                            if (i, j) != (r, c) and input_grid[i,j] == 4:
                                color_4_neighbors.append((i,j))

                    if len(color_4_neighbors) > 0:
                        # find relative location of first color 4 neighbor
                        n_r, n_c = color_4_neighbors[0]
                        if n_r < r: # above
                            if n_c < c: #above and left
                                output_grid[r,c] = 3
                            elif n_c > c: # above and right
                                output_grid[r,c] = 5
                            else: # directly above
                                output_grid[r,c] = 9

                        elif n_r > r: # below
                            if n_c < c: # below and left
                                output_grid[r,c] = 5
                            elif n_c > c:
                                output_grid[r,c] = 9
                            else:
                                output_grid[r,c] = 3
                        else: # same row
                            if n_c < c:
                                output_grid[r,c] = 3
                            elif n_c > c:
                                output_grid[r,c] = 5
            elif input_grid[r,c] == 4:
                neighbors = get_neighbors(input_grid, r, c)
                if 6 in neighbors:
                    output_grid[r,c] = 1

    return output_grid