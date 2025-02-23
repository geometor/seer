# 00d62c1b • 010 • refine_coder

---
```python
"""
1.  **Identify Green Clusters:** Locate all contiguous blocks (clusters) of green (3) pixels in the input grid.
2.  **Identify Target Pixels within Clusters:**
    *   For each green pixel within a cluster, examine its neighbors.
    *   If a green pixel has green neighbors directly below (south), to its left (west) and diagonal down and to its left (southwest), it is a target pixel.
3.  **Transform Target Pixels:** Change the color of all identified target pixels from green (3) to yellow (4).
4.  The output grid is the same size as the input grid and all non-target pixels are the same as in the input.
"""

import numpy as np

def find_green_clusters(grid):
    """
    Identifies contiguous blocks of green pixels.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    clusters = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_cluster):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != 3:
            return
        visited[r, c] = True
        current_cluster.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Only cardinal directions for contiguity
            dfs(r + dr, c + dc, current_cluster)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 3 and not visited[r, c]:
                current_cluster = []
                dfs(r, c, current_cluster)
                clusters.append(current_cluster)
    return clusters

def find_all_target_pixels(grid, clusters):
    """
    Finds all target pixels within all green clusters based on the neighbor rule.
    """
    target_pixels = []
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    for cluster in clusters:
        for r, c in cluster:
            # Check neighbors: below (south), left (west), and southwest
            south = (r + 1, c)
            west = (r, c - 1)
            southwest = (r + 1, c - 1)

            if (is_valid(south[0], south[1]) and grid[south] == 3 and
                is_valid(west[0], west[1]) and grid[west] == 3 and
                is_valid(southwest[0], southwest[1]) and grid[southwest] == 3):
                target_pixels.append((r, c))
    return target_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find clusters
    clusters = find_green_clusters(output_grid)

    # find all target pixels
    target_pixels = find_all_target_pixels(output_grid, clusters)

    # set target pixels to yellow
    for r, c in target_pixels:
        output_grid[r, c] = 4

    return output_grid
```
