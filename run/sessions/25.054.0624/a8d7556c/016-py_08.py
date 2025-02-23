"""
Identify all connected regions of white (0) pixels.
For each white region with more than two pixels:
    Change white pixels to red (2) if they are directly adjacent (up, down, left, or right, *not diagonal*) to a gray (5) pixel.
Leave all other pixels unchanged.
"""

import numpy as np
from scipy import ndimage

def get_white_regions(grid):
    """
    Finds and returns a list of connected white regions in the grid.
    """
    white_pixels = (grid == 0)
    labeled_grid, num_labels = ndimage.label(white_pixels)
    regions = []
    for i in range(1, num_labels + 1):
        region = np.where(labeled_grid == i)
        regions.append(list(zip(region[0], region[1])))
    return regions

def is_adjacent_to_gray(grid, r, c):
    """
    Checks if a pixel at (r, c) is adjacent to a gray (5) pixel.
    """
    rows, cols = grid.shape
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 5:
            return True
    return False

def transform(input_grid):
    """
    Transforms the input grid by selectively changing white pixels to red based on adjacency to gray pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Get connected white regions
    white_regions = get_white_regions(output_grid)

    # Change white pixels to red if adjacent to gray
    for region in white_regions:
        if len(region) > 2:
            for r, c in region:
                if is_adjacent_to_gray(output_grid, r, c):
                    output_grid[r, c] = 2

    return output_grid