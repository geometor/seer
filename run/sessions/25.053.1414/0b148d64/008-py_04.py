"""
1.  **Identify Regions:** Locate the contiguous green (3) region (region_2) in the bottom-right part of the input grid. Note the boundary positions (top and left) of this region.
2.  **Crop:** Define a rectangular cropping area. The top-left corner of this rectangle is the minimum x, y position of the green region, i.e., a pixel with value 3. The dimensions of the cropped region are calculated by the size of the green region itself.
3.  **Filter:** Within the cropped region, retain only the green (3) and white (0) pixels. Remove all red (2) pixels.
4.  **Output:** The resulting filtered and cropped region is the output.
"""

import numpy as np

def find_object(grid, color):
    # Find coordinates of all pixels with the specified color.
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None  # Handle the case where the color is not found.
    min_y, min_x = coords.min(axis=0)
    max_y, max_x = coords.max(axis=0)
    return (min_x, min_y), (max_x, max_y)

def transform(input_grid):
    # Convert input to numpy array for easier manipulation.
    input_grid = np.array(input_grid)

    # Find the bounding box of the green region (color 3).
    green_region_bounds = find_object(input_grid, 3)
    
    if green_region_bounds is None:
      return [] # Return an empty grid

    (min_x, min_y), (max_x, max_y) = green_region_bounds

    # Crop the grid to the green region's bounding box.
    cropped_grid = input_grid[min_y:max_y+1, min_x:max_x+1]

    # Filter out the red pixels (color 2) within the cropped region.
    output_grid = np.where(cropped_grid == 2, 0, cropped_grid)

    return output_grid.tolist()