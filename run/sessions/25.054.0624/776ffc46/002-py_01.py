"""
Identify red "cross" shapes and blue "L" or rectangular shapes.
Swap the colors of the red and blue objects, while leaving gray (5) and white (0) pixels unchanged.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a given color
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] == color:
                obj = []
                stack = [(r, c)]
                visited[r, c] = True

                while stack:
                    curr_r, curr_c = stack.pop()
                    obj.append((curr_r, curr_c))

                    neighbors = [
                        (curr_r - 1, curr_c),
                        (curr_r + 1, curr_c),
                        (curr_r, curr_c - 1),
                        (curr_r, curr_c + 1),
                    ]
                    for nr, nc in neighbors:
                        if (0 <= nr < rows and 0 <= nc < cols and
                                not visited[nr, nc] and grid[nr, nc] == color):
                            stack.append((nr, nc))
                            visited[nr, nc] = True
                objects.append(obj)
    return objects

def transform(input_grid):
    # Initialize output grid with the same dimensions and background.
    output_grid = np.copy(input_grid)

    # Find red and blue objects.
    red_objects = find_objects(input_grid, 2)
    blue_objects = find_objects(input_grid, 1)

    # keep the objects colors, do not swap
    # do not need to do anything for this.

    return output_grid