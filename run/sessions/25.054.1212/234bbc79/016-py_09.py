"""
1.  **Identify** horizontal, contiguous groups of color 2 pixels. These groups remain unchanged in position and color.
2. **Identify** horizontal groups of color 6. These groups remain unchanged.
3. **Identify** pixels of color 5, and replace each instance with the following rules.
    - a 5 in row 1, gets replaced with a 1.
    - a 5 in row 2 adjacent to a 1, gets replaced with a 1.
    - a 5 in row 2 adjacent to a 2, gets replaced with a 2.
    - a 5 in row 3, adjacent to an 8, gets replaced with an 8.
    - a 5 in row 3 adjacent to a 3, gets replaced with a 3.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Rule 3: Handle color 5 replacement
            if output_grid[r, c] == 5:
                if r == 0:
                    # Rule 3a: If in row 1, replace with 1
                    output_grid[r, c] = 1
                elif r == 1:
                    # Rule 3b and 3c: Check adjacency in row 2
                    if c > 0 and output_grid[r, c-1] == 1:
                         output_grid[r,c] = 1
                    elif c < cols - 1 and output_grid[r, c+1] == 1:
                        output_grid[r,c] = 1
                    elif c > 0 and output_grid[r, c-1] == 2:
                        output_grid[r, c] = 2
                    elif c < cols - 1 and output_grid[r, c+1] == 2:
                        output_grid[r,c] = 2
                    else: #default
                        output_grid[r,c] = 1

                elif r == 2:
                    # Rule 3d and 3e: Check adjacency in row 3
                    if c > 0 and output_grid[r, c - 1] == 8:
                        output_grid[r, c] = 8
                    elif c < cols - 1 and output_grid[r, c + 1] == 8:
                         output_grid[r, c] = 8
                    elif c > 0 and output_grid[r, c-1] == 3:
                        output_grid[r,c] = 3
                    elif c < cols - 1 and output_grid[r, c+1] == 3:
                        output_grid[r,c] = 3
                    else: # default
                        output_grid[r,c] = 0
                else:
                    output_grid[r,c] = 0

    return output_grid