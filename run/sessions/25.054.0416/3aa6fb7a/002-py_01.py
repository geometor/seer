"""
1.  **Identify Azure Regions:** Locate all contiguous regions of azure (8) pixels within the input grid.
2.  **Check adjacency:** For every azure pixel, find the number of adjacent azure pixels
3. **Change one pixel:** working left to right, top to bottom, for each region of azure pixels, change the color of the first azure pixel that does not have an adjacent azure pixel above or to the left, to blue.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col, color):
    """
    Gets the coordinates of adjacent pixels with same color.
    """
    rows, cols = grid.shape
    adjacent = []

    # Check above
    if row > 0 and grid[row-1, col] == color:
        adjacent.append((row-1, col))
    # Check below
    if row < rows - 1 and grid[row+1, col] == color:
        adjacent.append((row+1, col))
    # Check left
    if col > 0 and grid[row, col-1] == color:
        adjacent.append((row, col-1))
    # Check right
    if col < cols - 1 and grid[row, col+1] == color:
        adjacent.append((row, col+1))

    return adjacent

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    # iterate through each cell to find azure regions
    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 8 and not visited[r,c]:
                # find all connected azure pixels.
                region = []
                queue = [(r,c)]
                visited[r,c] = True
                
                while queue:
                    row, col = queue.pop(0)
                    region.append((row,col))
                    adjacent_pixels = get_adjacent_pixels(input_grid, row, col, 8)
                    
                    for adj_r, adj_c in adjacent_pixels:
                        if not visited[adj_r, adj_c]:
                            visited[adj_r,adj_c] = True
                            queue.append((adj_r, adj_c))

                #find the first azure that meets criteria
                for row, col in region:
                  adjacent_pixels = get_adjacent_pixels(input_grid, row, col, 8)
                  found_adj = False
                  for adj_r, adj_c in adjacent_pixels:
                    if adj_r < row or (adj_r == row and adj_c < col):
                      found_adj = True
                      break
                  if not found_adj:
                    output_grid[row,col] = 1
                    break

    return output_grid