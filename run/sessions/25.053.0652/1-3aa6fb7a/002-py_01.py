"""
The transformation rule is to find the center-most azure pixel in the input grid and change its color to blue.
"""

import numpy as np

def find_azure_pixels(grid):
    # Find the coordinates of all azure pixels (color 8).
    return np.argwhere(grid == 8)

def transform(input_grid):
    """
    Transforms the input grid by changing the center-most azure pixel to blue.
    """
    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)

    # Find all azure pixels.
    azure_pixels = find_azure_pixels(output_grid)

    # If there are no azure pixels, return the original grid.
    if len(azure_pixels) == 0:
        return output_grid

    # Calculate the centroid of the azure pixels.
    centroid = np.mean(azure_pixels, axis=0)

    # Find the azure pixel closest to the centroid.
    distances = np.sqrt(np.sum((azure_pixels - centroid)**2, axis=1))
    closest_pixel_index = np.argmin(distances)
    closest_pixel = azure_pixels[closest_pixel_index]

    # Change the color of the closest pixel to blue (color 1).
    output_grid[closest_pixel[0], closest_pixel[1]] = 1

    return output_grid