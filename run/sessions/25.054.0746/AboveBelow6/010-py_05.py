"""
1.  **Identify Red Regions:** Find all contiguous blocks of red (2) pixels in the input grid.
2.  **Conditional Extension:** For each contiguous block of red pixels:
     * Extend one row down and copy the object.
"""

import numpy as np

def find_red_regions(grid):
    """Finds contiguous blocks of red pixels."""
    red_regions = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(row, col, current_region):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] != 2:
            return
        visited.add((row, col))
        current_region.append((row, col))

        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 2 and (r, c) not in visited:
                current_region = []
                dfs(r, c, current_region)
                red_regions.append(current_region)
    return red_regions

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find red regions
    red_regions = find_red_regions(input_grid)
    
    #perform extension based on line.
    for region in red_regions:
        # Find the row indices for this region
        rows_in_region = sorted(list(set([r for r, c in region])))

        #copy object to one row down
        for r,c in region:
            if r+1 < rows:
                output_grid[r+1,c] = 2
            
    return output_grid