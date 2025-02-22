import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of a specified color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        """Depth-first search to find contiguous pixels."""
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

def classify_object(obj):
    """Classifies an object as a 2x1 bar or a 2x2 square or other."""
    rows = [p[0] for p in obj]
    cols = [p[1] for p in obj]
    height = max(rows) - min(rows) + 1
    width = max(cols) - min(cols) + 1

    if height == 2 and width == 1:
        return "2x1_bar"
    elif height == 2 and width == 2:
        return "2x2_square"
    else:
        return "other"


def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.copy(input_grid)  # Start with a copy of the input grid
    azure_objects = find_objects(input_grid, 8)  # Find all azure objects
    width = input_grid.shape[1]
    middle_column = width // 2

    for obj in azure_objects:
        object_type = classify_object(obj)
        rows = [r for r, c in obj]
        cols = [c for r, c in obj]
        min_row = min(rows)
        max_row = max(rows)
        min_col = min(cols)

        if object_type == "2x1_bar":
            if min_col < middle_column:  # Left half
                output_grid[min_row, min_col] = 1
            else:  # Right half
                output_grid[max_row, min_col] = 1
        elif object_type == "2x2_square":
            output_grid[min_row, min_col] = 1

    return output_grid