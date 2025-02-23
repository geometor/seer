# a64e4611 • 018 • refine_coder

---
```python
"""
1.  **Identify Red Regions:** Find all contiguous regions of red (2) pixels in the input grid. These regions define the potential boundaries.
2.  **Identify White Regions:** Find all contiguous regions of white (0) pixels.
3.  **Check for Enclosure:** For each white region:
    *   Examine *all* pixels adjacent to the white region, including diagonals (8-connectivity).
    *   If *any* of these adjacent pixels are *not* red (2), the white region is *not* enclosed.
    *   If *all* adjacent pixels are red (2), the white region *is* enclosed.
4.  **Fill Enclosed Regions:** Change all pixels within enclosed white regions to green (3).
"""

import numpy as np
from scipy.ndimage import label

def get_connected_regions(grid, color):
    """
    Finds connected regions of a specific color in the grid.

    Args:
        grid: A 2D numpy array representing the grid.
        color: The color to find connected regions for.

    Returns:
        A list of tuples, where each tuple contains the (row, col) coordinates
        of pixels belonging to a connected region of the specified color.
    """
    colored_pixels = (grid == color)
    labeled_array, num_features = label(colored_pixels)
    regions = []
    for i in range(1, num_features + 1):  # Iterate through each labeled region
        region_pixels = np.where(labeled_array == i)
        regions.append(list(zip(region_pixels[0], region_pixels[1])))
    return regions

def is_enclosed(region, grid, boundary_color):
    """
    Checks if a region is fully enclosed by a boundary color using 8-connectivity.

    Args:
        region: A list of (row, col) tuples representing the region.
        grid: The 2D numpy array representing the grid.
        boundary_color: The color that should enclose the region.

    Returns:
        True if the region is fully enclosed, False otherwise.
    """
    rows, cols = zip(*region)
    grid_height, grid_width = grid.shape

    for row, col in region:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip the current pixel itself

                nr, nc = row + dr, col + dc

                # Check boundaries and if the neighbor is the boundary color
                if 0 <= nr < grid_height and 0 <= nc < grid_width:
                    if grid[nr, nc] != boundary_color:
                        return False  # Not enclosed if a neighbor isn't the boundary color
                elif (nr < 0 or nr >= grid_height) or (nc < 0 or nc >= grid_width):
                  # if any of the region is on the border, it cannot be enclosed
                  return False

    return True  # Enclosed if all neighbors are the boundary color


def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    grid_shape = input_grid.shape

    # Get white regions
    white_regions = get_connected_regions(input_grid, 0)

    # Fill enclosed white regions
    for white_region in white_regions:
        if is_enclosed(white_region, input_grid, 2):
            for r, c in white_region:
                output_grid[r, c] = 3

    return output_grid
```
