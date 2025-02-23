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
    output_grid = input_grid.copy()
    l_shapes = find_l_shapes(input_grid, 8)
    for l_shape, missing_coords in l_shapes:
        output_grid[missing_coords] = 1
    return output_grid