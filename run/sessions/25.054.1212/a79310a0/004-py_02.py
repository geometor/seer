"""
1. Identify the contiguous region of azure (8) pixels in the input grid. This region can be of any size and shape.
2. Change the color of all pixels within this identified region from azure (8) to red (2).
3. Move the entire red region down by one row. The shape and size of the region remain unchanged.
4. All other pixels in the grid that were not part of the original azure region should remain unchanged (white, value 0).
"""

import numpy as np

def find_contiguous_region(grid, color):
    """Finds a contiguous region of a given color in the grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    region = []

    def dfs(row, col):
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        region.append((row, col))
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == color and not visited[i, j]:
                dfs(i, j)
                return region  # Return as soon as the first region is found
    return [] # no region


def transform(input_grid):
    # initialize output_grid as a copy of input
    output_grid = np.copy(input_grid)
    
    # find the azure region
    azure_region = find_contiguous_region(input_grid, 8)

    if not azure_region:
        return output_grid # return if no azure region found

    # change azure to red in place
    for row, col in azure_region:
        output_grid[row, col] = 2
        
    # clear old positions
    for row, col in azure_region:
      output_grid[row,col] = 0
    
    # move red region down by one
    for row, col in azure_region:
        new_row = row + 1
        if new_row < output_grid.shape[0]: # check boundaries
           output_grid[new_row,col] = 2

    return output_grid