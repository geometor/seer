"""
Counts the number of distinct white (0) regions in the input grid, considering diagonal adjacency.
"""

import numpy as np

def find_regions(grid, color):
    """
    Finds distinct regions of a specific color in the grid, including diagonal connections.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    region_count = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(row, col):
        """
        Depth-first search to explore a connected region, including diagonals.
        """
        if (row, col) in visited or not is_valid(row, col) or grid[row][col] != color:
            return
        visited.add((row, col))
        # Explore all 8 adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:  # Skip the current cell itself
                    continue
                dfs(row + dr, col + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and (r, c) not in visited:
                dfs(r, c)
                region_count += 1
    return region_count
    

def transform(input_grid):
    """
    Counts the number of distinct white (0) regions in the input grid, considering diagonal adjacency.
    """
    # Convert input_grid to a NumPy array for easier processing.
    grid = np.array(input_grid)

    # Find and count white regions, including diagonal connections.
    white_regions_count = find_regions(grid, 0)
    
    # The output should be represented as a single-element grid (1x1) showing
    # the count.
    output_grid = np.array([[white_regions_count]])
    return output_grid