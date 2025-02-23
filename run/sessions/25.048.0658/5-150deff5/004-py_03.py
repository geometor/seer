"""
The transformation rule involves identifying a specific object, conceptually splitting it into two horizontal sections based on contiguity, and recoloring each section with a distinct color. The positions and overall shape is respected, just altering the original object's color, splitted in two.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous regions of the same color in a grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, color, obj):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        obj.append((r, c))
        dfs(r + 1, c, color, obj)
        dfs(r - 1, c, color, obj)
        dfs(r, c + 1, color, obj)
        dfs(r, c - 1, color, obj)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if not visited[r, c] and grid[r, c] != 0:
                obj = []
                dfs(r, c, grid[r, c], obj)
                objects.append(obj)
    return objects

def split_object(obj):
    """
    Splits the object into two parts based on contiguity analysis.
    """
    # Find rows with only two contiguous pixels
    rows_with_two = []

    for row in range(min(r for r, c in obj), max(r for r, c in obj) + 1):

        row_pixels = [(r,c) for r,c in obj if r == row]
        if len(row_pixels) == 2:
            rows_with_two.append(row)

    # Split criteria. We are looking for a row that, if removed
    # separates the list
    top_half = []
    bottom_half = []
    split_row = -1

    if len(rows_with_two)>0:
      split_row = rows_with_two[0] # first one
      top_half = [(r,c) for r,c in obj if r < split_row]
      bottom_half = [(r,c) for r,c in obj if r > split_row]

    if len(top_half) == 0:
      # just split by the middle row
        min_row = min(r for r, c in obj)
        max_row = max(r for r, c in obj)
        mid_row = (min_row + max_row) // 2
        top_half = [(r, c) for r, c in obj if r <= mid_row]
        bottom_half = [(r, c) for r, c in obj if r > mid_row]

    return top_half, bottom_half

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find objects in the grid
    objects = get_objects(input_grid)

    # Assume there's only one relevant object (color 5)
    for obj in objects:
        if input_grid[obj[0]] == 5:
            # Split the object
            top_half, bottom_half = split_object(obj)

            # Recolor the top half to 8
            for r, c in top_half:
                output_grid[r, c] = 8

            # Recolor the bottom half to 2
            for r, c in bottom_half:
                output_grid[r, c] = 2

    return output_grid