"""
The grid is divided into regions based on color changes in the first row. Within each region, all connected pixels, starting from any white pixel and including other white pixels, are changed to white. The flood fill stops at the region boundaries.
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

def flood_fill(grid, start_row, start_col, region_bounds):
    # Perform a flood fill within the given region, propagating through white pixels.
    x_start, y_start, width, height = region_bounds
    queue = [(start_row, start_col)]
    while queue:
        row, col = queue.pop(0)
        if not (x_start <= col < x_start + width and y_start <= row < y_start + height):
            continue  # Out of bounds

        if grid[row, col] != 0:  #if pixel is not already white
           grid[row,col] = 0 #change pixel to white


        # Check neighbors
        if row > 0 and grid[row-1,col]!=0:
                queue.append((row - 1, col))
        if row < grid.shape[0] - 1 and grid[row+1, col] !=0:
                queue.append((row + 1, col))
        if col > 0 and grid[row,col-1] !=0:
                queue.append((row, col - 1))
        if col < grid.shape[1] - 1 and grid[row, col+1]!=0:
                queue.append((row, col + 1))
        #also add neighbors if they are white to the queue.
        if row > 0 and grid[row-1,col]==0:
                queue.append((row - 1, col))
        if row < grid.shape[0] - 1 and grid[row+1, col] ==0:
                queue.append((row + 1, col))
        if col > 0 and grid[row,col-1] ==0:
                queue.append((row, col - 1))
        if col < grid.shape[1] - 1 and grid[row, col+1]==0:
                queue.append((row, col + 1))

def transform(input_grid):
    # Initialize output_grid
    output_grid = np.copy(input_grid)
    regions = get_regions(input_grid)

    # Change output pixels
    for region, _ in regions:  # Region color is not needed for the fill itself
        x_start, y_start, width, height = region
        for row in range(y_start, y_start + height):
            for col in range(x_start, x_start + width):
                if input_grid[row, col] == 0:  # Found a white pixel (seed)
                    flood_fill(output_grid, row, col, region)

    return output_grid