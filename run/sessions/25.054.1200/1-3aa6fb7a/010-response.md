# 1-3aa6fb7a • 010 • refine_coder

---
```python
"""
1.  **Identify Clusters:** Find all connected clusters of '8' (azure) pixels in the input grid. Consider pixels to be connected orthogonally.

2.  **Locate Strategic Points:** Within each '8' cluster, identify "strategic points" for inserting '1's. Strategic points are defined as:
    *   **Endpoints:** An '8' pixel with only one orthogonally adjacent '8' neighbor.
    *   **Corners:** An '8' pixel where the direction of the cluster changes. This is determined by:
        *   The '8' has exactly two orthogonally adjacent '8' pixels that are not orthogonally adjacent to *each other*.
        *   An '8' on a diagonal cluster boundary.
    * **Inside Bends**: Where the cluster has two adjacent '8' pixels *and* at least one diagonally adjacent '8' pixel
    *   **Do not place at boundaries that do not contain an '8' pixel:**

3. **Insert '1's:** Replace the '8' pixels at the identified strategic points with '1' (blue) pixels.

4. **Preserve shape:** The new '1' pixels, together with the remaining '8' pixels, preserve the general outline and direction changes.
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

def get_neighbors(grid, r, c, value=None):
    """Gets the orthogonal and diagonal neighbors of a cell, optionally filtering by value."""
    neighbors = []
    rows, cols = grid.shape

    # Orthogonal neighbors
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if value is None or grid[nr, nc] == value:
                neighbors.append((nr, nc))
    return neighbors

def get_diagonal_neighbors(grid, r, c, value=None):
    neighbors = []
    rows, cols = grid.shape

    for dr, dc in [(1,1), (1,-1), (-1, 1), (-1,-1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if value is None or grid[nr, nc] == value:
                neighbors.append((nr, nc))

    return neighbors

def is_endpoint(grid, r, c, cluster):
    """Checks if a cell is an endpoint of a cluster."""
    neighbors = get_neighbors(grid, r, c, value=8)
    return len(neighbors) == 1

def is_corner(grid, r, c, cluster):
    """Checks if a cell is a corner of a cluster."""
    neighbors = get_neighbors(grid, r, c, value=8)
    if len(neighbors) == 2:
        n1r, n1c = neighbors[0]
        n2r, n2c = neighbors[1]
        # Check if neighbors are not orthogonally adjacent
        if abs(n1r - n2r) + abs(n1c - n2c) > 1:
            return True
    
    return False

def is_inside_bend(grid, r, c, cluster):
    neighbors = get_neighbors(grid, r, c, 8)
    diagonal_neighbors = get_diagonal_neighbors(grid, r, c, 8)

    if len(neighbors) >= 2 and len(diagonal_neighbors) >= 1:
       return True
    return False
    

def transform(input_grid):
    """Transforms the input grid by inserting '1's near '8' clusters."""
    output_grid = np.copy(input_grid)
    clusters_of_8 = find_clusters(input_grid, 8)

    for cluster in clusters_of_8:
        for r, c in cluster:
            if is_endpoint(input_grid, r, c, cluster) or is_corner(input_grid, r, c, cluster) or is_inside_bend(input_grid, r, c, cluster):
                output_grid[r, c] = 1

    return output_grid
```
