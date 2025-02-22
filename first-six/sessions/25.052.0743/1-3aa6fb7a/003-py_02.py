import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return []

        visited[row, col] = True
        region = [(row, col)]

        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))

        return region

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                objects.append(dfs(row, col))

    return objects

def find_l_shape_elbow(object_pixels):
    for row, col in object_pixels:
        neighbors = 0
        # Check up, down, left, right
        if (row - 1, col) in object_pixels:
            neighbors += 1
        if (row + 1, col) in object_pixels:
            neighbors += 1
        if (row, col - 1) in object_pixels:
            neighbors += 1
        if (row, col + 1) in object_pixels:
            neighbors += 1
        if neighbors == 2:
            return (row, col)
    return None  # Should not happen for a valid L-shape

def transform(input_grid):
    output_grid = input_grid.copy()
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        if len(obj) == 3:  # Ensure it's an L-shape
            elbow = find_l_shape_elbow(obj)
            if elbow:
                row, col = elbow
                # Check adjacent cells and place blue pixel if empty and not part of the L
                if (row - 1, col) not in obj and row - 1 >= 0 and output_grid[row-1, col] == 0:
                    output_grid[row - 1, col] = 1
                elif (row + 1, col) not in obj and row + 1 < output_grid.shape[0] and output_grid[row+1, col] == 0:
                    output_grid[row + 1, col] = 1
                elif (row, col - 1) not in obj and col -1 >= 0 and output_grid[row, col-1] == 0:
                    output_grid[row, col - 1] = 1
                elif (row, col + 1) not in obj and col + 1 < output_grid.shape[1] and output_grid[row, col+1] == 0:
                    output_grid[row, col + 1] = 1

    return output_grid