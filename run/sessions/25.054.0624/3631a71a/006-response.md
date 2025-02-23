# 3631a71a • 006 • refine_coder

---
```python
"""
1.  **Identify Maroon Regions:** Locate all contiguous regions of maroon (color value 9) pixels within the input grid.
2.  **Check for Enclosed Regions:** For each maroon region, determine if it *completely encloses* one or more regions of a different color.  "Completely encloses" means that if you expand the non-maroon region slightly, the boundary of that expanded region is entirely within the maroon region.
3.  **Conditional Removal:** If a maroon region fully encloses other colored regions, change all pixels *within that maroon region* to white (color value 0).
4.  **Preserve Other Pixels:** Maroon regions that do not fully enclose other colors are not modified. All other pixels remain unchanged.
"""

import numpy as np
from scipy.ndimage import label, binary_dilation, binary_erosion, generate_binary_structure

def find_regions(grid, color_value):
    """
    Finds contiguous regions of a specific color.
    """
    colored_pixels = (grid == color_value).astype(int)
    labeled_array, num_features = label(colored_pixels)
    return labeled_array, num_features

def is_fully_enclosed(grid, maroon_mask):
    """
    Checks if a maroon region fully encloses other colors.
    """
    # Get the inverse of the maroon mask (everything *but* the maroon)
    non_maroon_mask = ~maroon_mask

    # If the maroon region is on the edge, it can't fully enclose
    if np.any(maroon_mask[0, :]) or np.any(maroon_mask[-1, :]) or \
       np.any(maroon_mask[:, 0]) or np.any(maroon_mask[:, -1]):
        return False

    # Label the non-maroon regions
    labeled_non_maroon, num_non_maroon = label(non_maroon_mask)

    # Iterate through each non-maroon region *within* the bounding box of the maroon region
    min_row, min_col = np.min(np.where(maroon_mask)[0]), np.min(np.where(maroon_mask)[1])
    max_row, max_col = np.max(np.where(maroon_mask)[0]), np.max(np.where(maroon_mask)[1])

    for region_label in range(1, num_non_maroon + 1):
        region_mask = (labeled_non_maroon == region_label)

        # Check if this non-maroon region intersects with the current maroon region's bounding box
        if np.any(region_mask[min_row:max_row+1, min_col:max_col+1]):
            # Expand the non-maroon region slightly
            struct = generate_binary_structure(2, 2)  # 3x3 structuring element
            expanded_region = binary_dilation(region_mask, structure=struct, border_value=0)

            # Check if the boundary of the expanded region is entirely within the maroon region
            boundary_mask = expanded_region ^ binary_erosion(expanded_region, structure=struct, border_value=0)
            if not np.all(grid[boundary_mask] == 9):
                return False  # Not fully enclosed

    return True # if all non-maroon regions inside bounding box pass check


def transform(input_grid):
    """
    Transforms grid, removing maroon regions enclosing other colors.
    """
    output_grid = np.copy(input_grid)
    maroon_labeled_array, num_maroon_regions = find_regions(input_grid, 9)

    for region_label in range(1, num_maroon_regions + 1):
        region_mask = (maroon_labeled_array == region_label)
        if is_fully_enclosed(input_grid, region_mask):
            output_grid[region_mask] = 0

    return output_grid
```
