# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: "Scattered azure pixels forming three distinct clusters."
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: "Same as input"
    - color: 1
      positions: [(1, 4), (2,3), (5,3)]
      shape: "Three blue pixels."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. Here, three azure clusters of different shapes are visible.

2.  **Preserve Azure Objects:** The azure objects are preserved.

3. **Detect Azure object positions and put blue pixels:**
   For each azure colored object, find the "top-right" azure pixel within that object and move one pixel up and one pixel to the left to place a blue pixel (color 1).

**Transformation Rule Summary**

The transformation rule is as follows:

-   Azure objects are copied from the input to the output grid.
-   For each separate cluster of azure objects, find the top right most azure pixel within that cluster and transform the pixel up and to the left of that pixel to blue.

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

