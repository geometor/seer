# 1-3aa6fb7a • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Clusters:** Locate all clusters of '8' (azure) pixels in the input grid.
2.  **Insert '1':** For some of the '8' pixels, especially at changes of direction of edges. replace with a `1`.
3. The overall shape of the 8's is preserved.
"""

import numpy as np

def find_clusters(grid, value):
    """Finds clusters of a specific value in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    clusters = []

    def dfs(row, col, current_cluster):
        """Depth-first search to explore a cluster."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != value
        ):
            return

        visited[row, col] = True
        current_cluster.append((row, col))

        dfs(row + 1, col, current_cluster)
        dfs(row - 1, col, current_cluster)
        dfs(row, col + 1, current_cluster)
        dfs(row, col - 1, current_cluster)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == value and not visited[row, col]:
                current_cluster = []
                dfs(row, col, current_cluster)
                clusters.append(current_cluster)

    return clusters

def transform(input_grid):
    """Transforms the input grid by inserting '1's near '8' clusters."""
    output_grid = np.copy(input_grid)
    clusters_of_8 = find_clusters(input_grid, 8)

    # identify corners/ direction changes within the clusters
    for cluster in clusters_of_8:
        for r, c in cluster:
          neighbors = []

          if r > 0:
            neighbors.append(input_grid[r-1,c])
          if r < input_grid.shape[0]-1:
            neighbors.append(input_grid[r+1,c])
          if c > 0:
            neighbors.append(input_grid[r,c-1])
          if c < input_grid.shape[1] -1:
            neighbors.append(input_grid[r, c+1])
          
          num_8_neighbors = neighbors.count(8)

          if num_8_neighbors < 2 and num_8_neighbors > 0:
              output_grid[r,c] = 1

    return output_grid
```
