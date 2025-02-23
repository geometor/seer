"""
1.  **Identify Colored Pixels:** Locate all pixels in the input grid that are *not* white (0).
2.  **Expand Each:** For *each* of these non-white pixels, create a 3x3 block in the output grid. The original pixel's color should be used for its entire 3x3 block. The 3x3 block should be centered on the original pixel's location. If this expansion would go past the edge of the input, constrain it to stop at the border.
3.  **Handle Overlaps:** After *all* expansions are complete, check for any overlapping pixels (pixels where multiple expanded blocks have a non-white color). For *all* of these overlapping pixels, set their color in the output grid to gray (5).
4. **Maintain background:** all un-affected pixels should stay white (0)
"""

import numpy as np

def get_pixels_by_color(grid, color):
    """Finds the positions of all pixels of a given color."""
    return np.argwhere(grid == color)

def get_non_white_pixels(grid):
    """Finds the positions of all non-white pixels."""
    return np.argwhere(grid != 0)

def expand_pixel(grid, position, color):
    """Expands a pixel into a 3x3 block, constrained by grid boundaries."""
    rows, cols = grid.shape
    row, col = position
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            grid[i, j] = color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    # Initialize output_grid as all white
    output_grid = np.zeros_like(input_grid)
    output_grid[:] = 0 # Explicitly set to white

    # Create a temporary grid to store expanded pixels before overlap check
    temp_grid = np.zeros_like(input_grid)

    # Get initial positions of all non-white pixels
    non_white_pixels = get_non_white_pixels(input_grid)

    # Expand each non-white pixel in the temporary grid
    for pos in non_white_pixels:
        color = input_grid[pos[0], pos[1]]
        temp_grid = expand_pixel(temp_grid, pos, color)

    # Iterate through the temp_grid to build the output and handle overlaps
    for i in range(output_grid.shape[0]):
      for j in range(output_grid.shape[1]):
        if temp_grid[i,j] != 0:
            output_grid[i,j] = temp_grid[i,j]
    
    # find overlaps and replace with color (5) gray
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            pixel_count = 0
            for pos in non_white_pixels:
              color = input_grid[pos[0], pos[1]]
              expanded_grid = np.zeros_like(input_grid)
              expanded_grid = expand_pixel(expanded_grid, pos, color)
              if expanded_grid[i,j] != 0:
                pixel_count+=1
            if pixel_count > 1:
              output_grid[i,j] = 5

    return output_grid