"""
1. Object Identification: Identify all contiguous regions of the same color as distinct objects. Record their color, bounding box (min/max row and column), and an approximate shape description.
2. Expansion/Fill: If there is an object, expand the object by 1 pixel on all sides.
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

def get_bounding_box(pixels):
    """
    Calculates the bounding box of a set of pixels.
    """
    min_row = min(r for r, _ in pixels)
    max_row = max(r for r, _ in pixels)
    min_col = min(c for _, c in pixels)
    max_col = max(c for _, c in pixels)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # find objects in the input grid
    input_objects = find_objects(input_grid)

    # expand each object
    for color, pixels in input_objects.items():
        min_row, max_row, min_col, max_col = get_bounding_box(pixels)

        # expand borders
        new_min_row = max(0, min_row - 1)
        new_max_row = min(rows - 1, max_row + 1)
        new_min_col = max(0, min_col - 1)
        new_max_col = min(cols - 1, max_col + 1)

        # fill the expanded region in output grid
        for r in range(new_min_row, new_max_row + 1):
            for c in range(new_min_col, new_max_col + 1):
                output_grid[r, c] = color
    
    return output_grid