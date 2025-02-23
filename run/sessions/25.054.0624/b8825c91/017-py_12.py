"""
The transformation preserves the outermost ring of a diamond shape centered in the grid. 
Within the diamond, excluding the outer ring, colors are shifted inward: 
colors in the second ring are replaced by those in the third, 
the third by the fourth, and so on.
"""

import numpy as np

def find_diamond_center(grid):
    # Find the center of the grid
    center_row, center_col = grid.shape[0] // 2, grid.shape[1] // 2
    return center_row, center_col

def is_inside_diamond(row, col, center_row, center_col, size):
    # Determine if a given cell is within the diamond
    dist_row = abs(row - center_row)
    dist_col = abs(col - center_col)
    return dist_row + dist_col <= size

def get_diamond_size(grid):
    # Determine the maximum size (radius) of the diamond
    center_row, center_col = find_diamond_center(grid)
    max_size = min(center_row, center_col)
    return max_size

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    center_row, center_col = find_diamond_center(input_grid)
    size = get_diamond_size(input_grid)

    # Iterate through rings within the diamond, starting from the second outermost
    for ring in range(1, size):  # ring 0 is outside, size is the center
        for row in range(input_grid.shape[0]):
            for col in range(input_grid.shape[1]):
                if is_inside_diamond(row, col, center_row, center_col, size - ring) and not is_inside_diamond(row, col, center_row, center_col, size - ring - 1):
                  #if the pixel it's in the current ring
                    # find source color for substitution
                    for source_row in range(input_grid.shape[0]):
                        for source_col in range(input_grid.shape[1]):
                            if is_inside_diamond(source_row, source_col, center_row, center_col, size - ring -1) and not is_inside_diamond(source_row, source_col, center_row, center_col, size - ring - 2):
                                #if the pixel is one ring inside
                                output_grid[row,col] = input_grid[source_row, source_col]


    return output_grid