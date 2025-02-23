"""
The transformation rule is: "Locate the two separated L-shaped azure objects, identify the specific cells to the right and left of the L shaped objects, and change those to blue, maintaining every other cell."
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of tuples, each containing the coordinates of the elbow cell.
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

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1. Find two L-shaped azure objects.
    2. Change the color of the cell to the right of the top-left L and the cell to the left of the bottom-right L to blue.
    3. Keep other cells unchanged.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find the L-shaped objects of color 8 (azure)
    l_shapes = find_l_shapes(output_grid, 8)
    
    # Sort the l_shapes. Assume top-left L comes first.
    l_shapes.sort()

    # Change specific cells to blue (color 1) if L shapes are found
    if len(l_shapes) == 2:
        top_left_l_elbow = l_shapes[0]
        bottom_right_l_elbow = l_shapes[1]

        # Change cell to the right of the top-left L
        if top_left_l_elbow[1] + 1 < output_grid.shape[1]:
          output_grid[top_left_l_elbow[0], top_left_l_elbow[1] + 1] = 1

        # Change cell to the left of the bottom-right L
        if bottom_right_l_elbow[1] -1 >= 0:
          output_grid[bottom_right_l_elbow[0], bottom_right_l_elbow[1] - 1] = 1

    return output_grid