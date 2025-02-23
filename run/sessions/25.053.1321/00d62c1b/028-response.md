# 00d62c1b • 028 • refine_coder

---
```python
"""
Identifies contiguous green areas. Within each area, the "interior" green pixels (those whose removal would not disconnect the area) are recolored to yellow.
"""

import numpy as np
from scipy.ndimage import label, generate_binary_structure

def get_contiguous_regions(grid, color):
    """
    Finds contiguous regions of a specific color in the grid.
    Returns a list of masks, one for each region.
    """
    color_mask = (grid == color)
    labeled_array, num_features = label(color_mask)
    regions = []
    for i in range(1, num_features + 1):  # Iterate through each labeled region
        regions.append(labeled_array == i)
    return regions

def is_interior(region_mask, row, col):
    """
    Checks if removing the pixel at (row, col) would disconnect the region.
    """
    # Create a copy of the mask and remove the pixel
    temp_mask = region_mask.copy()
    temp_mask[row, col] = False

    # Label the remaining pixels
    labeled_array, num_features = label(temp_mask)

    # If the number of features increased, it's an interior pixel
    return num_features == 1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all contiguous green regions
    green_regions = get_contiguous_regions(input_grid, 3)

    # change output pixels
    for region_mask in green_regions:
        for r in range(rows):
            for c in range(cols):
                if region_mask[r, c]:  # If it's part of the current green region
                    if is_interior(region_mask, r, c):
                        output_grid[r, c] = 4 # Change to yellow

    return output_grid
```
