"""
1.  **Identify Azure Objects:** Locate all distinct, contiguous groups of azure (8) pixels. Each group is considered an "azure object."

2.  **Determine Blue Pixel Placement:** For *each* azure object, find the adjacent (up, down, left or right - *not* diagonal) empty/white (0) cell. If there's only one such position, color this white cell blue (1).

3.  **Output:** The final grid will contain the original azure objects and single blue pixels at positions determined during processing each azure object.
"""

import numpy as np

def get_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_adjacent_white_pixels(grid, object_pixels):
    adjacent_white = []
    for r, c in object_pixels:
        neighbors = [
            (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)
        ]
        for nr, nc in neighbors:
            if (0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and
                    grid[nr, nc] == 0):
                adjacent_white.append((nr, nc))
    return list(set(adjacent_white))  # Remove duplicates


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify azure objects
    azure_objects = get_objects(input_grid, 8)

    # Determine and apply blue pixel placement for each azure object
    for azure_object in azure_objects:
       adjacent_whites = get_adjacent_white_pixels(output_grid, azure_object)
       if len(adjacent_whites) > 0:
            output_grid[adjacent_whites[0]] = 1

    return output_grid