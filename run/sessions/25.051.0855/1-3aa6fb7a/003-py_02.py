import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
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

def is_vertical_line(obj):
    rows = sorted(list(set([cell[0] for cell in obj])))
    cols = sorted(list(set([cell[1] for cell in obj])))
    if len(cols) == 1 and len(rows) > 1:
        return True

    return False


def is_horizontal_line(obj):
    rows = sorted(list(set([cell[0] for cell in obj])))
    cols = sorted(list(set([cell[1] for cell in obj])))
    if len(rows) == 1 and len(cols) > 1:
        return True
    return False


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()
    objects_8 = find_objects(input_grid, 8)

    for obj in objects_8:
      if is_vertical_line(obj):
        top_row = min(cell[0] for cell in obj)
        top_col = obj[0][1]

        if top_row > 0 and input_grid[top_row - 1, top_col] == 0:  # Check for white (0) above
            output_grid[top_row -1, top_col] = 1

      elif is_horizontal_line(obj):
        left_col = min(cell[1] for cell in obj)
        left_row = obj[0][0]
        if left_col > 0 and input_grid[left_row, left_col - 1] == 0:  # Check for white (0) to the left
          output_grid[left_row, left_col - 1] = 1
    return output_grid