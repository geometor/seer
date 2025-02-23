# 1-3aa6fb7a • 008 • example_2 - CODE

---
```python
"""
1.  **Identify Azure Clusters:** Locate all contiguous clusters of azure (8) pixels in the input grid. A cluster can be a single isolated pixel or a group of adjacent pixels.

2. **Inner Replacement** For each azure cluster of more than one pixel, going from left to right, top to bottom, find each 8 that has adjacent 8s on all four sides (up, down, left, right) and replace the first found 8 with a 1.

3. **Outer Placement**: Locate all azure pixels on the edges of an azure cluster that are adjacent to zero (white) pixels on the top-left diagonal. If a 8 is found adjacent to a white on its top left diagonal, replace the white with a 1.

4.  **Output:** The resulting grid, after these replacements, is the output grid.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Get the neighbors of a cell (up, down, left, right, diagonals)."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the cell itself
            neighbor_row, neighbor_col = row + i, col + j
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                neighbors.append((neighbor_row, neighbor_col))
    return neighbors

def find_azure_clusters(grid):
    """Find all clusters of azure (8) pixels."""
    rows, cols = grid.shape
    visited = set()
    clusters = []

    def dfs(row, col, current_cluster):
        """Depth-first search to find connected components."""
        if (row, col) in visited or grid[row, col] != 8:
            return
        visited.add((row, col))
        current_cluster.append((row, col))
        for neighbor_row, neighbor_col in get_neighbors(grid, row, col):
            if abs(neighbor_row - row) <= 1 and abs(neighbor_col - col) <=1: # Check direct neighbors
                if (neighbor_row, neighbor_col) not in visited:
                    dfs(neighbor_row, neighbor_col, current_cluster)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 8 and (row, col) not in visited:
                current_cluster = []
                dfs(row, col, current_cluster)
                clusters.append(current_cluster)
    return clusters

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    clusters = find_azure_clusters(output_grid)

    # Inner Replacement
    for cluster in clusters:
        if len(cluster) > 1:
            for row, col in cluster:
                neighbors = get_neighbors(output_grid, row, col)
                num_azure_neighbors = 0
                for n_row, n_col in neighbors:
                    if abs(n_row - row) <=1 and abs(n_col - col) <= 1:
                        if output_grid[n_row, n_col] == 8:
                            num_azure_neighbors +=1
                if num_azure_neighbors == 8:
                    output_grid[row,col] = 1
                    break # only first match should change

    # Outer Placement
    for row in range(rows):
        for col in range(cols):
            if output_grid[row, col] == 8:
                neighbors = get_neighbors(output_grid, row, col)
                for n_row, n_col in neighbors:
                     if n_row == row - 1 and n_col == col - 1 and output_grid[n_row,n_col] == 0:
                        output_grid[n_row,n_col] = 1

    return output_grid
```
