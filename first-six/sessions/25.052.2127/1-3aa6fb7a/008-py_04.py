"""
Identifies two mirrored "L"-shaped azure objects in the input grid.
Adds a blue pixel inside each L-shape, relative to its corner and direction:
- 'up': blue pixel below and to the right of the corner.
- 'down': blue pixel above and to the left of the corner.
- 'right': blue pixel below and to the left of the corner
- 'left': blue pixel above and to the right of the corner
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specified color in the grid.
    Returns a list of coordinates representing the corner pixel of each L-shape,
    and a direction ('up', 'down', 'left', 'right').
    """
    rows, cols = grid.shape
    l_shapes = []

    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L shapes
                if grid[r + 1, c] == color and grid[r, c + 1] == color:  # Top-left L
                    l_shapes.append( ((r, c), 'up') )
                elif grid[r - 1, c] == color and grid[r, c - 1] == color: # Bottom-right L
                    l_shapes.append( ((r,c), 'down') )
                elif grid[r - 1, c] == color and grid[r, c + 1] == color: # Top-right L
                     l_shapes.append( ((r, c), 'right') )
                elif grid[r + 1, c] == color and grid[r, c - 1] == color:  #Bottom-left L
                     l_shapes.append( ((r,c), 'left'))

    # Remove duplicates, keeping only unique L-shape corners.
    unique_l_shapes = []
    seen_corners = set()

    for corner, direction in l_shapes:
      if corner not in seen_corners:
        unique_l_shapes.append((corner, direction))
        seen_corners.add(corner)

    return unique_l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure = 8
    blue = 1

    # Find the corner coordinates and directions of all azure L-shapes
    l_shapes = find_l_shapes(input_grid, azure)

    # Insert blue pixels based on L-shape orientation
    for (r, c), direction in l_shapes:
        # Check the orientation and place blue pixel
        if direction == 'up':
          output_grid[r + 1, c + 1] = blue
        elif direction == 'down':
          output_grid[r - 1, c - 1] = blue
        elif direction == 'right':
          output_grid[r - 1, c + 1] = blue
        elif direction == 'left':
          output_grid[r + 1, c - 1] = blue

    return output_grid