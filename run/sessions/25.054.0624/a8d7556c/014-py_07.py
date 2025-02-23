"""
Identify white (0) pixels in the input grid.
Selectively change some of these white pixels to red (2).
The selection appears to be sparse and only within regions of connected white pixels; not all white pixels are changed.
"""

import numpy as np

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

from scipy import ndimage

def transform(input_grid):
    """
    Transforms the input grid by selectively changing some white pixels to red.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Get connected white regions
    white_regions = get_white_regions(output_grid)


    # Selectively change some white pixels to red within each region
    for region in white_regions:
        if len(region)>2:

            # very naive selection - just pick one, but we can't be sure
            # we need more data
            selected_pixels = [region[1], region[2]]

            for r, c in selected_pixels:
                 output_grid[r, c] = 2

    return output_grid