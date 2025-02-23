"""
1.  **Identify:** Locate all pixels with the value '8' (azure) within the input grid.
2.  **Evaluate Adjacency:** For each azure pixel, check for diagonal adjacency:
    *   specifically, if the top left 2x2 subgrid matches either of these patterns:
        *   8s in the top-left and bottom-right, 1 is placed in top-left
        *   8s in the top-right and bottom-left, 1 is placed in bottom-right

3.  **Transform:**
    *   if an azure pixel has another azure pixel located diagonally down and to the right, change the first pixel's value to '1' (blue).
    *   if an azure pixel has another azure pixel located diagonally up and to the left, change the second pixel's value to '1' (blue)
4.  **Output:** Produce the modified grid, where the identified azure pixels have been changed to blue, and all other pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current pixel is azure (8)
            if input_grid[i, j] == 8:
                # Check for diagonal adjacency (down and to the right)
                if i + 1 < rows and j + 1 < cols and input_grid[i + 1, j + 1] == 8:
                    output_grid[i, j] = 1  # Change the first pixel to blue (1)
                #check for diaganol adjaceny (up and to the left)
                elif i - 1 > 0 and j -1 > 0 and input_grid[i,j] == 8:
                    if input_grid[i-1,j-1] == 8:
                        output_grid[i,j] = 1


    return output_grid