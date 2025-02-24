"""
1. **Identify Divider:** Locate the horizontal line of yellow (4) pixels in the input grid. This line divides the input grid into an "upper region" and "lower region".
2.  **Focus on Upper Region:** Disregard the "lower region" of the input grid (everything at or below the yellow line).
3. **Determine output size:** The output size is the dimensions of the "upper region".
4.  **Map to Output:** Create an output grid of the dimensions determined in the previous step. For each non-white pixel in the "upper region", change the color to green (3). Change all the white pixels to 0.
"""

import numpy as np

def find_horizontal_line(grid, color):
    """Finds the row index of a horizontal line of a given color."""
    for i, row in enumerate(grid):
        if all(pixel == color for pixel in row):
            return i
    return -1  # Not found

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)

    # 1. Identify Divider
    yellow_line_row = find_horizontal_line(input_grid, 4)

    # 2. Focus on Upper Region
    upper_region = input_grid[:yellow_line_row]

    # 3. Determine Output size
    output_height, output_width = upper_region.shape
    
    # Initialize the output_grid
    output_grid = np.zeros((output_height, output_width), dtype=int)


    # 4. Map to Output
    for i in range(output_height):
        for j in range(output_width):
            if upper_region[i,j] != 0:
                output_grid[i,j] = 3
            else:
                output_grid[i, j] = 0


    return output_grid.tolist()