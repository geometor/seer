"""
1.  **Find Azure Objects:** Identify all distinct, contiguous regions of azure (8) pixels in the input grid.  A contiguous region is defined as a group of azure pixels connected horizontally or vertically.

2.  **Identify Top-Left and Bottom-Right Objects:**
    *   **Top-Left Object:** The object with the smallest top-most row index. If multiple objects share the same top-most row, the one with the smallest left-most column index is the top-left.
    *   **Bottom-Right Object:** The object with the largest bottom-most row index. If multiple objects share the same bottom-most row, select the one with the largest right-most column index.

3.  **Place Blue Pixel near Top-Left Object:**  Find the right-most pixel of the top-most row of the top-left azure object. Place a blue (1) pixel immediately to the *right* of this pixel. If this position is outside the grid, do not place a pixel for this rule.

4.  **Place Blue Pixel near Bottom-Right Object:** Find the top-left corner pixel of the bottom-right azure object (smallest row, smallest column within that object). Place a blue (1) pixel immediately *above* this pixel. If this position is outside the grid boundaries, do not place a pixel for this rule.

5. **Preserve Azure:** All azure pixels from the input must be in the output.

6.  **Output:** Return the modified grid with the added blue pixels (if any).
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_top_left_and_bottom_right_objects(objects):
    if not objects:
        return None, None

    # Find top-left object
    top_left_object = min(objects, key=lambda obj: (min(r for r, c in obj), min(c for r, c in obj if r == min(row for row, _ in obj))))

    # Find bottom-right object
    bottom_right_object = max(objects, key=lambda obj: (max(r for r, c in obj), max(c for r, c in obj if r == max(row for row, _ in obj))))
    
    return top_left_object, bottom_right_object


def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Find top-left and bottom-right azure objects
    top_left_object, bottom_right_object = find_top_left_and_bottom_right_objects(azure_objects)

    # Place blue pixel near top-left object
    if top_left_object:
        top_row = min(r for r, c in top_left_object)
        right_most_col = max(c for r, c in top_left_object if r == top_row)
        if right_most_col + 1 < cols:
            output_grid[top_row, right_most_col + 1] = 1

    # Place blue pixel near bottom-right object
    if bottom_right_object:
        top_left_corner_r = min(r for r, c in bottom_right_object)
        top_left_corner_c = min(c for r, c in bottom_right_object if r == top_left_corner_r )
        if top_left_corner_r - 1 >= 0:
            output_grid[top_left_corner_r - 1, top_left_corner_c] = 1

    return output_grid