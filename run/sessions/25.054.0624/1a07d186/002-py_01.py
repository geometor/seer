"""
Transforms an input grid by preserving green and yellow pixels that are part of vertical lines and are adjacent to each other.
Other pixels are set to white (0).
"""

import numpy as np

def find_vertical_lines(grid, color):
    lines = []
    rows, cols = grid.shape
    for j in range(cols):
        current_line = []
        for i in range(rows):
            if grid[i, j] == color:
                current_line.append((i, j))
            else:
                if len(current_line) > 0:
                    lines.append(current_line)
                    current_line = []
        if len(current_line) > 0:
            lines.append(current_line)
    return lines

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid, filled with white (0).
    output_grid = np.zeros_like(input_grid)

    # Find vertical lines of green (3) and yellow (4) pixels.
    green_lines = find_vertical_lines(input_grid, 3)
    yellow_lines = find_vertical_lines(input_grid, 4)
    
    # Flatten lists of lines into lists of pixels
    green_pixels = [pixel for line in green_lines for pixel in line]
    yellow_pixels = [pixel for line in yellow_lines for pixel in line]


    # Iterate through green pixels and check for adjacent yellow pixels.
    for (row, col) in green_pixels:
        if (row, col + 1) in yellow_pixels:
            output_grid[row, col] = 3

    # Iterate through yellow pixels and check for adjacent green pixels.
    for (row, col) in yellow_pixels:
         if (row, col - 1) in green_pixels:
            output_grid[row, col] = 4

    return output_grid