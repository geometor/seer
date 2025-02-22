import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Find top-right and bottom-left corners
        rows, cols = zip(*obj)
        top_right_corner = (min(rows), max(cols))
        bottom_left_corner = (max(rows), min(cols))

        # Add blue pixel to the right of the top-right corner
        if top_right_corner[1] + 1 < output_grid.shape[1]:
            output_grid[top_right_corner[0], top_right_corner[1] + 1] = 1

        # Add blue pixel to the left of the bottom-left corner
        if bottom_left_corner[1] - 1 >= 0:
            output_grid[bottom_left_corner[0], bottom_left_corner[1] - 1] = 1

    return output_grid