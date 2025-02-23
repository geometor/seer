"""
1. Identify Azure L-shapes: Find all azure (color 8) objects in the input grid. These objects are L-shaped, consisting of three cells.

2. Determine L-shape Orientation: For each azure L-shape, determine its orientation. There are four possible orientations:
    *   Top-Left: The corner cell is at the top-left. The L extends down and right.
    *   Top-Right: The corner cell is at the top-right. The L extends down and left.
    *   Bottom-Left: The corner cell is at the bottom-left. The L extends up and right.
    *   Bottom-Right: The corner cell is at the bottom-right. The L extends up and left.

3. Place Blue Cells based on Orientation:
    *   Top-Left: Place a blue (color 1) cell immediately to the *right* of the rightmost cell of the L-shape.
    *   Top-Right: Place a blue (color 1) cell immediately to the *left* of the leftmost cell of the L-shape.
    *   Bottom-Left: Place a blue (color 1) cell immediately to the *right* of the rightmost cell of the L-shape.
    *   Bottom-Right: Place a blue (color 1) cell immediately to the *left* of the leftmost cell of the L-shape.

4. Preserve existing objects: The initial azure objects are preserved in the output grid.
"""

import numpy as np

def find_objects(grid, color):
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

def get_l_shape_orientation(obj):
    # Find the corner of the L-shape
    rows, cols = zip(*obj)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    if len(set(rows)) == 2 and len(set(cols)) == 2:  # It's an L-shape
        # Find the corner cell: it appears in both min/max row and col lists
        if rows.count(min_row) > 1:
            corner_row = max_row
        else:
            corner_row = min_row

        if cols.count(min_col) > 1:
            corner_col = max_col
        else:
            corner_col = min_col
        
        # Determine orientation based on corner and other cells
        if corner_row == min_row and corner_col == min_col:
            return "Top-Left"
        elif corner_row == min_row and corner_col == max_col:
            return "Top-Right"
        elif corner_row == max_row and corner_col == min_col:
            return "Bottom-Left"
        elif corner_row == max_row and corner_col == max_col:
            return "Bottom-Right"
    return None  # Not a valid L-shape

def transform(input_grid):
    # Initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)

    # Find the azure objects
    azure_objects = find_objects(input_grid, 8)

    # Process each L-shape
    for obj in azure_objects:
        if len(obj) != 3:  # Ensure it's an L-shape (3 cells)
            continue

        orientation = get_l_shape_orientation(obj)
        if orientation is None:
            continue

        rows, cols = zip(*obj)

        if orientation == "Top-Left" or orientation == "Bottom-Left":
            # Place blue cell to the right of the rightmost cell
            rightmost_col = max(cols)
            rightmost_row = rows[cols.index(rightmost_col)]
            if rightmost_col + 1 < output_grid.shape[1]:
                output_grid[rightmost_row, rightmost_col + 1] = 1
        elif orientation == "Top-Right" or orientation == "Bottom-Right":
            # Place blue cell to the left of the leftmost cell
            leftmost_col = min(cols)
            leftmost_row = rows[cols.index(leftmost_col)]

            if leftmost_col - 1 >= 0:
                output_grid[leftmost_row, leftmost_col - 1] = 1
    return output_grid