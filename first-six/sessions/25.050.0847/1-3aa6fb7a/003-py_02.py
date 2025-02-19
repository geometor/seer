"""
The transformation rule identifies three specific azure (color 8) clusters: a 2x1 horizontal, a 1x2 vertical and a 2x1 horizontal azure colored clusters. A blue cell (color 1) is placed immediately to the left of the top cell of the 2x1 cluster.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()
    rows, cols = grid.shape
    
    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
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
                
def is_1x2_vertical(obj):
    if len(obj) != 2:
        return False
    obj.sort()
    return obj[1][0] == obj[0][0] + 1 and obj[1][1] == obj[0][1]

def is_2x1_horizontal(obj):
    if len(obj) != 2:
        return False
    obj.sort()
    return obj[1][1] == obj[0][1] + 1 and obj[1][0] == obj[0][0]
    

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through azure objects and identify 1x2 and 2x1 clusters
    for obj in azure_objects:
        if is_1x2_vertical(obj):
            # Place a blue cell to the right of the top cell
            top_cell = sorted(obj)[0]
            if top_cell[1] + 1 < cols:
                output_grid[top_cell[0], top_cell[1] + 1] = 1
        elif is_2x1_horizontal(obj):
            # Place a blue cell to the left of the top cell
            top_cell = sorted(obj)[0]
            if top_cell[1] -1 >=0 :
               
                 output_grid[top_cell[0] , top_cell[1] -1] = 1

    return output_grid