# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
import numpy as np

def find_azure_clusters(grid):
    """
    Finds separate clusters of azure (color 8) pixels.
    """
    visited = set()
    clusters = []

    def dfs(row, col, current_cluster):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != 8:
            return
        visited.add((row, col))
        current_cluster.append((row, col))
        # Check all 8 neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_cluster)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 8 and (i, j) not in visited:
                current_cluster = []
                dfs(i, j, current_cluster)
                clusters.append(current_cluster)
    return clusters

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Azure objects are preserved.
    - For each separate cluster of azure objects, find the top right most azure pixel within that cluster and transform the pixel up and to the left of that pixel to blue.
    """
    output_grid = np.copy(input_grid)
    azure_clusters = find_azure_clusters(input_grid)

    for cluster in azure_clusters:
        if cluster:
            #Find top-right corner of each cluster
            top_right_row =  min(pos[0] for pos in cluster)
            possible_cols = [pos[1] for pos in cluster if pos[0] == top_right_row]
            top_right_col = max(possible_cols)

            # Place blue pixel one up and one left if possible.
            if(top_right_row-1 >= 0 and top_right_col-1 >= 0):
              output_grid[top_right_row - 1, top_right_col - 1] = 1

    return output_grid
```

