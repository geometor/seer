"""
1.  **Identify Maroon Regions:** Locate all contiguous regions of maroon (color value 9) pixels within the input grid.
2.  **Check for enclosed objects:** For each maroon region, check if it contains pixels of any color other than maroon.
3.  **Conditional Removal:** If a maroon region contains other colors, change all pixels *within that maroon region* to white (color value 0).
4. **Preserve other pixels:** If a maroon region contains *only* the color maroon, it is not modified. All other pixels in the input grid remain unchanged.
"""

import numpy as np
from scipy.ndimage import label

def find_regions(grid, color_value):
    """
    Finds all contiguous regions of a specific color in a grid.

    Args:
        grid: The input grid (NumPy array).
        color_value: The color value to search for.

    Returns:
        A labeled array where each region has a unique integer label, and the number of features.
    """
    colored_pixels = (grid == color_value).astype(int)
    labeled_array, num_features = label(colored_pixels)
    return labeled_array, num_features

def has_other_colors(grid, region_mask):
    """
    Checks if a region contains colors other than its primary color.

    Args:
        grid: The input grid (NumPy array).
        region_mask: A boolean mask representing the region.

    Returns:
        True if the region contains colors other than the primary color, False otherwise.
    """
    region_pixels = grid[region_mask]
    unique_colors = np.unique(region_pixels)
    return len(unique_colors) > 1

def transform(input_grid):
    """
    Transforms the input grid by removing maroon (9) regions that contain other colors.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find all maroon regions
    maroon_labeled_array, num_maroon_regions = find_regions(input_grid, 9)

    # Iterate through each maroon region
    for region_label in range(1, num_maroon_regions + 1):
        region_mask = (maroon_labeled_array == region_label)
        # Check if the region contains other colors
        if has_other_colors(input_grid, region_mask):
            # Remove the region by setting it to white (0)
            output_grid[region_mask] = 0

    return output_grid