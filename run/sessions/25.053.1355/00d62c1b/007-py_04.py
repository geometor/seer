"""
1. Identify Green Regions: Find all contiguous regions of green (value 3) pixels in the input grid. A contiguous region is a group of green pixels where each pixel is directly adjacent (up, down, left, or right – not diagonally) to at least one other pixel in the group.
2. Determine Enclosure: For each identified green region, determine if it is "enclosed." A region is considered enclosed if *none* of its pixels are on the edge of the grid.
3. Transform Enclosed Pixels: Change the color of all pixels within the enclosed green regions from green (3) to yellow (4).
"""

import numpy as np

def flood_fill(grid, r, c, visited, region):
    """Performs a flood fill to identify a contiguous region."""
    rows, cols = grid.shape
    if (r < 0 or r >= rows or c < 0 or c >= cols or
        grid[r, c] != 3 or (r, c) in visited):
        return
    visited.add((r, c))
    region.append((r, c))
    flood_fill(grid, r + 1, c, visited, region)
    flood_fill(grid, r - 1, c, visited, region)
    flood_fill(grid, r, c + 1, visited, region)
    flood_fill(grid, r, c - 1, visited, region)

def is_enclosed(grid, region):
    """Checks if a region is enclosed (not touching the edge)."""
    rows, cols = grid.shape
    for r, c in region:
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            return False
    return True

def transform(input_grid):
    """Transforms enclosed green regions to yellow."""
    grid = np.array(input_grid)  # Ensure we're working with a NumPy array
    rows, cols = grid.shape
    output_grid = grid.copy()
    visited = set()
    
    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # If we find a green pixel that hasn't been visited yet
            if grid[r, c] == 3 and (r, c) not in visited:
                region = []
                flood_fill(grid, r, c, visited, region)  # Find the contiguous region
                
                # If the region is enclosed, change all its pixels to yellow
                if is_enclosed(grid, region):
                    for row, col in region:
                        output_grid[row, col] = 4
    return output_grid.tolist()