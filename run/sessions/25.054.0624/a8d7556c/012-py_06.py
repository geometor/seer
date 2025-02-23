"""
1.  **Identify Regions:** Examine the input grid. Find all regions, where a region is a group of orthogonally connected pixels of the same color. Regions are bounded by either the edge of the grid or pixels of color grey (value 5).

2.  **Find First White Region:** Among all regions of color white (value 0), identify the "first" white region. The first white region is determined by the following priority:
    *   The region whose top-most row number is smallest.
    *   If multiple regions share the same top-most row, select the region whose left-most column number is smallest.

3.  **Fill Region:** Change the color of *all* pixels within the "first" white region to red (value 2). This fill operation should be constrained by the boundaries of the region (grey pixels or the edge of the grid).

4.  **Output:** Return the modified grid. The dimensions of the output grid are identical to the input grid. Only the pixels within the identified white region are changed; all other pixels remain unchanged.
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
    Fills the region specified by the provided coordinates with red (2), using flood fill.
    """
    output_grid = np.copy(grid)
    rows, cols = grid.shape
    if not region:
      return output_grid

    # Use a queue for flood fill (BFS)
    queue = region.copy()  # Start with all pixels in the region
    visited = set()
    
    while queue:
        r, c = queue.pop(0)  # Dequeue a pixel
        if (r,c) in visited:
           continue
        
        visited.add((r,c))

        if output_grid[r,c] == 0: #check its still white
           output_grid[r, c] = 2    # Fill with red
        # Add neighbors to the queue if they are within bounds, are white, and haven't been visited
        for nr, nc in get_neighbors((r,c), rows, cols):
           if output_grid[nr,nc] == 0 and (nr, nc) not in visited:  # Only add if white
                if (nr,nc) in region: # Make sure to stay within region!
                   queue.append((nr, nc))
    
    return output_grid



def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Identify all white regions
    white_regions = find_regions(input_grid, 0)

    # Find the first white region
    first_white_region = find_first_white_region(input_grid, white_regions)

    # Fill the region using flood fill.
    if first_white_region:
        output_grid = fill_region(output_grid, first_white_region)

    return output_grid