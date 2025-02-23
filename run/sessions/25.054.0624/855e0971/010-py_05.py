"""
The grid is divided into regions. White pixels within a region act as seeds. From each white seed, the white color spreads to all connected pixels of the region's original color, stopping at the region's boundary.
"""

import numpy as np

def get_regions(grid):
    # Divide the grid into regions based on the first row's color changes.
    regions = []
    start_col = 0
    current_color = grid[0, 0]
    for col in range(1, grid.shape[1]):
        if grid[0, col] != current_color:
            regions.append(((start_col, 0, col - start_col, grid.shape[0]), current_color))
            current_color = grid[0, col]
            start_col = col
    regions.append(((start_col, 0, grid.shape[1] - start_col, grid.shape[0]), current_color))  # Add the last region
    return regions

def flood_fill(grid, start_row, start_col, target_color, replacement_color, region_bounds):
    # Perform a flood fill, staying within the given region.
    x_start, y_start, width, height = region_bounds
    queue = [(start_row, start_col)]
    while queue:
        row, col = queue.pop(0)
        if not (x_start <= col < x_start + width and y_start <= row < y_start + height):
            continue #out of bounds
        if grid[row, col] == target_color:
            grid[row, col] = replacement_color
            if row > 0:
                queue.append((row - 1, col)) #up
            if row < grid.shape[0] - 1:
                queue.append((row + 1, col)) #down
            if col > 0:
                queue.append((row, col - 1))  # Left
            if col < grid.shape[1] - 1:
                queue.append((row, col + 1))  # Right

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    regions = get_regions(input_grid)

    # change output pixels
    for region, region_color in regions:
        x_start, y_start, width, height = region
        for row in range(y_start, y_start + height):
            for col in range(x_start, x_start + width):
                if input_grid[row, col] == 0:  # Found a white pixel
                    flood_fill(output_grid, row, col, region_color, 0, region)

    return output_grid