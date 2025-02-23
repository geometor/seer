# 3aa6fb7a • 012 • refine_coder

---
```python
"""
Identifies azure (8) clusters in the input grid. For each cluster, finds adjacent white (0) pixels.
If a white pixel is adjacent to only one azure cluster, it's considered unique. Changes one unique white pixel to blue (1) for each cluster.
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

def find_adjacent_whites(grid, clusters):
    adjacent_whites = {}
    for i, cluster in enumerate(clusters):
        for r, c in cluster:
            # Check neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and grid[nr, nc] == 0:
                    if (nr, nc) not in adjacent_whites:
                        adjacent_whites[(nr, nc)] = []
                    adjacent_whites[(nr, nc)].append(i)  # Store the cluster index
    return adjacent_whites

def transform(input_grid):
    # Initialize output grid as a copy of input
    output_grid = np.copy(input_grid)
    
    # Find azure clusters
    clusters = find_azure_clusters(input_grid)
    
    # Find adjacent white pixels and the clusters they are adjacent to
    adjacent_whites = find_adjacent_whites(input_grid, clusters)

    # Find unique white neighbors
    unique_whites = {coord: cluster_indices for coord, cluster_indices in adjacent_whites.items() if len(cluster_indices) == 1}

    # Place blue pixel for each cluster based on unique adjacency
    placed_for_cluster = [False] * len(clusters) # track which clusters have had a blue pixel assigned
    for (r, c), cluster_indices in unique_whites.items():
        cluster_index = cluster_indices[0]  # Get the index of the cluster this unique white is next to
        if not placed_for_cluster[cluster_index]:
             output_grid[r, c] = 1
             placed_for_cluster[cluster_index] = True #mark that a blue was placed for that cluster
    return output_grid
```
