"""
Locates azure (8) clusters in the input grid. Identifies adjacent white (0) pixels
and changes them to blue (1) in the output grid.
"""

import numpy as np

def find_azure_clusters(grid):
    # Find all azure pixels
    azure_pixels = np.argwhere(grid == 8)
    clusters = []
    visited = set()

    # helper function to perform Depth First Search
    def dfs(row, col, current_cluster):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != 8:
            return

        visited.add((row, col))
        current_cluster.append((row, col))

        # Explore adjacent cells
        dfs(row + 1, col, current_cluster)
        dfs(row - 1, col, current_cluster)
        dfs(row, col + 1, current_cluster)
        dfs(row, col - 1, current_cluster)


    for r, c in azure_pixels:
        if (r, c) not in visited:
            current_cluster = []
            dfs(r, c, current_cluster)
            clusters.append(current_cluster)

    return clusters

def find_adjacent_whites(grid, cluster):
    adjacent_whites = []
    for r, c in cluster:
        # Check neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and grid[nr, nc] == 0:
                if (nr, nc) not in adjacent_whites: #avoid duplicates
                    adjacent_whites.append((nr, nc))
    return adjacent_whites

def transform(input_grid):
    # Initialize output grid as a copy of input
    output_grid = np.copy(input_grid)
    
    # Find azure clusters
    clusters = find_azure_clusters(input_grid)
    
    #introduce blue adjacent to clusters
    for cluster in clusters:
      adjacent_whites = find_adjacent_whites(input_grid, cluster)
      if adjacent_whites:
          #only put one blue next to the cluster
          row,col = adjacent_whites[0]
          output_grid[row,col]=1

    return output_grid