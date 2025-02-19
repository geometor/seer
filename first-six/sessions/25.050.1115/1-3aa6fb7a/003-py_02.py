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
    return max(obj, key=lambda cell:cell[0])

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    azure_objects.sort(key=lambda obj: (get_top_cell(obj)[0], get_top_cell(obj)[1]))

    if len(azure_objects) >= 3:
        top_right_object = azure_objects[-1]  # Select the object in the top-right
        middle_left_object = azure_objects[1] #Select the object in the middle
        bottom_object = azure_objects[0] #select the object in the bottom

        # Top-right object: Change cell to the left of the bottom cell
        bottom_cell = get_bottom_cell(top_right_object)
        left_of_bottom = (bottom_cell[0], bottom_cell[1] - 1)
        if (
            0 <= left_of_bottom[0] < output_grid.shape[0]
            and 0 <= left_of_bottom[1] < output_grid.shape[1]
            and output_grid[left_of_bottom] == 0
        ):
            output_grid[left_of_bottom] = 1

        # Middle-left object: Change cell to the right of the top cell.
        top_cell = get_top_cell(middle_left_object)
        right_of_top = (top_cell[0], top_cell[1] + 1)
        if (
            0 <= right_of_top[0] < output_grid.shape[0]
            and 0 <= right_of_top[1] < output_grid.shape[1]
            and output_grid[right_of_top] == 0
            ):
            output_grid[right_of_top]=1

        # Bottom object: Change the cell to the left of the top cell.
        top_cell = get_top_cell(bottom_object)
        left_of_top = (top_cell[0], top_cell[1] -1)

        if (
             0 <=  left_of_top[0] < output_grid.shape[0]
            and 0 <= left_of_top[1] < output_grid.shape[1]
            and output_grid[left_of_top] == 0
        ):
            output_grid[left_of_top] = 1

    return output_grid