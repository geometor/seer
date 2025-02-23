"""
1. Find all objects.
2. Move each object at the bottom, preserving the column position and stacking if necessary.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all distinct single-cell objects in the grid.
    Returns a dictionary of color: (row, col) pairs.
    """
    objects = {}
    for r, row in enumerate(grid):
        for c, color in enumerate(row):
            if color != 0:
                if color not in objects:
                    objects[color] = []
                objects[color].append((r, c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.zeros_like(input_grid)
    objects = find_objects(input_grid)

    # Create a dictionary to track the next available row for each column
    next_available_row = {col: input_grid.shape[0] - 1 for col in range(input_grid.shape[1])}

    # Iterate through each object and move it down
    for color, positions in objects.items():
        for r, c in positions:
          output_grid[next_available_row[c], c] = color
          next_available_row[c] -= 1

    return output_grid