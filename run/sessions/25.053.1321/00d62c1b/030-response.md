# 00d62c1b • 030 • refine_coder

---
```python
"""
1. Identify Contiguous Green Regions: Find all distinct, connected areas where pixels are green (value 3). Connectivity includes diagonals (8-connectivity).
2. Identify Interior Pixels: Within each identified green region, locate the "interior" green pixels. A green pixel is considered "interior" if all eight of its neighboring pixels (up, down, left, right, and the four diagonals) are either:
    * Also green pixels.
    * Outside the bounds of the grid (edge or corner pixels).
3. Recolor Interior Pixels: Change the color of all identified interior green pixels to yellow (value 4).
4. Leave other pixels unchanged: All pixels which are not interior green pixels are not modified.
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
    Checks if a pixel is an interior pixel within a region.
    """
    rows, cols = grid.shape

    # Check if the pixel is within the region
    if not region_mask[row, col]:
        return False

    # Check all 8 neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:  # Skip the pixel itself
                continue

            r, c = row + dr, col + dc

            # Check if the neighbor is within grid bounds
            if 0 <= r < rows and 0 <= c < cols:
                # Check if the neighbor is NOT part of the region or is a different color
                if not region_mask[r,c]:
                    return False  # Not an interior pixel
            # else: neighbor is outside grid, which is okay for an interior pixel

    return True  # All neighbors are either green or out of bounds


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
```
