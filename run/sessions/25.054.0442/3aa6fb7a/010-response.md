# 3aa6fb7a • 010 • refine_coder

---
```python
"""
Locates azure (8) clusters in the input grid. For each cluster, finds adjacent white (0) pixels
and changes one of them to blue (1) in the output grid, prioritizing above, then left, then below, then right.
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
    
    # Introduce blue adjacent to clusters with prioritization
    for cluster in clusters:
        adjacent_whites = find_adjacent_whites(input_grid, cluster)
        
        # Prioritization logic: Above > Left > Below > Right
        placed = False
        for r, c in cluster:
            #check above
            if (r - 1, c) in adjacent_whites:
                output_grid[r - 1, c] = 1
                placed = True
                break #exit as soon as blue is placed
            #check left
            if not placed:
                if (r, c - 1) in adjacent_whites:
                    output_grid[r, c - 1] = 1
                    placed = True
                    break
            #check below
            if not placed:
                if (r + 1, c) in adjacent_whites:
                    output_grid[r+1, c] = 1
                    placed = True
                    break

            #check right
            if not placed:
                if(r, c + 1) in adjacent_whites:
                    output_grid[r, c + 1] = 1
                    placed = True
                    break

    return output_grid
```
