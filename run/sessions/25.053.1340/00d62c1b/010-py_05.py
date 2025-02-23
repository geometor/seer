"""
Identifies a green (3) pixel within the input grid that is completely surrounded by other green pixels, 
and changes the color of that pixel to yellow (4). All other pixel values are maintained.
"""

import numpy as np

def get_green_pixels(grid):
    """Finds coordinates of all green pixels in the grid."""
    green_pixels = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 3:
                green_pixels.append((r, c))
    return green_pixels

def is_surrounded(grid, r, c):
    """Checks if a pixel at (r, c) is surrounded by green pixels."""
    rows, cols = len(grid), len(grid[0])
    # Check immediate neighbors (up, down, left, right)
    neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    for nr, nc in neighbors:
        if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 3):
            return False  # Not surrounded if any neighbor is out of bounds or not green
    return True

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = len(output_grid), len(output_grid[0])
    
    # Find all green pixels
    green_pixels = get_green_pixels(output_grid)
    
    # Find a green pixel that is surrounded by other green pixels
    target_pixel = None
    for r, c in green_pixels:
        if is_surrounded(output_grid, r, c):
            target_pixel = (r, c)
            break  # Stop after finding the first surrounded pixel

    # Change the color of the selected pixel to yellow (4)
    if target_pixel:
        output_grid[target_pixel[0]][target_pixel[1]] = 4

    return output_grid