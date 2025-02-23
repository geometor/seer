"""
Identifies connected azure (8) colored objects and replaces azure pixels with blue (1) if the azure pixels are on the edge of the azure object and adjacent to empty space (0).
"""

import numpy as np

def get_neighbors(grid, r, c):
    """Returns the valid neighbors of a cell in a grid."""
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def find_connected_regions(grid, color):
    """Finds connected regions of a given color in the grid."""
    rows, cols = grid.shape
    visited = set()
    regions = []

    def dfs(r, c, current_region):
        """Depth-first search to find connected components."""
        if (r, c) in visited or grid[r, c] != color:
            return
        visited.add((r, c))
        current_region.append((r, c))
        for nr, nc in get_neighbors(grid, r, c):
            dfs(nr, nc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_region = []
                dfs(r, c, current_region)
                regions.append(current_region)
    return regions

def find_edge_pixels(grid, region):
    """Identifies edge pixels of a region that border empty space (0)."""
    edge_pixels = []
    for r, c in region:
        for nr, nc in get_neighbors(grid, r, c):
            if grid[nr, nc] == 0:
                edge_pixels.append((r, c))
                break  # Move to the next pixel in the region
    return edge_pixels
    

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # 1. Identify Connected Azure Regions
    azure_regions = find_connected_regions(output_grid, 8)

    # 2. Iterate through each azure region
    for region in azure_regions:
       # 3. Identify edge pixels
       edge_pixels = find_edge_pixels(output_grid, region)

       # 4. change color of edge pixels
       for r,c in edge_pixels:
           output_grid[r,c] = 1
    
    return output_grid