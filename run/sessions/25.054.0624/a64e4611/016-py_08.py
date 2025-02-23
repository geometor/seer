"""
1.  **Identify Red Objects:** Locate all connected regions of red (2) pixels in the input grid.  These define the boundaries.
2.  **Identify White Regions:**  Locate all connected regions of white (0) pixels.
3.  **Fill Enclosed White Regions:** For each white region, determine if it's fully enclosed by red pixels (using 8-connectivity). If a white region is fully enclosed, change all pixels in that region to green (3).
"""

import numpy as np
from scipy.ndimage import label, measurements

def get_connected_regions(grid, color):
    """
    Finds connected regions of a specific color in the grid.

    Args:
        grid: A 2D numpy array representing the grid.
        color: The color to find connected regions for.

    Returns:
        A list of tuples, where each tuple contains the (row, col) coordinates
        of pixels belonging to a connected region of the specified color.
        Also return the labeled array, where each region is a unique integer,
        and the number of regions
    """
    colored_pixels = (grid == color)
    labeled_array, num_features = label(colored_pixels)
    regions = []
    for i in range(1, num_features + 1):  # Iterate through each labeled region
        region_pixels = np.where(labeled_array == i)
        regions.append(list(zip(region_pixels[0], region_pixels[1])))
    return regions, labeled_array, num_features

def is_enclosed(region, labeled_array, boundary_color, grid_shape):
    """
    Checks if a region is fully enclosed by a boundary color.

    Args:
      region: list of (row, col) of the region to check
      labeled_array: labeled array from the connected regions
      boundary_color:  color of the boundary
      grid_shape: (height, width)

    Returns:
        True if the region is fully enclosed, False otherwise.
    """

    rows, cols = zip(*region)  # Unzip the coordinates
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    # Check if the region touches the edges of the grid
    if min_row == 0 or max_row == grid_shape[0] - 1 or min_col == 0 or max_col == grid_shape[1] - 1:
      return False

    # Check all neighboring pixels around the *bounding box* of the region
    for r in range(min_row - 1, max_row + 2):
        for c in range(min_col - 1, max_col + 2):
          # skip the inside of the bounding box, we only care about the perimeter
            if min_row <= r <= max_row and min_col <=c <= max_col:
              continue

            # Check boundaries - if out of grid, or not red.
            if (0 <= r < grid_shape[0] and 0 <= c < grid_shape[1]):
                if labeled_array[r, c] != boundary_color:
                  
                  return False
            
    return True
  

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    grid_shape = input_grid.shape

    # Get red regions
    red_regions, red_labeled_array, red_num_features = get_connected_regions(input_grid, 2)

    # Label the entire red-colored area (all red regions combined) with a single label '2'
    red_combined_mask = (input_grid == 2)
    red_labeled_combined, _ = label(red_combined_mask) #we do not care about number of objects
    
    # Get white regions
    white_regions, white_labeled_array, white_num_features = get_connected_regions(input_grid, 0)

    # Fill enclosed white regions
    for white_region in white_regions:
        # Check if enclosed by red using the combined red labeled array
        if is_enclosed(white_region, red_labeled_combined, 2, grid_shape):
            for r, c in white_region:
                output_grid[r, c] = 3

    return output_grid