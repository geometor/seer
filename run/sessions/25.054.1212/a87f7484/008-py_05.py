"""
1. Identify all pixels of color orange (7) in the input grid.
2. Observe relative position and relationships, with special attention to the surrounding white spaces (0).
3. Create a 3x3 output grid.
4. Fill the output grid using the spatial arrangement and the distribution pattern of orange as the main reference.
5. Complete the output using white (0) as needed.

In other words. Extract all orange (7) colored pixels. If an orange pixel is present at input[x,y], place it at output[x%3, y%3], and fill other places with white.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid to the output grid based on orange pixel positions."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)  # Initialize 3x3 output grid with white (0)

    rows, cols = input_grid.shape

    # Iterate through the input grid
    for i in range(rows):
        for j in range(cols):
            # Check if the pixel is orange (7)
            if input_grid[i, j] == 7:
                # Map the orange pixel to the output grid using modulo operation
                output_grid[i % 3, j % 3] = 7

    return output_grid.tolist()