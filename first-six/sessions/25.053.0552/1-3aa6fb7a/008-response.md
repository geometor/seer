# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
The program consists of finding all azure L-shaped objects, and inserting a
blue pixel inside each "L". The blue pixel is placed diagonally adjacent to
the corner pixel of the L.
"""

import numpy as np

def find_l_shapes(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return

        visited.add((r, c))
        current_object.append((r, c))

        neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)
    
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] == color and (r,c) not in visited:
                current_object = []
                dfs(r,c,current_object)

                if len(current_object) == 3:
                    objects.append(current_object)
    return objects

def find_corner(l_shape):
    # Find the corner pixel of an L-shape (list of 3 (r,c) tuples)
    for p1 in l_shape:
        count = 0
        for p2 in l_shape:
            if p1 == p2:
                continue
            if p1[0] == p2[0] or p1[1] == p2[1]:
                count += 1
        if count == 2:
            return p1
    return None # Should never happen, but handle for safety


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find azure L-shapes
    azure_l_shapes = find_l_shapes(input_grid, 8)

    # Add a blue pixel inside each azure L-shape
    for l_shape in azure_l_shapes:
        # Find the corner pixel
        corner = find_corner(l_shape)

        # Determine insertion point (diagonally adjacent to corner)
        row_neighbors = []
        col_neighbors = []
        for r, c in l_shape:
            if (r,c) != corner:
                if r == corner[0]:
                    row_neighbors.append((r,c))
                elif c == corner[1]:
                    col_neighbors.append((r,c))
        
        #calculate insert position
        insert_row = 0
        insert_col = 0

        if row_neighbors[0][1] > corner[1]:
            insert_col = corner[1] + 1
        else:
            insert_col = corner[1] - 1

        if col_neighbors[0][0] > corner[0]:
            insert_row = corner[0] + 1
        else:
            insert_row = corner[0] -1

        # Place blue pixel
        output_grid[insert_row, insert_col] = 1
    return output_grid
```
