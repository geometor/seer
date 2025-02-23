"""
The transformation rule involves identifying distinct objects in the input grid, and then creating copies to the right by a fixed amount.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all distinct objects in a grid.
    Returns a dictionary where keys are colors and values are lists of (row, col) coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and (r, c) not in visited:
                if color not in objects:
                    objects[color] = []
                stack = [(r, c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    if (curr_r, curr_c) in visited:
                        continue
                    visited.add((curr_r, curr_c))
                    objects[color].append((curr_r, curr_c))
                    # Check neighbors (up, down, left, right)
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color and (nr, nc) not in visited:
                            stack.append((nr, nc))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the rule.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    # Calculate offsets and build transformed shape
    for color, pixels in objects.items():
      if color == 0:
        continue

      min_col = min(c for _, c in pixels)
      object_width = max(c for _,c in pixels) - min_col + 1

      for r, c in pixels:
        output_grid[r, c + object_width] = color

    return output_grid.tolist()