"""
The transformation rule preserves two L-shaped azure objects and changes the color of the cells immediately to the right of their top-left corners from white (0) to blue (1).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected regions of the specified color and returns a list of their coordinates.
    Uses a simple flood-fill algorithm.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def flood_fill(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            flood_fill(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                flood_fill(r, c, current_object)
                objects.append(current_object)

    return objects
def get_top_left(obj):
    """
    Gets the top-left coordinate of an object.
    """
    min_row = float('inf')
    min_col = float('inf')

    for r, c in obj:
        if r < min_row:
            min_row = r
        if c < min_col:
          min_col = c
    return min_row,min_col
def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1.  Identify azure (color 8) L-shaped objects.
    2.  Preserve their structure.
    3. Change to blue the cells to the right of the top-left-corner
    of each object, from white (color 0)
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through the azure objects
    for obj in azure_objects:
      #find top-left corner
      top_left_r, top_left_c = get_top_left(obj)
      #check if the cell to the right exists and it is color 0
      if top_left_c + 1 < output_grid.shape[1] and output_grid[top_left_r,top_left_c + 1] == 0:
        output_grid[top_left_r, top_left_c + 1] = 1
    return output_grid