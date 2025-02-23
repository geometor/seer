"""
1. Examine the Input Grid.
2. Locate all pixels with the value of 8 (azure), 3 (green) or 1 (blue).
3. Change any pixel of color 8 (azure), 1 (blue), or 3 (green) to the color 5 (gray).
4. Leave pixels of all colors other than 8, 1, and 3 unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule:
    Replace azure (8), blue (1), and green (3) with gray (5); keep all other colors unchanged.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through all pixels
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Replace all instances of 8 (azure), 1 (blue) and 3 (green) with 5 (gray).
            if output_grid[i, j] in (8, 1, 3):
                output_grid[i, j] = 5

    return output_grid