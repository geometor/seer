"""
1.  **Identify the Green Shape:** Locate all pixels with the value 3 (green) that form a contiguous shape.
2.  **Find the Center:** Determine the "center" of the green shape. based on the example:
    + find green pixel at the center of the height of the shape
    + then find the center of those
3.  **Change Color:** Change the color of the center-most green pixel to 4 (yellow).
"""

import numpy as np

def find_green_shape(grid):
    # Find all green pixels (value 3)
    green_pixels = np.argwhere(grid == 3)
    return green_pixels

def find_center_pixel(green_pixels):
    # find the center of the height
    min_row = np.min(green_pixels[:, 0])
    max_row = np.max(green_pixels[:, 0])
    center_row = (min_row + max_row) // 2
    
    pixels_at_center_row = green_pixels[green_pixels[:,0] == center_row]
    
    # find the center of the col
    min_col = np.min(pixels_at_center_row[:, 1])
    max_col = np.max(pixels_at_center_row[:, 1])
    center_col = (min_col + max_col) // 2
    

    center_pixel = [center_row, center_col]
    
    
    return center_pixel

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the green shape
    green_shape = find_green_shape(output_grid)

    # Find the center pixel of the green shape
    center_pixel = find_center_pixel(green_shape)

    # Change the color of the center pixel to yellow (4)
    output_grid[center_pixel[0], center_pixel[1]] = 4

    return output_grid