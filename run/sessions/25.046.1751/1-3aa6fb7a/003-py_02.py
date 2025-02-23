import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    def get_neighbors(r, c):
        neighbors = []
        if r > 0:
            neighbors.append((r - 1, c))  # Up
        if r < rows - 1:
            neighbors.append((r + 1, c))  # Down
        if c > 0:
            neighbors.append((r, c - 1))  # Left
        if c < cols - 1:
            neighbors.append((r, c + 1))  # Right
        return neighbors

    def dfs(r, c, current_object):
        visited[r, c] = True
        current_object.append((r, c))
        for nr, nc in get_neighbors(r, c):
            if input_grid[nr, nc] == 8 and not visited[nr, nc]:
                dfs(nr, nc, current_object)

    objects = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8 and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)

    for obj in objects:
        top_most_row = rows  # Initialize with a large value
        top_most_col = -1
        for r, c in obj:
            if r < top_most_row:
                top_most_row = r
                top_most_col = c

        if top_most_col + 1 < cols:  # Check if adding to the right is possible
           output_grid[top_most_row, top_most_col + 1] = 1

    return output_grid