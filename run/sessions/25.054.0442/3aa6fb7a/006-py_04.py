"""
1.  **Identify Clusters:** Find all distinct clusters of azure (8) pixels in the input grid.  A cluster is a group of orthogonally connected azure pixels.

2.  **Find Center Pixel:** For each azure cluster:
    *   Find the centermost pixels.
    *   Prioritize the top-left pixel among the centermost pixels.

3.  **Replace Pixel:** Change the value of the selected center pixel in each cluster from azure (8) to blue (1).

4.  **Preserve Other Pixels:** All other pixels in the grid remain unchanged.
"""

import numpy as np

def find_clusters(grid, value):
    """Finds all clusters of a given value in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    clusters = []

    def dfs(row, col, current_cluster):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != value):
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

def find_center_pixel(cluster):
    """Finds the centermost pixel, prioritizing top-left."""
    rows = [p[0] for p in cluster]
    cols = [p[1] for p in cluster]

    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    center_row = (min_row + max_row) // 2
    center_col = (min_col + max_col) // 2
    
    # gather the centermost pixels
    center_pixels = []
    for row, col in cluster:
        if (row == center_row or row == center_row) and (col == center_col or col == center_col):
            center_pixels.append((row,col))

    # prioritize top left
    if len(center_pixels) > 1:
        center_pixels.sort(key=lambda x: (x[0], x[1]))
    
    return center_pixels[0]
    


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    # find clusters of 8s
    clusters = find_clusters(output_grid, 8)
    # replace center of each cluster with 1s
    for cluster in clusters:
        center_pixel = find_center_pixel(cluster)
        output_grid[center_pixel] = 1

    return output_grid