"""
1.  **Corner Replacement:**  Locate all gray (5) pixels in the input grid. If a gray pixel is at a corner of the grid, change it to white (0).
2.  **Preserve original**: Before step 3, for each gray pixel store it's original adjacent colors
3.  **Adjacent Replacement:** For each white pixel (0) that *was* a gray pixel, check its immediate neighbors (up, down, left, and right - not diagonally).  If a neighbor was of one of the original adjacencies, change that pixel to white (0) as well.
4.  Continue expanding the adjacency check to the newly changed white squares until no more changes can be made.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """Returns the neighbors of a cell and their original colors."""
    rows, cols = grid.shape
    neighbors = {}
    if r > 0:
        neighbors[(r - 1, c)] = grid[r-1, c] # Up
    if r < rows - 1:
        neighbors[(r + 1, c)] = grid[r+1, c]  # Down
    if c > 0:
        neighbors[(r, c - 1)] = grid[r, c-1] # Left
    if c < cols - 1:
        neighbors[(r, c + 1)] = grid[r, c+1]  # Right
    return neighbors
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Store original neighbors of gray pixels
    gray_neighbors = {}
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 5:
                gray_neighbors[(r, c)] = get_neighbors(input_grid, r, c)

    # Corner Replacement
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                if (r == 0 and c == 0) or \
                   (r == 0 and c == cols - 1) or \
                   (r == rows - 1 and c == 0) or \
                   (r == rows - 1 and c == cols - 1):
                    output_grid[r, c] = 0  # Corner replacement

    # Adjacent Replacement (Iterative)
    changed = True
    while changed:
        changed = False
        new_output_grid = np.copy(output_grid)
        for r in range(rows):
            for c in range(cols):
                if output_grid[r, c] == 0 and (r,c) in gray_neighbors:
                    for (nr, nc), color in gray_neighbors[(r,c)].items():
                         if output_grid[nr, nc] == color:
                             new_output_grid[nr, nc] = 0
                             changed = True
        output_grid = new_output_grid
    
    return output_grid