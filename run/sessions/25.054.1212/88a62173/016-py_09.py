"""
The transformation reduces a checkerboard-like input grid to a 2x2 output grid. It determines the color of each output pixel by analyzing the color frequencies within corresponding quadrants of the input grid.
"""

import numpy as np
from collections import Counter

def get_quadrant(grid, row_start, row_end, col_start, col_end):
    """Helper function to extract a quadrant from the grid."""
    return grid[row_start:row_end, col_start:col_end]

def get_dominant_colors(grid):
    """Helper function to get the two most frequent colors"""
    counts = Counter(grid.flatten())
    most_common = counts.most_common(2)  # Get the two most common
    colors = [color for color, count in most_common]
    
    # ensure that 2 colors are returned if possible
    while len(colors) < 2:
        colors.append(0) # Use 0 as a default fill if needed

    return colors[:2]

def transform(input_grid):
    # initialize output_grid as 2x2 numpy array with zeros
    output_grid = np.zeros((2, 2), dtype=int)

    # get input grid dimensions
    rows, cols = input_grid.shape

    # calculate midpoints for quadrant division
    row_mid = (rows + 1) // 2  # Integer division, rounding up for center
    col_mid = (cols + 1) // 2

    # Determine the overall dominant color of the input grid
    overall_dominant_colors = get_dominant_colors(input_grid)
    overall_dominant_color = overall_dominant_colors[0]


    # Process each quadrant
    quadrants = [
        (0, row_mid, 0, col_mid),          # Top-left
        (0, row_mid, col_mid, cols),       # Top-right
        (row_mid, rows, 0, col_mid),       # Bottom-left
        (row_mid, rows, col_mid, cols)  # Bottom-right
    ]

    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = get_quadrant(input_grid, row_start, row_end, col_start, col_end)
        quadrant_dominant_colors = get_dominant_colors(quadrant)

        # apply logic to get pixel
        if overall_dominant_color in quadrant_dominant_colors:
            output_grid[i // 2, i % 2] = overall_dominant_color
        else:
            output_grid[i // 2, i % 2] = quadrant_dominant_colors[0] if quadrant_dominant_colors[0] != overall_dominant_color else quadrant_dominant_colors[1]


    return output_grid