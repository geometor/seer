"""
The transformation rule identifies the contiguous object formed by the non-white color (the "bounding object") and outputs only the white pixels that are completely enclosed within this object.  All other pixels, including the bounding object itself, are set to white (0) in the output grid.
"""

import numpy as np
from scipy.ndimage import label

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of the specified color in the grid."""
    colored_pixels = (grid == color).astype(int)
    labeled_array, num_features = label(colored_pixels)
    regions = []
    for i in range(1, num_features + 1):
        region = np.argwhere(labeled_array == i)
        regions.append(region.tolist())
    return regions

def is_enclosed(region, bounding_object_coords, grid_shape):
    """
    Checks if a region is fully enclosed by the bounding object.
    """
    rows, cols = grid_shape
    region_arr = np.array(region)

    # Check if any part of region is on edge of grid
    if (np.any(region_arr[:, 0] == 0) or
        np.any(region_arr[:, 0] == rows - 1) or
        np.any(region_arr[:, 1] == 0) or
        np.any(region_arr[:, 1] == cols - 1)):
        return False


    #Check all directions around region
    for coord in region:
       row,col = coord
       
       #Check N
       if [row - 1,col] not in bounding_object_coords and [row-1, col] not in region:
          return False
          
       #Check S
       if [row + 1,col] not in bounding_object_coords and [row + 1,col] not in region:
          return False
          
       #Check W
       if [row,col - 1] not in bounding_object_coords and [row,col - 1] not in region:
          return False       
          
       #Check E   
       if [row,col + 1] not in bounding_object_coords and [row,col + 1] not in region:
          return False             
    return True

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Determine the bounding color (the non-white color)
    unique_colors = np.unique(input_grid)
    bounding_color = [color for color in unique_colors if color != 0][0]

    # Find coordinates of the bounding object
    bounding_object_coords = np.argwhere(input_grid == bounding_color).tolist()

    # Find all white regions
    white_regions = find_contiguous_regions(input_grid, 0)

    # Identify enclosed white regions
    enclosed_regions = []
    for region in white_regions:
        if is_enclosed(region, bounding_object_coords, input_grid.shape):
            enclosed_regions.append(region)

    # Set the pixels of the enclosed regions to white (0) in the output grid.
    for region in enclosed_regions:
        for row, col in region:
            output_grid[row, col] = 0

    return output_grid.tolist()