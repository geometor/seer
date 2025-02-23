"""
Copies azure L-shapes from the input grid to the output grid and inserts a blue cell to the right of the vertical "tip" of each L-shape.
"""

import numpy as np

def find_l_shapes(grid, color):
    """Finds L-shaped objects of a specified color in the grid."""
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L shape (2x2 block with one cell missing)
                if grid[r+1, c] == color and grid[r, c+1] == color and grid[r+1,c+1] !=color:  # Top-left corner
                   l_shapes.append( ((r, c), (r+1, c), (r, c+1)) )
                if grid[r, c] == color and grid[r+1, c] == color and grid[r+1,c+1] == color and grid[r, c+1] !=color:  # mirrored L
                   l_shapes.append( ((r, c), (r+1, c), (r+1, c+1)) )


    return l_shapes

def get_tip_coordinates(l_shape_coordinates):
    """Calculates tip for the vertical bar in L shape"""
    #find lowest x
    coords = sorted(l_shape_coordinates, key=lambda item: item[0], reverse=True)

    if coords[0][0] > coords[1][0] and coords[0][0] > coords[2][0]:
       return (coords[0][0], coords[0][1]+1)
    #find largest x
    coords = sorted(l_shape_coordinates, key=lambda item: item[0])
    if coords[0][0] < coords[1][0] and coords[0][0] < coords[2][0]:
        return (coords[0][0], coords[0][1]+1)

    return None

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find L-shapes of color 8 (azure)
    l_shapes = find_l_shapes(input_grid, 8)

    # Insert blue cells
    for l_shape in l_shapes:
        # find the "tip" coordinate of the L shape
        tip_coord = get_tip_coordinates(l_shape)

        if tip_coord is not None:
           # add a blue cell next to the tip
           if tip_coord[0] < rows and tip_coord[1] < cols: # Check bounds
              output_grid[tip_coord] = 1

    return output_grid