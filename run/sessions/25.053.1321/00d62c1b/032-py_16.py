"""
1.  **Identify Green Regions:** Find all distinct, contiguous regions of green (value 3) pixels in the input grid. Diagonal connections count as being contiguous (8-connectivity).

2.  **Determine Interior Pixels:** For each green region:
    - Iterate over all pixels in region.
    - a pixel is considered an "interior pixel" if it is a green pixel and part of current region.

3.  **Recolor Interior Pixels:** Change the color of all identified interior green pixels to yellow (value 4).

4.  **Output:** Return the modified grid. All pixels that are not "interior green pixels" should remain unchanged.
"""

import numpy as np
from scipy.ndimage import label

def get_contiguous_regions(grid, color):
    """
    Finds contiguous regions of a specific color in the grid.
    Returns a list of masks, one for each region.
    """
    color_mask = (grid == color)
    labeled_array, num_features = label(color_mask, structure=np.array([[1,1,1],[1,1,1],[1,1,1]]))  # 8-connectivity
    regions = []
    for i in range(1, num_features + 1):
        regions.append(labeled_array == i)
    return regions

def is_interior_pixel(grid, row, col, region_mask):
    """
    Checks if a pixel is an interior pixel within a region.  Simplified to just check if it's part of the region and the correct color.
    """
    # Check if within region boundaries and green
    return region_mask[row, col] and grid[row,col] == 3


def transform(input_grid):
    """
    Transforms the input grid by identifying contiguous green regions and
    recoloring interior green pixels to yellow.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all contiguous green regions
    green_regions = get_contiguous_regions(input_grid, 3)

    # change output pixels
    for region_mask in green_regions:
        for r in range(rows):
            for c in range(cols):
                if is_interior_pixel(input_grid, r, c, region_mask):
                    output_grid[r, c] = 4  # Change to yellow

    return output_grid