"""
The transformation rule identifies 'L' shaped objects of color 8 (azure) in the input grid and adds a single cell of color 1 (blue) adjacent to them based on their orientation. The azure objects are preserved in their original positions. If the 'L' shape is oriented towards the top-left, a blue cell is added to its right. If the 'L' shape is oriented towards the bottom-right, a blue cell is added to its left.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds the coordinates of objects of a specific color.
    An object is defined as a contiguous region of the same color.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        # Check all 4 directions
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        # Sort the coordinates to identify top-left and bottom-right objects
        obj.sort()
        
        if len(obj) == 3: # Check that it is the "L" shape
            # Determine if it's top-left or bottom-right based on coordinates
            # Top-left object: min row and min col
            # Bottom-right object: max row and max col
            # The L-shape objects in question don't follow the top-leftmost or bottom-rightmost logic strictly.
            # Instead, we'll check the relative positions of the azure cells directly

            min_row = min(r for r, c in obj)
            min_col = min(c for r, c in obj)
            max_row = max(r for r, c in obj)
            max_col = max(c for r, c in obj)

            # Assuming that the orientation is deterministic, it is not needed to be adaptive to new orientations.
            if obj == sorted([(min_row,min_col), (min_row, min_col+1), (min_row+1, min_col)]): #top-left or top-right
                # Add blue cell to the right
              if min_row >= 0 and min_row < output_grid.shape[0] and min_col + 2 >= 0 and min_col + 2 < output_grid.shape[1]:
                if output_grid[min_row, min_col + 2] == 0:
                  output_grid[min_row, min_col + 2] = 1

            elif obj == sorted([(max_row-1, max_col), (max_row, max_col-1), (max_row, max_col)]): # bottom-right or bottom-left
                # Add blue cell to the left
              if max_row >= 0 and max_row < output_grid.shape[0] and max_col-2 >=0 and max_col-2 < output_grid.shape[1]:
                if output_grid[max_row, max_col - 2] == 0:
                    output_grid[max_row, max_col - 2] = 1
            elif obj == sorted([(min_row, max_col-1), (min_row, max_col), (min_row+1, max_col)]):#top-right
                if min_row >= 0 and min_row < output_grid.shape[0] and max_col + 1 >= 0 and max_col+1 < output_grid.shape[1]:
                    if output_grid[min_row,max_col+1] == 0:
                        output_grid[min_row,max_col+1] = 1
            elif obj == sorted([(max_row-1,min_col), (max_row, min_col), (max_row,min_col+1)]):#bottom-left
              if max_row >= 0 and max_row < output_grid.shape[0] and min_col - 1 >= 0 and min_col -1 < output_grid.shape[1] :
                if output_grid[max_row,min_col-1] == 0:
                  output_grid[max_row, min_col -1] = 1

    return output_grid