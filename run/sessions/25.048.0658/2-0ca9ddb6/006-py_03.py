"""
This script implements the transformation rule described as follows:

1. **Identify Key Objects:** Locate all red (color 2) pixels and blue (color 1) pixels in the input grid.
2. **Red Surroundings:** For each red pixel, change the color of the pixels immediately above, below, to the left, and right to the color yellow (value 4).
3. **Blue Surroundings:** For each blue pixel, change the color of the pixels immediately above, below, to the left, and right to the color orange (value 7).
4. **Preservation:** The positions of the original red and blue pixels, and any other color are preserved.
5. **Background:** All other pixels remain unchanged (color 0).
"""

import numpy as np

def find_all_pixels(grid, color):
    """Finds the coordinates of all pixels of the specified color."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """Transforms the input grid according to the generalized rule."""
    
    output_grid = np.copy(input_grid)
    
    # Find all red pixels (color 2)
    red_pixels = find_all_pixels(input_grid, 2)
    for row, col in red_pixels:
        # Change surrounding pixels to yellow (color 4)
        if row > 0:
            output_grid[row - 1, col] = 4  # Above
        if row < input_grid.shape[0] - 1:
            output_grid[row + 1, col] = 4  # Below
        if col > 0:
            output_grid[row, col - 1] = 4  # Left
        if col < input_grid.shape[1] - 1:
            output_grid[row, col + 1] = 4  # Right
            
    # Find all blue pixels (color 1)
    blue_pixels = find_all_pixels(input_grid, 1)
    for row, col in blue_pixels:
       # Change surrounding pixels to orange (color 7)
        if row > 0:
            output_grid[row - 1, col] = 7  # Above
        if row < input_grid.shape[0] - 1:
            output_grid[row + 1, col] = 7  # Below
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < input_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # Right

    return output_grid