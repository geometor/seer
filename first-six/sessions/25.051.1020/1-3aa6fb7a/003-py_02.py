import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of coordinates representing the corners of the L-shapes.
    """
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for different orientations of L-shapes
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    l_shapes.append(((r, c), (r + 1, c), (r, c + 1)))  # Bottom-Right
                elif grid[r + 1, c] == color and grid[r + 1, c + 1] == color:
                    l_shapes.append(((r, c), (r + 1, c), (r + 1, c + 1)))  # Bottom-Left
                elif grid[r, c + 1] == color and grid[r + 1, c + 1] == color:
                    l_shapes.append(((r, c), (r, c + 1), (r + 1, c + 1)))  # Top-Left
                elif c>0 and grid[r+1,c] == color and grid[r+1,c-1] == color:
                    l_shapes.append(((r, c), (r + 1, c), (r + 1, c - 1))) # Top-Right
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    - Keeps the position and shape of L-shaped azure (8) objects.
    - Adds one blue (1) cell to fill their inner empty corner.
    """
    output_grid = np.zeros_like(input_grid)  # Initialize with all zeros
    
    # Find L-shapes of color 8 (azure)
    l_shapes = find_l_shapes(input_grid, 8)
    
    # Fill the inner empty corner of each L-shape with color 1 (blue)
    for l_shape in l_shapes:
        (r1, c1), (r2, c2), (r3, c3) = l_shape
        
        #Copy L
        output_grid[r1,c1] = 8
        output_grid[r2,c2] = 8
        output_grid[r3,c3] = 8


        # Determine the corner and fill the inside
        if r2 == r1 + 1 and c2 == c1:  # r1,c1 and r1+1, c1
            if c3 == c1 + 1: # Bottom-Right L
                output_grid[r1+1, c1 + 1] = 1
            else: # Top-Right L
                output_grid[r1+1,c1-1] = 1
        elif r2 == r1 + 1 and c2 == c1+1:  # r1, c1 and r1+1, c1+1
            output_grid[r1, c1 + 1] = 1 # Bottom-Left L
        elif r2 == r1 and c2 == c1 + 1: #r1,c1 and r1, c1+1
            output_grid[r1 + 1, c1 + 1] = 1  # Top-Left L


    return output_grid