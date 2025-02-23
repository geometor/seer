# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The transformation preserves the azure (8) objects and adds blue (1) cells immediately:
* to the right of the first element of vertical azure lines,
* to the left of the second element of horizontal lines.
* to the left of the element on the vertex of "L"-shaped objects.
"""

import numpy as np

def find_objects(grid, color):
    # Find objects of a specific color in the grid.
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

        # Check all 4 directions (up, down, left, right)
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def check_line_orientation(obj):

    if len(obj) < 2:
        return "point"  # Not a line

    # Extract row and column coordinates
    rows, cols = zip(*obj)

    if len(set(rows)) == 1:
        return "horizontal"  # All rows are the same
    elif len(set(cols)) == 1:
        return "vertical"  # All columns are the same
    else:
        return "diagonal"

def is_l_shaped(obj):
    if len(obj) != 3:
        return False

    rows, cols = zip(*obj)
    row_counts = {}
    col_counts = {}

    for r in rows:
        row_counts[r] = row_counts.get(r, 0) + 1
    for c in cols:
        col_counts[c] = col_counts.get(c, 0) + 1

    # Check for exactly two rows and two cols, with one of each having a count of 2 and the other a count of 1.
    if len(row_counts) != 2 or len(col_counts) != 2:
      return False

    return 2 in row_counts.values() and 1 in row_counts.values() and 2 in col_counts.values() and 1 in col_counts.values()

def find_l_vertex(obj):
    #Find vertex for an L-shaped object
    rows, cols = zip(*obj)
    row_counts = {}
    col_counts = {}

    for r in rows:
      row_counts[r] = row_counts.get(r,0) + 1
    for c in cols:
      col_counts[c] = col_counts.get(c,0) + 1

    vertex_row = [r for r, count in row_counts.items() if count == 1][0]
    vertex_col = [c for c, count in col_counts.items() if count == 1][0]

    return (vertex_row, vertex_col)
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)

    # Preserve azure objects and add blue cells based on their positions
    for obj in azure_objects:
        orientation = check_line_orientation(obj)

        if orientation == "vertical":
            first_element = obj[0]
            r, c = first_element
            if c + 1 < cols and output_grid[r, c + 1] != 8:
                 output_grid[r, c + 1] = 1  # Paint blue to the right

        elif orientation == "horizontal":

            second_element = obj[1]
            r,c = second_element
            if c - 1 >= 0 and output_grid[r, c - 1] != 8:
                 output_grid[r, c-1] = 1 # Paint blue to the left

        elif is_l_shaped(obj):
            vertex = find_l_vertex(obj)
            r,c = vertex
            if c - 1 >= 0 and output_grid[r,c-1] != 8:
                output_grid[r,c-1] = 1

    return output_grid
```

