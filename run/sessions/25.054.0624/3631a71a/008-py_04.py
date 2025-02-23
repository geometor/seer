"""
The transformation rule involves identifying connected regions (objects) of the same color in the input grid and then simplifying the colors within each object. Specifically, if a color appears only once within an object, it is replaced by one of its most prevalent neighboring color.
"""

import numpy as np
from collections import Counter

def get_objects(grid):
    """
    Identifies and returns a list of objects in the grid.
    An object is a set of connected pixels with the same color.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.add((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, color, current_object)

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                current_object = set()
                dfs(r, c, grid[r, c], current_object)
                objects.append((grid[r,c], current_object)) #Store the color and the set
    return objects

def get_neighbors(grid, r, c):
    """
    Get valid neighbors for the given cell.

    """

    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append(grid[nr, nc])
    return neighbors


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify Objects:
    objects = get_objects(input_grid)

    # Iterate through each object:
    for color, object_pixels in objects:

      # Analyze Colors:
      pixels_list = list(object_pixels)
      colors_in_object = [input_grid[r,c] for r, c in pixels_list]
      color_counts = Counter(colors_in_object)

      #Find the colors to be changed and store positions in dict
      colors_to_change = {color:[] for color, count in color_counts.items() if count == 1}
      for r, c in pixels_list:
          if input_grid[r,c] in colors_to_change:
              colors_to_change[input_grid[r,c]].append((r,c))

      # Update Colors
      for unique_color, positions in colors_to_change.items():
        for r, c in positions:
          #Find the most prevalent neighbor
          neighbors = get_neighbors(input_grid, r, c)
          if neighbors: #Check that list of neighbors is not empty
            neighbor_counts = Counter(neighbors)
            #Exclude pixels of same color from the count
            if unique_color in neighbor_counts:
               del neighbor_counts[unique_color]

            if neighbor_counts: # Check the neighbor count is not empty after removing same color
              most_common_neighbor = neighbor_counts.most_common(1)[0][0]

            #If the count is empty, keeps original pixel
              output_grid[r, c] = most_common_neighbor


    return output_grid