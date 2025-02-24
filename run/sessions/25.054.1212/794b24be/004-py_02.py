"""
1. Identify all blue pixels: Find all pixels in the input grid that have a value of 1 (blue).
2. Bounding Box: Determine the smallest rectangle that contains all the blue pixels. This can be defined by the minimum and maximum row and column indices of the blue pixels.
3. Construct the output grid: change the color of the blue pixels from blue to red and move the rectangle formed to the top-left corner of the output grid. The rest of the pixels in output grid are 0.
"""

import numpy as np

def find_blue_pixels(grid):
    # Find the indices of all blue (1) pixels
    return np.where(grid == 1)

def bounding_box(coords):
    # Calculate the bounding box
    min_row, min_col = np.min(coords[0]), np.min(coords[1])
    max_row, max_col = np.max(coords[0]), np.max(coords[1])
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    # Find all blue pixels
    blue_pixels = find_blue_pixels(input_grid)

    # if no blue pixels return all 0 grid.
    if len(blue_pixels[0]) == 0:
      return np.zeros_like(input_grid)

    # Determine the bounding box
    (min_row, min_col), (max_row, max_col) = bounding_box(blue_pixels)

    # Calculate output grid size
    output_height = max_row - min_row + 1
    output_width = max_col - min_col + 1

    # Initialize the output grid
    output_grid = np.zeros((output_height, output_width), dtype=int)
    
    # change to red and move to top-left of the output grid
    for i in range(len(blue_pixels[0])):
        row = blue_pixels[0][i]
        col = blue_pixels[1][i]
        output_grid[row - min_row, col - min_col] = 2


    return output_grid