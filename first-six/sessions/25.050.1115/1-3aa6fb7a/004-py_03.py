"""
The transformation rule identifies all azure (8) L-shaped objects in the input grid.
It then changes the color of specific white (0) cells to blue (1) based on their position relative to these azure objects.

- For the "top-left/first" azure object (when sorted by top cell row, then column),
  it changes the white cell to the right of its topmost cell to blue.

- For the "bottom-right/last" azure object,
  it changes the white cell to the left of its bottommost cell to blue.
- If the two rules don't apply to an object:
  - For a "middle" object,
      change the cell to the left of the top-most cell.

All other cells remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Finds connected regions of the specified color."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        """Depth-first search to find connected cells."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_top_cell(obj):
    """Returns the cell with the smallest row value (top-most)."""
    return min(obj, key=lambda cell: cell[0])

def get_bottom_cell(obj):
    """Returns the cell with the largest row value."""
    return max(obj, key=lambda cell: cell[0])

def sort_objects(objects):
     """Sorts objects based on top-left corner's row, then column."""
     return sorted(objects, key=lambda obj: (get_top_cell(obj)[0], get_top_cell(obj)[1]))

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    sorted_azure_objects = sort_objects(azure_objects)

    for i, obj in enumerate(sorted_azure_objects):
        top_cell = get_top_cell(obj)
        bottom_cell = get_bottom_cell(obj)
        changed = False #flag

        # "Top-Left/First" object rule
        if i == 0:
            right_of_top = (top_cell[0], top_cell[1] + 1)
            if (
                0 <= right_of_top[0] < output_grid.shape[0]
                and 0 <= right_of_top[1] < output_grid.shape[1]
                and output_grid[right_of_top] == 0
            ):
                output_grid[right_of_top] = 1
                changed = True

        # "Bottom-Right/Last" object rule
        if i == len(sorted_azure_objects) - 1:
            left_of_bottom = (bottom_cell[0], bottom_cell[1] - 1)
            if (
                0 <= left_of_bottom[0] < output_grid.shape[0]
                and 0 <= left_of_bottom[1] < output_grid.shape[1]
                and output_grid[left_of_bottom] == 0
            ):
                output_grid[left_of_bottom] = 1
                changed = True

        # "Middle Object"
        if (not changed):
             left_of_top = (top_cell[0], top_cell[1] - 1)
             if (
                0 <= left_of_top[0] < output_grid.shape[0]
                and 0 <= left_of_top[1] < output_grid.shape[1]
                and output_grid[left_of_top] == 0
            ):
                output_grid[left_of_top] = 1


    return output_grid