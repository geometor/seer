"""
1.  Identify Azure Objects: Find all contiguous groups of azure (8) colored pixels. Each group is considered a separate object.

2.  Find Top-Left Pixels: For each identified azure object:
    *   Find all pixels that are at the highest row (minimum row value).
    *   Among these, select the pixel(s) furthest to the left (minimum column value).
    *   Change the color of pixel to blue.

3.  Find Top-Right Pixels: For each identified azure object:
    * Find all pixels that are at the highest row (minimum row value).
    * Among these, select the pixel(s) furthest to the right (maximum column value).
    * Change the color of pixel to blue.

4.  Output: The output grid is a copy of the input grid, but with the top-left and top-right pixels (as defined above) of all azure objects are changed to blue (1).
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_top_left_pixel(object_pixels):
    min_row = min(pixel[0] for pixel in object_pixels)
    top_pixels = [pixel for pixel in object_pixels if pixel[0] == min_row]
    min_col = min(pixel[1] for pixel in top_pixels)
    top_left_pixel = [pixel for pixel in top_pixels if pixel[1] == min_col][0]
    return top_left_pixel

def find_top_right_pixel(object_pixels):
    min_row = min(pixel[0] for pixel in object_pixels)
    top_pixels = [pixel for pixel in object_pixels if pixel[0] == min_row]
    max_col = max(pixel[1] for pixel in top_pixels)
    top_right_pixel = [pixel for pixel in top_pixels if pixel[1] == max_col][0]
    return top_right_pixel


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Change the color of the top-left and top-right pixel of each azure object to blue
    for obj in azure_objects:
        if len(obj) > 1:
            top_left_pixel = find_top_left_pixel(obj)
            output_grid[top_left_pixel]=1
            top_right_pixel = find_top_right_pixel(obj)
            output_grid[top_right_pixel]=1

    return output_grid