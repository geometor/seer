"""
1.  **Identify the Cross:** Locate the cross-shaped object within the input grid. This object is defined as a set of contiguous green (3) pixels forming a cross.
2.  **Locate Interior Pixels:** Examine each cell in the cross.
3. **Transform Interior Pixels:** Find the pixels that are completely surrounded on all four sides (up, down, left, right and not diagnonally) and convert those green (3) pixels into yellow (4) pixels.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Create a copy of the input grid to serve as the output grid.
    output_grid = np.copy(input_grid)
    
    # Find the dimensions of the grid.
    rows, cols = input_grid.shape
    
    # Iterate through each cell of the grid (excluding the borders).
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Check if the current cell is green (3).
            if input_grid[i, j] == 3:
                # Check if the current cell is surrounded by green pixels on all four sides.
                if (input_grid[i-1, j] == 3 and
                    input_grid[i+1, j] == 3 and
                    input_grid[i, j-1] == 3 and
                    input_grid[i, j+1] == 3):
                    # Change the color of the current cell to yellow (4).
                    output_grid[i, j] = 4

    return output_grid