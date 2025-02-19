"""
The transformation preserves the azure (8) L-shaped objects. It adds blue cells adjacent to specific parts of the azure objects: A blue color 1 cell is placed immediately right of uppermost, leftmost cell of the first azure L, and a blue 1 is placed above the bottom most cell of the second azure L.
"""

import numpy as np

def find_top_left_cell(grid, color):
    """Finds the uppermost and leftmost cell of a given color."""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    min_row_index = np.argmin(rows)
    min_col_index = np.argmin(cols)

    min_row = rows[min_row_index]
    indices = np.where(rows == min_row)[0]
    min_col = cols[indices[np.argmin(cols[indices])]]
    return min_row, min_col

def find_bottom_most_cell(grid, color):
    """Finds the bottom-most cell of given color"""
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None
    max_row_index = np.argmax(rows)

    max_row = rows[max_row_index]
    return max_row

def get_l_objects(grid,color):
    """ Get all separated L shaped objects """
    objects = []
    visited = set()
    rows, cols = grid.shape
    
    def is_valid(r,c):
        return 0 <= r < rows and 0 <= c < cols
    
    def dfs(r,c, current_object):
        if (r,c) in visited or not is_valid(r,c) or grid[r,c] != color:
            return
        visited.add((r,c))
        current_object.append((r,c))
        
        dfs(r+1,c,current_object)
        dfs(r-1,c,current_object)
        dfs(r,c+1, current_object)
        dfs(r,c-1,current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == color and (r,c) not in visited:
                current_object = []
                dfs(r,c,current_object)
                objects.append(current_object)
    return objects
        

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    objects = get_l_objects(input_grid,8)
    
    if len(objects) >= 2:
        first_l = objects[0]
        second_l = objects[1]

    # Find top-left of first L
        first_l_rows = [r for r, _ in first_l]
        first_l_cols = [c for _, c in first_l]

        min_row_index = np.argmin(first_l_rows)
        min_row = first_l_rows[min_row_index]

        indices = np.where(np.array(first_l_rows) == min_row)[0]
        min_col = first_l_cols[indices[np.argmin(np.array(first_l_cols)[indices])]]
        top_left_first_l = (min_row, min_col)

      # Place blue cell to the right of the top-left of the first L
        if top_left_first_l[1] + 1 < output_grid.shape[1]:
          output_grid[top_left_first_l[0], top_left_first_l[1] + 1] = 1

        # Find bottom-most cell of second L.

        second_l_rows = [r for r,_ in second_l]
        second_l_cols = [c for _,c in second_l]

        max_row = np.max(second_l_rows)


      # Place blue cell above the bottom-most cell of the second L
        if max_row -1 >= 0:
          output_grid[max_row - 1, second_l_cols[np.where(np.array(second_l_rows) == max_row)[0][0]]] = 1
    

    return output_grid