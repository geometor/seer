"""
The transformation rule is: "Locate the L-shaped azure objects, identify the specific cells immediately to the right or left of these L-shaped objects, and change those cells to blue, maintaining all other cells."
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of tuples, each containing the coordinates of the elbow cell of each L.
    """
    rows, cols = grid.shape
    l_shapes = []

    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for top-left L
            if (grid[r, c] == color and grid[r + 1, c] == color and
                grid[r, c + 1] == color and grid[r+1,c+1] !=color):
                l_shapes.append((r + 1, c)) #elbow
            # Check for bottom-right L
            if (grid[r, c] != color and grid[r + 1, c] == color and
                grid[r, c + 1] == color and grid[r+1,c+1] ==color):
                l_shapes.append((r+1, c + 1)) #elbow
            # Check for top-right L
            if (grid[r, c] == color and grid[r+1, c] != color and
                grid[r, c+1] == color and grid[r+1, c + 1] == color):
                l_shapes.append((r, c+1))
            # Check for bottom-left L
            if (grid[r,c] == color and grid[r+1,c] == color and grid[r,c+1]!=color and grid[r+1,c+1] == color):
                l_shapes.append((r+1,c))



    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1. Find all L-shaped azure objects.
    2. Change the color of cells to the right or left of these L-shapes to blue.
    3. Keep other cells unchanged.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the L-shaped objects of color 8 (azure)
    l_shapes = find_l_shapes(output_grid, 8)

    # Change specific cells to blue (color 1) if L shapes are found
    for l_elbow in l_shapes:

        # Top-Left L shape
        if l_elbow[1] + 1 < output_grid.shape[1] and output_grid[l_elbow[0]-1,l_elbow[1]] == 8 and output_grid[l_elbow[0],l_elbow[1]+1] == 8:
                output_grid[l_elbow[0], l_elbow[1] + 1] = 1

        # Bottom-Right L
        elif l_elbow[1] -1 >= 0 and output_grid[l_elbow[0]-1,l_elbow[1]] == 8 and output_grid[l_elbow[0],l_elbow[1]-1] == 8:
                output_grid[l_elbow[0], l_elbow[1] - 1] = 1
        # Top-Right L
        elif l_elbow[1]-1 >= 0 and output_grid[l_elbow[0],l_elbow[1]-1]==8 and output_grid[l_elbow[0]+1,l_elbow[1]] == 8:
             output_grid[l_elbow[0],l_elbow[1]-1] = 1
        # Bottom-Left L
        elif l_elbow[1] + 1 < output_grid.shape[1] and output_grid[l_elbow[0]-1,l_elbow[1]]==8 and output_grid[l_elbow[0],l_elbow[1]+1]==8:
              output_grid[l_elbow[0],l_elbow[1]+1] = 1
    return output_grid