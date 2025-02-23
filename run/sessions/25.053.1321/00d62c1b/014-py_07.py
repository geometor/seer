"""
1.  **Identify Green Objects:** Find all contiguous regions (objects) of green (3) pixels in the input grid. Consider pixels connected if they share an edge (4-connectivity).
2.  **Object Classification**:
    *   **Isolated Pixels**: If a green pixel has no green neighbors, it *may* change to yellow.
    *   **Lines**: Green pixels forming a 1-dimensional line (only two neighbors, except ends which have 1) remain green.
    *  **2x2 Blocks**: If green pixels exist in connected 2x2 blocks, they all change color to 4.
    *  **Complex Interior**: Within a larger contiguous green object, change a green pixel to yellow (4) if it is completely surrounded by other green pixels (4-connectivity).
3.  **Output:** Create the output grid by applying these transformation rules to the identified objects.
"""

import numpy as np

def find_objects(grid, color):
    """Finds all contiguous objects of a given color."""
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
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def count_neighbors(grid, r, c, color):
    """Counts the number of neighbors of a given color."""
    rows, cols = grid.shape
    count = 0
    neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    for nr, nc in neighbors:
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            count += 1
    return count

def is_2x2_block(grid, r, c, color):
    """check for 2x2 block"""
    rows, cols = grid.shape

    if (r + 1 < rows and c + 1 < cols):
        if (grid[r+1,c] == color and
            grid[r,c+1] == color and
            grid[r+1,c+1] == color):

            return True

    return False

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find green objects
    green_objects = find_objects(input_grid, 3)

    for obj in green_objects:
      for r,c in obj:
        # 2x2 block check
        if is_2x2_block(input_grid, r, c, 3):
          output_grid[r,c] = 4
          output_grid[r+1,c] = 4
          output_grid[r,c+1] = 4
          output_grid[r+1,c+1] = 4

        # Complex interior check
        elif count_neighbors(input_grid, r, c, 3) == 4:
            output_grid[r, c] = 4

    return output_grid