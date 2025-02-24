"""
1. Identify the Expanding Color: Find the color in the input grid that is not white (0). This is the "expanding color".
2. Determine Output Dimensions: Count the number of pixels of the expanding color in the input grid. The output grid will have a height of this count plus the number of rows in the input (which is always 1, so count + 1). The output grid has same number of columns as the input.
3. Create Diagonal Rectangle:
    *   The expanding color creates a diagonal rectangle in the output grid.
    * The height of the rectangle is equal to the count determined before + 1
4. Fill Background: Fill the remaining cells of the output grid with white (0).
"""

import numpy as np

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the expanding color (non-zero color)
    expanding_color = None
    for color in np.unique(input_grid):
        if color != 0:
            expanding_color = color
            break

    # Count the number of pixels of the expanding color
    expanding_color_count = np.count_nonzero(input_grid == expanding_color)

    # Determine output dimensions
    output_rows = expanding_color_count + rows
    output_cols = cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Create the diagonal rectangle
    for i in range(output_rows):
        for j in range(min(output_cols, expanding_color_count + i)):
            output_grid[i, j] = expanding_color

    return output_grid.tolist()