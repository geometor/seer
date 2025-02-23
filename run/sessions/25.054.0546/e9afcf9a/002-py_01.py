"""
The transformation takes a 2x6 grid as input. The output grid is also 2x6. The colors in the output grid alternate between green (3) and maroon (9) in both rows and columns. Specifically:

1.  The first row of the output alternates starting with green: green, maroon, green, maroon, green, maroon.
2.  The second row of the output alternates starting with maroon: maroon, green, maroon, green, maroon, green.
3. Each column alternates between green and maroon.

Essentially. The transformation creates a checkerboard pattern using the two colors from the input rows.
"""

import numpy as np

def transform(input_grid):
    # Get dimensions of the input grid
    rows, cols = input_grid.shape
    
    # Initialize the output grid with the same dimensions
    output_grid = np.zeros((rows, cols), dtype=int)

    # Define the color mapping
    green = 3
    maroon = 9
    
    # Iterate through each cell of the output grid
    for i in range(rows):
        for j in range(cols):
            # Alternate colors based on row and column indices
            if (i + j) % 2 == 0:
                output_grid[i, j] = green  # Even sum: green
            else:
                output_grid[i, j] = maroon # Odd sum: maroon

    return output_grid