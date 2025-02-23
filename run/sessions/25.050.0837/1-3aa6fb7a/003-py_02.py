import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates for each object.
    """
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
    
def find_leftmost(object_coords):
    """
    Finds and returns the leftmost coordinate of a set of object coordinates
    """
    if not object_coords:
        return None
    
    leftmost_coord = object_coords[0]
    
    for coord in object_coords:
        if coord[1] < leftmost_coord[1]:
            leftmost_coord = coord

    return [leftmost_coord]

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule:
    - Finds azure (color 8) objects.
    - For each object with 2 cells, the leftmost cell is turned blue.
    - Keeps all other cells the same.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        if len(obj) == 2:
            leftmost = find_leftmost(obj)
            for coord in leftmost:
                output_grid[coord] = 1
    return output_grid