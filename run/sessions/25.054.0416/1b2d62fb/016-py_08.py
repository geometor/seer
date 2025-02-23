"""
1.  **Identify Key Element:** Find all blue (1) pixels in the input grid.
2.  **Output Grid:** create output is a 5x3 grid, filled with white (0).
3.  **Map and transform:**
    *   For each blue pixel in input:
        *   Calculate output row: `input_row // 2`
        *   Calculate output col: `input_col // 2`
        *   Set the pixel at `[output_row, output_col]` in the output grid to azure (8).
4. **Output:** return the modified output grid.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    """Finds the coordinates of pixels of a specific color."""
    return np.argwhere(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros((5, 3), dtype=int)  # Initialize 5x3 output grid with white (0)

    blue_pixels = find_pixels_by_color(input_grid, 1)  # Find blue pixels

    for row, col in blue_pixels:
        new_row = row // 2  # Corrected row transformation
        new_col = col // 2  # Corrected column transformation
        if 0 <= new_row < 5 and 0<= new_col < 3:
            output_grid[new_row, new_col] = 8 #set to azure

    return output_grid