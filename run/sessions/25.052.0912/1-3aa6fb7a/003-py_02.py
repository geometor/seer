import numpy as np

def is_l_shape(pixels, grid):
    """Checks if a set of pixels forms an L-shape."""
    if len(pixels) != 3:
        return False

    # Convert list of tuples to numpy array for easier manipulation
    pixels_arr = np.array(pixels)

    # Find the pixel that has two neighbors
    for i, (x, y) in enumerate(pixels):
        neighbors = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x + dx, y + dy) in pixels:
                neighbors += 1
        if neighbors == 2:
            return True, (x, y)
    return False, None

def find_objects(grid, color):
    """Finds connected components of a specific color."""
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
                objects.append(current_object)
    return objects

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    output_grid = np.copy(input_grid)
    azure_objects = find_objects(output_grid, 8)

    for obj in azure_objects:
        is_l, corner_pixel = is_l_shape(obj, output_grid)
        if is_l:
            output_grid[corner_pixel] = 1

    return output_grid