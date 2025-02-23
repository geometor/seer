"""
1.  **Identify Regions:** The input grid consists of pixels with values from 0 to 9, representing different colors. Find all regions, where a region is defined as a contiguous block of pixels of the same color, that are bounded by either the edge of the grid, or a grey (value 5) pixel.

2.  **Find First White Region.** Among the white (value 0) regions, find the region whose top-most row is the lowest. If there are multiple such regions, the region that starts at the lowest column takes priority.
    
3.  **Fill Region:** Starting with the top-most row of this region, change the color of all pixels in the region to red (value 2) until a grey pixel or the grid boundary is reached.

4.  **Iterate:** Repeat this process for all rows of the specified white region, changing the color of all white pixels to red that are within that region, until a grey pixel, or the edge of the grid is reached.
    
5.  **No Modification of Other Pixels:** The gray (5) pixels and all other regions are not to be modified. The final output grid has the same dimensions as the input.
"""

import numpy as np

def get_neighbors(pos, rows, cols):
    """Returns the valid neighbors of a given position."""
    r, c = pos
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def find_regions(grid, color):
    """Finds all regions of the specified color in the grid."""
    rows, cols = grid.shape
    visited = set()
    regions = []

    def dfs(pos, current_region):
        """Depth-first search to find connected regions."""
        if pos in visited or grid[pos] != color:
            return
        visited.add(pos)
        current_region.append(pos)
        for neighbor in get_neighbors(pos, rows, cols):
            # Check for boundary (grey pixel or edge)
            if grid[neighbor] != color and grid[neighbor] !=5:
                continue
            dfs(neighbor, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_region = []
                dfs((r, c), current_region)
                regions.append(current_region)
    return regions

def find_first_white_region(grid, white_regions):
    """Finds the first white region based on top-most row and then left-most column."""
    if not white_regions:
        return None

    # Sort regions by top-most row (and then left-most column for ties)
    sorted_regions = sorted(white_regions, key=lambda region: (min(r for r, _ in region), min(c for _, c in region)))
    return sorted_regions[0]

def fill_region(grid, region):
    """
    Fill the region specified by the provided coordinates.
    """
    output_grid = np.copy(grid)
    min_row = min(r for r, _ in region)
    
    
    for r,c in region:
        if grid[r,c] == 0:
           output_grid[r,c] = 2
    return output_grid



def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Identify all white regions
    white_regions = find_regions(input_grid, 0)

    # Find the first white region
    first_white_region = find_first_white_region(input_grid, white_regions)

    # Fill the region.
    if first_white_region:
        output_grid = fill_region(output_grid, first_white_region)

    return output_grid