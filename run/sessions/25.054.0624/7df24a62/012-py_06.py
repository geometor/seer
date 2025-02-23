"""
Preserves all yellow pixels and moves any blue shape to the highest possible position in the output grid without overlapping other non-black pixels.
"""

import numpy as np

def find_blue_shapes(grid):
    """Finds all contiguous blue shapes in the grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    blue_shapes = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, shape):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != 1:
            return
        visited[r, c] = True
        shape.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1 and not visited[r, c]:
                shape = []
                dfs(r, c, shape)
                if shape:
                    blue_shapes.append(shape)
    return blue_shapes

def get_shape_bounds(shape):
    """Calculates the bounding box of a shape."""
    min_row = min(p[0] for p in shape)
    max_row = max(p[0] for p in shape)
    min_col = min(p[1] for p in shape)
    max_col = max(p[1] for p in shape)
    return min_row, max_row, min_col, max_col

def can_place_shape(grid, shape, target_row, target_col):
    """Checks if a shape can be placed at the target location without overlapping existing non-black pixels."""
    rows, cols = grid.shape
    min_row, max_row, min_col, max_col = get_shape_bounds(shape)
    shape_height = max_row - min_row + 1
    shape_width = max_col - min_col + 1

    if target_row < 0 or target_row + shape_height > rows or target_col < 0 or target_col + shape_width > cols:
        return False

    for r in range(shape_height):
        for c in range(shape_width):
            original_r = min_row + r
            original_c = min_col + c
            #check within the bounds of original shape
            if (original_r, original_c) in shape:
               if grid[target_row + r, target_col + c] != 0:
                   return False  # Overlap with a non-black pixel
    return True

def place_shape(grid, shape, target_row, target_col):
    """Places the shape at the target location."""

    min_row, max_row, min_col, max_col = get_shape_bounds(shape)
    for r in range(max_row - min_row + 1):
        for c in range(max_col - min_col + 1):
            if (min_row + r, min_col + c) in shape:
                grid[target_row + r, target_col + c] = 1



def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Preserve yellow pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 4:
                output_grid[r, c] = 4

    # Find blue shapes
    blue_shapes = find_blue_shapes(input_grid)

    # Move blue shapes to the top
    for shape in blue_shapes:
        min_row, max_row, min_col, max_col = get_shape_bounds(shape)
        shape_width = max_col - min_col +1
        # Find the highest possible position for the shape
        target_row = 0
        target_col = min_col

        while not can_place_shape(output_grid, shape, target_row, target_col):
            target_row += 1
            if target_row + (max_row-min_row) >= rows:
              break # shape cannot be placed

        # Place the shape
        if target_row + (max_row-min_row) < rows:
            place_shape(output_grid, shape, target_row, target_col)

    return output_grid