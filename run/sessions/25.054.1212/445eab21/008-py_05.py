"""
1.  **Identify the Target Object:** Find the orange (value 7) object within the input grid.
2.  **Extract Representative:** Extract the smallest possible 2x2 square composed entirely of the orange color (7).
3.  **Output:** Present this extracted 2x2 orange square as the output. Disregard all other objects and colors in the input.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds all contiguous regions of a specific color in the grid.
    """
    coords = np.argwhere(grid == color)
    if len(coords) == 0:
        return []

    objects = []
    visited = set()

    def dfs(row, col, current_object):
        if (row, col) not in visited and 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1] and grid[row, col] == color:
            visited.add((row, col))
            current_object.append((row, col))
            dfs(row + 1, col, current_object)
            dfs(row - 1, col, current_object)
            dfs(row, col + 1, current_object)
            dfs(row, col - 1, current_object)


    for row, col in coords:
        if (row, col) not in visited:
            current_object = []
            dfs(row, col, current_object)
            objects.append(current_object)

    return objects

def extract_2x2_square(objects):
    """
    Extracts the first 2x2 square from the list of objects. It assumes a 2x2 is the min representation.
    Returns coordinates of the 2x2 square as a list of tuples.
    """

    for obj in objects: # for each object
      for r, c in obj:   # check each pixel to make sure not on edge.

          if (r + 1, c) in obj and (r, c+1) in obj and (r+1, c+1) in obj:
              return [[r,c], [r+1, c], [r, c+1], [r+1, c+1]]

    return []

def transform(input_grid):
    """
    Transforms the input grid according to the described rules.
    """
    # Find the orange (7) object.
    orange_objects = find_objects(input_grid, 7)

    # Extract a 2x2 square of orange color.
    square_coords = extract_2x2_square(orange_objects)

    # create output grid based on presence of 2x2 square
    if len(square_coords) > 0:
      output_grid = np.full((2, 2), 7, dtype=int) # all orange output
    else:
      output_grid = np.full((2,2), 0, dtype=int) # blank output if not

    return output_grid