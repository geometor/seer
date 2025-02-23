"""
1.  **Identify Green Regions:** Find all contiguous regions (objects) of green pixels.  Pixels are considered connected if they share an edge (4-connectivity).

2.  **Prioritize 2x2 Blocks:** Within each green region, check *every* green pixel to see if it is the top-left corner of a 2x2 block of green pixels. If it is, change *all four* pixels in that 2x2 block to yellow (value 4).

3.  **Identify Boundaries:** For each green region, determine its boundary pixels. A boundary pixel is a green pixel that has at least one neighbor (4-connectivity) that is *not* green.

4. **Fill Interior with Yellow**: For each green region change green pixels to yellow if all neighbors are part of the same green object AND it is NOT part of a 2x2 block.

5.  **Output:** Create the output grid by applying these transformation rules. All unchanged pixels retain original values.
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

def is_2x2_block(grid, r, c, color):
    """check for 2x2 block"""
    rows, cols = grid.shape

    if (r + 1 < rows and c + 1 < cols):
        if (grid[r+1,c] == color and
            grid[r,c+1] == color and
            grid[r+1,c+1] == color):

            return True

    return False

def get_neighbors(grid, r, c):
    """Returns the valid neighbors of a cell (4-connectivity)."""
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def is_boundary(grid, r, c, object_pixels):
    """Checks if a pixel is on the boundary of its object."""
    for nr, nc in get_neighbors(grid, r, c):
        if (nr, nc) not in object_pixels:
            return True
    return False


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find green objects
    green_objects = find_objects(input_grid, 3)
    
    # 2. Handle 2x2 blocks (priority)
    for obj in green_objects:
        for r, c in obj:
            if is_2x2_block(input_grid, r, c, 3):
                output_grid[r, c] = 4
                output_grid[r + 1, c] = 4
                output_grid[r, c + 1] = 4
                output_grid[r + 1, c + 1] = 4

    # Create sets for faster lookup
    green_object_sets = [set(obj) for obj in green_objects]

    # Re-iterate to handle the fill operation.  Need to do this *after* 2x2 blocks.
    for obj_set in green_object_sets:
        for r, c in obj_set:

            # Skip if already changed by 2x2 rule
            if output_grid[r,c] == 4:
                continue

            # 3. and 4. Check if it's an interior pixel and not part of a 2x2 block.
            if not is_boundary(input_grid, r, c, obj_set):
               output_grid[r,c] = 4

    return output_grid