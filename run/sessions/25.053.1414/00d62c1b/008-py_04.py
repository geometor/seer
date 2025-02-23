"""
1.  **Identify Green Clusters:** Locate all contiguous blocks of green (3) pixels within the grid.
2.  **Locate Target Pixel:** If there are at least three green pixels forming an L-shape (2x2 minus the top-left pixel), select the single green pixel for modification that lies on the top-right tip of the L-shape.
3. **Change Pixel color to yellow (4) in the grid**.

In more detail, if an L-shape can be formed, we look for a green pixel (A) which is adjacent to:
 - green pixel below, and
 - green pixel diagonally down and to the left.

If such a pixel (A) is found, its color is changed from green to yellow.
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
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            dfs(r + dr, c + dc, current_cluster)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 3 and not visited[r, c]:
                current_cluster = []
                dfs(r, c, current_cluster)
                clusters.append(current_cluster)
    return clusters

def find_l_shape_target(grid, cluster):
    """
    Finds the target pixel within a green cluster based on the L-shape rule.
    """
    for r, c in cluster:
      below = (r+1,c)
      diag = (r+1, c-1)

      if below in cluster and diag in cluster:
          return (r,c)
    return None



def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # find clusters
    clusters = find_green_clusters(output_grid)
    
    # iterate through clusters
    for cluster in clusters:
        # find target
        target_pixel = find_l_shape_target(output_grid, cluster)
        # set to yellow
        if target_pixel:
            output_grid[target_pixel] = 4

    return output_grid