"""
Copies the input grid to the output grid, then finds three specific L-shaped azure objects and modifies them.
"""

import numpy as np

def find_l_shapes(grid, color):
    # helper function for finding objects (same as before)
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return

        visited[x, y] = True
        current_object.append((x, y))

        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_object = []
                dfs(x, y, current_object)
                # check for approximate shape and size
                if 3 <= len(current_object) <= 5:
                    objects.append(current_object)

    return objects

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    if len(l_shapes) >= 3:
        # Process the first L-shape (right-most)
        first_l_shape = l_shapes[0]
        rightmost_pixel = max(first_l_shape, key=lambda p: p[1])
        output_grid[rightmost_pixel] = 1

        # Process the second L-shape (bottom-most)
        second_l_shape = l_shapes[1]
        bottommost_pixel = max(second_l_shape, key=lambda p: p[0])
        output_grid[bottommost_pixel] = 1

        # Process the third L-shape (top-most)
        third_l_shape = l_shapes[2]
        topmost_pixel = min(third_l_shape, key=lambda p: p[0])  # Use min for top-most
        output_grid[topmost_pixel] = 1


    return output_grid