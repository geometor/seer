"""
1.  **Identify L-shapes:** Find all 2x2 blocks of pixels where exactly three of the pixels are azure (color 8) and one is not. These form L-shaped objects.

2.  **Locate the Inner Corner:** For each L-shape, determine the location of the "missing" pixel within the 2x2 block that would complete a square. This is the inner corner.

3.  **Fill the Inner Corner:** Change the color of the pixel at the inner corner to blue (color 1).

4. **Copy other elements** All other cells remain unchanged.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of coordinates representing the corners of the L-shapes,
    and the coordinates of the missing corner.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Extract the 2x2 block
            block = grid[r:r+2, c:c+2]
            # Count the number of pixels of the specified color
            count = np.sum(block == color)
            if count == 3:
                # Find the coordinates of the missing corner within the 2x2 block
                missing_row, missing_col = np.where(block != color)
                missing_coords = (r + missing_row[0], c + missing_col[0])
                
                coords = []
                for i in range(2):
                    for j in range(2):
                        if grid[r+i,c+j] == color:
                           coords.append((r+i,c+j))

                l_shapes.append((coords, missing_coords))
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Keeps the position and shape of L-shaped azure (8) objects.
    - Adds one blue (1) cell to fill their inner empty corner.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = input_grid.copy()
    # Find L-shapes of color 8 (azure)
    l_shapes = find_l_shapes(input_grid, 8)
    # Fill the inner empty corner of each L-shape with color 1 (blue)
    for l_shape, missing_coords in l_shapes:
        output_grid[missing_coords] = 1
    return output_grid