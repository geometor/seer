"""
1.  **Identify Green:** Find all pixels in the input grid that are colored green (value 3).
2.  **Find Adjacent Pixels:** For each green pixel, locate its immediate neighbors. Neighbors are defined as the pixels directly above, below, to the left, and to the right (not diagonal).
3.  **Conditional Color Change:** For each neighboring pixel:
    *   If the neighboring pixel is white (value 0), change its color to yellow (value 4).
    *   If the neighboring pixel is *not* white, leave it unchanged.
4.  **Output:** The output grid has the same dimensions as the input grid, with only the specified color changes applied. All other pixels remain their original color.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    # returns a list of (row, col) tuples for pixels matching the specified color
    return np.array(np.where(grid == color)).T.tolist()

def get_adjacent_pixels(grid, position):
    # returns a list of (row, col) tuples for pixels adjacent (horizontally or vertically) to a given position
    rows, cols = grid.shape
    row, col = position
    adjacent = []
    if row > 0:
        adjacent.append([row - 1, col])  # Up
    if row < rows - 1:
        adjacent.append([row + 1, col])  # Down
    if col > 0:
        adjacent.append([row, col - 1])  # Left
    if col < cols - 1:
        adjacent.append([row, col + 1])  # Right
    return adjacent

def transform(input_grid):
    # initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # find all green pixels
    green_pixels = find_pixels_by_color(input_grid, 3)
    
    # find white pixels adjacent to green pixels and change their color to yellow
    for green_pixel in green_pixels:
        for adj_pixel in get_adjacent_pixels(input_grid, green_pixel):
            # check if adjacent pixel is white before changing color
            if input_grid[adj_pixel[0], adj_pixel[1]] == 0:
                output_grid[adj_pixel[0], adj_pixel[1]] = 4
                
    return output_grid