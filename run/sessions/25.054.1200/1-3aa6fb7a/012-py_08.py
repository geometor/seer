"""
1.  **Identify Azure Clusters:** Locate all connected regions (clusters) of azure (8) pixels in the input grid. Orthogonal connectivity defines a cluster.
2.  **Outline with Blue:** For each azure cluster, place blue (1) pixels *around* the cluster.  The blue pixels should be placed orthogonally adjacent to azure pixels, effectively forming an outline of the azure shape. The blue pixels *do not* replace azure pixels *within* a continuous region, they only trace the exterior boundary.
3. **Preserve Azure Regions**: Do not modify regions without azure.
4. **One Pixel Outline:** Ensure the outline is one pixel wide where possible.
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

def get_neighbors(grid, r, c):
    """Gets the orthogonal neighbors of a cell."""
    neighbors = []
    rows, cols = grid.shape
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def transform(input_grid):
    """Transforms the input grid by outlining '8' clusters with '1's."""
    output_grid = np.copy(input_grid)
    clusters_of_8 = find_clusters(input_grid, 8)

    for cluster in clusters_of_8:
        # Create a set for faster neighbor checking
        cluster_set = set(cluster)
        for r, c in cluster:
            # Check neighbors for potential outline placement
            for nr, nc in get_neighbors(input_grid, r, c):
                if (nr, nc) not in cluster_set and output_grid[nr,nc] == 0:
                    output_grid[nr, nc] = 1

    return output_grid