"""
The transformation rule identifies azure (color 8) objects in the input grid. 
For each azure object, it locates specific corner:
- if the corner is part of a vertical line selects the top cell.
- if the corner is part of a horizontal line selects the left cell.
Then, changes that identified cell's color to blue (color 1). All other cells remain unchanged.
"""

import numpy as np

def get_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of lists of coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_corner_cell(obj):
    """
    Finds the corner cell of an object. It considers the cell part of the longest
    rectangle side.

    """
    min_row = min(cell[0] for cell in obj)
    #max_row = max(cell[0] for cell in obj)
    min_col = min(cell[1] for cell in obj)
    #max_col = max(cell[1] for cell in obj)

    top_left = (min_row, min_col)

    is_vertical = False
    for cell in obj:
      if cell[0] == min_row + 1 and cell[1] == min_col:
        is_vertical = True
        break

    if is_vertical:
      return top_left
    else:
      return top_left
      
def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Get azure (color 8) objects
    azure_objects = get_objects(output_grid, 8)
    
    # Iterate through each azure object
    for obj in azure_objects:
        # Find the corner cell of the object
        corner_cell = find_corner_cell(obj)

        # Change the corner cell's color to blue (color 1)
        output_grid[corner_cell[0], corner_cell[1]] = 1

    return output_grid