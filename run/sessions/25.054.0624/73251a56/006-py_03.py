"""
1. Iterate through each pixel in the input grid.
2. Identify Regions: For each pixel, determine if it's part of a contiguous region of the *same* color.
3. Check for Enclosure: For each region identified:
    *   Determine if the region is *completely enclosed* by pixels of a *different* color. A region is considered enclosed if all pixels along its boundary are adjacent (horizontally, vertically, or diagonally) to pixels of a different color.
4. Fill Enclosed Regions: If a region is enclosed, change *all* pixels within that region to blue (color value 1).
5. Retain other pixels: All pixels that are not within the enclosed region will retain their original values.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Get the neighbors of a cell (including diagonals).
    """
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append((i, j))
    return neighbors

def get_region(grid, row, col, visited):
    """
    Gets the contiguous region of the same color using flood fill.
    Returns the set of (row, col) tuples in the region.
    """
    rows, cols = grid.shape
    start_color = grid[row, col]
    region = set()
    stack = [(row, col)]
    visited.add((row,col))

    while stack:
        r, c = stack.pop()
        region.add((r, c))
        neighbors = get_neighbors(grid, r, c)
        for nr, nc in neighbors:
            if (nr, nc) not in visited and grid[nr, nc] == start_color:
                visited.add((nr, nc))
                stack.append((nr, nc))
    return region

def is_enclosed_region(grid, region):
    """
    Checks if an entire region is enclosed by pixels of a different color.
    """
    enclosed = True
    for row, col in region:
        neighbors = get_neighbors(grid, row, col)
        for nr, nc in neighbors:
            if (nr, nc) not in region:
                if grid[nr, nc] == grid[row,col]:
                  return False

    # check that the region is not along any edges
    rows,cols = grid.shape
    for row,col in region:
      if row == 0 or row == rows - 1 or col == 0 or col == cols -1:
        return False
    
    return enclosed

def transform(input_grid):
    """
    Transforms the input grid by filling enclosed regions of any color with blue (1).
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = set()

    # Iterate through each pixel
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                # Get the region for the current pixel
                region = get_region(input_grid, row, col, visited)

                # Check if the region is enclosed
                if is_enclosed_region(input_grid, region):
                    # Fill the enclosed region with blue (1)
                    for r, c in region:
                        output_grid[r, c] = 1

    return output_grid