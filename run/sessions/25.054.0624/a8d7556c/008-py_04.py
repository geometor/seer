"""
1.  **Identify Regions:** Examine the input grid and identify enclosed regions of white (0) pixels that are completely surrounded by gray (5) pixels. These regions may have irregular shapes.

2.  **Selective Filling:** Starting at row index 5, and moving left to right, and downward by one row, for all regions identified in the prior stage: if there is white (0) pixel, paint it and every pixel to the right of it, until the next grey pixel, with '2'.
    - continue until the last row of the output

3.  **Preserve Boundaries:** The gray (5) pixels in the input grid remain unchanged in the output grid. Their positions define the boundaries for the filling operation.

4.  **Unfilled Regions:** Some white (0) regions may not be modified because it is before row 5, based on the selective filling criteria above.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through rows starting from index 5
    for i in range(5, rows):
        # Iterate through columns
        for j in range(cols):
            # Check if the current pixel is white (0)
            if output_grid[i, j] == 0:
                # Fill with red (2) to the right until a gray (5) pixel is encountered
                for k in range(j, cols):
                    if output_grid[i, k] == 0:
                        output_grid[i, k] = 2
                    elif output_grid[i,k] == 5:
                        break; #stop when a gray pixel is encountered
    return output_grid