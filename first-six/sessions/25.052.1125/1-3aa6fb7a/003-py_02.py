import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
        obj.sort()  # Sort by row, then column
        rows = [r for r, c in obj]
        cols = [c for r, c in obj]

        if len(set(rows)) > len(set(cols)):  # More rows than cols = vertical
            top_cell = obj[0]
            output_grid[top_cell[0], top_cell[1] + 1] = 1
        elif len(set(cols)) > len(set(rows)): # More cols than rows = horizontal
            rightmost_cell = obj[-1]
            output_grid[rightmost_cell[0], rightmost_cell[1] - 1] = 1
        else: #same number of rows and columns: could be a single cell or square
              # if it is 1x1, it can be treated as horizontal or vertical
            if len(obj) == 1:
                top_cell = obj[0]
                output_grid[top_cell[0], top_cell[1] + 1] = 1

    return output_grid