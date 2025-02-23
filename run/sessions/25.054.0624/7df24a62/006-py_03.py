"""
1. Identify all Blue Regions: Find *all* contiguous blue (1) regions in the input grid, considering diagonal connections.
2. Determine Bounding Boxes: For *each* blue region, calculate its bounding box (min/max rows and columns).
3. Fill Regions: For *each* blue region:
    *   Iterate through all pixels within the bounding box of that blue region.
    *   Change *all* pixels within the current bounding box to blue (1), including yellow pixels.
4. Preserve other colors outside of the box: Iterate through all pixels in the entire grid. If the source pixel is not 1 (blue) or 4 (yellow), then restore the pixel in the destination grid.
"""

import numpy as np
from scipy.ndimage import label

def find_all_blue_regions(grid):
    # Use 8-connectivity to include diagonals
    labeled_grid, num_regions = label(grid == 1, structure=np.array([[1,1,1],[1,1,1],[1,1,1]]))
    regions = []
    for i in range(1, num_regions + 1):
        coords = np.argwhere(labeled_grid == i)
        min_row = np.min(coords[:, 0])
        max_row = np.max(coords[:, 0])
        min_col = np.min(coords[:, 1])
        max_col = np.max(coords[:, 1])
        regions.append(((min_row, max_row, min_col, max_col), coords))
    return regions

def transform(input_grid):
    # Initialize output_grid as a copy of input
    output_grid = input_grid.copy()

    # Find all blue regions with diagonal connectivity
    blue_regions = find_all_blue_regions(input_grid)

    # Fill each bounding box with blue
    for (min_row, max_row, min_col, max_col), _ in blue_regions:
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                output_grid[row, col] = 1

    return output_grid