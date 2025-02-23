"""
Preserve azure (8) pixels and apply an alternating pattern to other color regions, with border pixels taking the color of adjacent objects of different colors.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous regions of the same color, excluding white (0).
    Returns a dictionary: {color: [list of (row, col) coordinates]}.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, color, coords):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        coords.append((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, color, coords)

    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and (r, c) not in visited:
                coords = []
                dfs(r, c, color, coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(coords)
    return objects

def get_bounding_box(coords):
    """
    Calculates the bounding box for a set of coordinates.
    Returns (min_row, min_col, max_row, max_col).
    """
    min_r = min(r for r, c in coords)
    max_r = max(r for r, c in coords)
    min_c = min(c for r, c in coords)
    max_c = max(c for r, c in coords)
    return min_r, min_c, max_r, max_c

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects
    objects = get_objects(input_grid)

    # 2. Preserve Azure (8) - already handled

    # 3. Process Other Colors
    for color, obj_list in objects.items():
        if color == 8:
            continue

        for obj_coords in obj_list:
            # Border Handling
            for r, c in obj_coords:
                neighbor_color = None
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr, nc] != color and grid[nr,nc] != 0 and grid[nr,nc] != 8:
                                neighbor_color = grid[nr, nc]
                                break
                    if neighbor_color is not None:
                        break
                if neighbor_color is not None:
                    output_grid[r, c] = neighbor_color

            # Interior Alternating Pattern (after border handling)
            min_r, min_c, max_r, max_c = get_bounding_box(obj_coords)
            for r, c in obj_coords:
                if output_grid[r,c] == color: # Check if it's still the original color (not a border)
                    if (r - min_r + c - min_c) % 2 == 1:
                        output_grid[r, c] = 0

    return output_grid