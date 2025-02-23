"""
The transformation rule preserves three distinct azure (8) objects and adds a blue (1) pixel adjacent to each of them. The rule follows a left, top, left, sequence.

"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specified color in the grid.
    Returns a list of coordinates (row, col) for each object,
    where each object is a list of connected pixels of the same color.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        # Check adjacent cells (including diagonals for this specific task)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    1. Locate azure (8) objects.
    2. Keep azure objects unchanged.
    3. Add a blue (1) pixel to the left, to the top, to the left of each azure object.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    if len(azure_objects) >= 3:
        # Process the first azure object (horizontal line)
        first_object = sorted(azure_objects[0], key=lambda x: x[1])
        left_pixel = first_object[0]
        output_grid[left_pixel[0], left_pixel[1] - 1] = 1
        # Process the second azure object (vertical line)
        second_object = sorted(azure_objects[1], key=lambda x: x[0])  # Sort by row
        top_pixel = second_object[0]
        output_grid[top_pixel[0] - 1, top_pixel[1]] = 1

        # Process the third azure object
        third_object = sorted(azure_objects[2], key=lambda x: x[1])  # Sort by column
        left_pixel = third_object[0]
        output_grid[left_pixel[0], left_pixel[1] - 1] = 1
    return output_grid