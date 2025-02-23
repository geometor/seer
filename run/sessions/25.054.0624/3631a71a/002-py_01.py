"""
1.  **Identify the target region:** Find the largest contiguous region of maroon (color value 9) pixels within the input grid.
2.  **Remove the region:** Change the color value of all pixels within the identified maroon region to white (color value 0).
3.  **Preserve the rest:** All other pixels in the grid remain unchanged.
"""

import numpy as np
from scipy.ndimage import label

def find_largest_contiguous_region(grid, color_value):
    """
    Finds the largest contiguous region of a specific color in a grid.

    Args:
        grid: The input grid (NumPy array).
        color_value: The color value to search for.

    Returns:
        A mask representing the largest contiguous region, or None if no region of the specified color is found.
    """
    colored_pixels = (grid == color_value).astype(int)
    labeled_array, num_features = label(colored_pixels)
    
    if num_features == 0:
        return None
    
    sizes = np.bincount(labeled_array.ravel())
    largest_label = np.argmax(sizes[1:]) + 1  # +1 because 0 is the background
    largest_region_mask = (labeled_array == largest_label)
    return largest_region_mask

def transform(input_grid):
    """
    Transforms the input grid by removing the largest contiguous region of maroon (9) pixels.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the largest contiguous region of maroon pixels
    maroon_mask = find_largest_contiguous_region(input_grid, 9)

    # change output pixels 
    if maroon_mask is not None:
      output_grid[maroon_mask] = 0

    return output_grid