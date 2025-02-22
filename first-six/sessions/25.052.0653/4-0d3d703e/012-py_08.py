"""
The transformation rule can be summarized by the following process:

1.  **Identify the color** of each cell in the input grid.
2.  **Apply the following transformation rules:**
    *   If the color is 5, add 6 to it and take the modulo 10 of the result.
    *   If the color is 6, subtract 4 from it and take the modulo 10 of the result.
    *   If the color is 2, add 4 to it and take the modulo 10 of the result.
    *   Otherwise, add 1 to the color and take the modulo 10 of the result.
3.  **Place the new color value** in the corresponding cell of the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions and data type as the input.
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid using nested loops.
    for x in range(input_grid.shape[0]):
        for y in range(input_grid.shape[1]):
            # Apply transformation rules based on the color value.
            if input_grid[x, y] == 5:
                output_grid[x, y] = (input_grid[x, y] + 6) % 10  # Add 6, modulo 10.
            elif input_grid[x, y] == 6:
                output_grid[x, y] = (input_grid[x, y] - 4) % 10  # Subtract 4, modulo 10.
            elif input_grid[x, y] == 2:
                output_grid[x, y] = (input_grid[x, y] + 4) % 10  # Add 4, modulo 10
            else:
                output_grid[x, y] = (input_grid[x, y] + 1) % 10  # Add 1, modulo 10.

    return output_grid