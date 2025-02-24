"""
Identifies the first "C"-shaped object in the input grid, and returns a 2x2 grid of the same color.
"""

import numpy as np

def get_objects(grid):
    """
    Find contiguous regions of the same color in the grid (excluding white/0).
    Returns a dictionary of objects, where keys are colors and values are lists of pixel coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj_pixels):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or (row, col) in visited
            or grid[row, col] != color
        ):
            return
        visited.add((row, col))
        obj_pixels.append((row, col))
        dfs(row + 1, col, color, obj_pixels)
        dfs(row - 1, col, color, obj_pixels)
        dfs(row, col + 1, color, obj_pixels)
        dfs(row, col - 1, color, obj_pixels)

    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and (r, c) not in visited:
                obj_pixels = []
                dfs(r, c, color, obj_pixels)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_pixels)
    return objects

def analyze_object(obj_pixels):
    """
    Analyzes a single object (list of pixel coordinates) to determine if it's C-shaped.
    """
    if not obj_pixels:
        return False

    min_row = min(p[0] for p in obj_pixels)
    max_row = max(p[0] for p in obj_pixels)
    min_col = min(p[1] for p in obj_pixels)
    max_col = max(p[1] for p in obj_pixels)

    width = max_col - min_col + 1
    height = max_row - min_row + 1

    if width > 2 and height > 2:
        # Check for a "C" shape
        top_line = all((min_row, c) in obj_pixels for c in range(min_col, max_col + 1))
        bottom_line = all((max_row, c) in obj_pixels for c in range(min_col, max_col + 1))
        left_line = all((r, min_col) in obj_pixels for r in range(min_row, max_row + 1))
        top_right = (min_row, max_col) not in obj_pixels
        bottom_right = (max_row, max_col) not in obj_pixels

        if top_line and bottom_line and left_line and top_right and bottom_right:
            return True

    return False

def transform(input_grid):
    # Find objects in the input grid.
    objects = get_objects(input_grid)

    # Find the first C-shaped object and its color.
    c_shape_color = None
    for color, obj_list in objects.items():
        for obj_pixels in obj_list:
            if analyze_object(obj_pixels):
                c_shape_color = color
                break  # Stop after finding the first C-shaped object
        if c_shape_color is not None:
            break

    # If no C-shaped object is found, return a minimal empty grid.
    if c_shape_color is None:
        return np.array([[0]])

    # Create a 2x2 output grid with the C-shape's color.
    output_grid = np.full((2, 2), c_shape_color)

    return output_grid