"""
1.  **Identify Azure Pixels:** Locate all pixels with the color azure (8) within the input grid.
2.  **Calculate Centroid:** If there are azure pixels, compute the centroid (average row and column index) of these pixels.
3.  **Find Nearest Azure Pixel:** Determine the azure pixels that are closest to the calculated centroid. Use Euclidean distance to measure closeness.
4. **Change all "central" pixels:** For *all* pixels closest to the average row/column, change the pixel color from azure (8) to blue (1).
"""

import numpy as np

def get_azure_pixels(grid):
    # Find coordinates of all azure (8) pixels
    return np.argwhere(grid == 8)

def calculate_centroid(pixels):
    # Calculate the average row and column index
    return np.mean(pixels, axis=0)

def find_nearest_azure_pixels(centroid, azure_pixels):
    # Calculate Euclidean distances to the centroid
    distances = np.sqrt(np.sum((azure_pixels - centroid)**2, axis=1))
    # Find the minimum distance
    min_distance = np.min(distances)
    # Return all pixels with the minimum distance to centroid
    return azure_pixels[distances == min_distance]

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find all azure pixels
    azure_pixels = get_azure_pixels(input_grid)

    if azure_pixels.size > 0:
        # Calculate the centroid of the azure pixels
        centroid = calculate_centroid(azure_pixels)

        # Find the nearest azure pixel(s) to the centroid
        central_pixels = find_nearest_azure_pixels(centroid, azure_pixels)

        # Change the color of the central pixel(s) to blue (1)
        for pixel in central_pixels:
            output_grid[pixel[0], pixel[1]] = 1

    return output_grid