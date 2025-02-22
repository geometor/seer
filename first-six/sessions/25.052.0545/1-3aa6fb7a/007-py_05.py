import numpy as np

def find_objects(grid, color):
    """Finds contiguous regions of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == color and not visited[i, j]:
                obj = []
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    if 0 <= r < rows and 0 <= c < cols and grid[r, c] == color and not visited[r, c]:
                        visited[r, c] = True
                        obj.append((r, c))
                        stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
                objects.append(obj)
    return objects

def is_l_shape(obj):
    """Checks if the object is an L-shape (not rotated)."""
    if len(obj) != 3:
        return False

    coords = np.array(obj)
    # Sort coordinates to handle different L orientations
    coords = coords[coords[:, 0].argsort()] #sort by row

    #check for [[r,c],[r+1,c],[r+1,c+1]]
    if coords[0,0] == coords[1,0] -1 and \
       coords[0,1] == coords[1,1] and \
       coords[1,0] == coords[2,0] and \
       coords[1,1] == coords[2,1] -1:
        return True

    coords = coords[coords[:, 1].argsort()] #sort by col
    #check for [[r,c],[r,c+1],[r+1,c+1]]
    if coords[0,0] == coords[1,0] and \
       coords[0,1] == coords[1,1] -1 and \
       coords[1,0] == coords[2,0] -1 and \
       coords[1,1] == coords[2,1]:
        return True

    return False

def find_insertion_point(obj):
    """Finds the insertion point for the blue pixel."""
    coords = np.array(obj)

    coords_row_sorted = coords[coords[:, 0].argsort()] #sort by row
     #check for [[r,c],[r+1,c],[r+1,c+1]]
    if coords_row_sorted[0,0] == coords_row_sorted[1,0] -1 and \
       coords_row_sorted[0,1] == coords_row_sorted[1,1] and \
       coords_row_sorted[1,0] == coords_row_sorted[2,0] and \
       coords_row_sorted[1,1] == coords_row_sorted[2,1] -1:
        return (coords_row_sorted[2,0],coords_row_sorted[2,1]+1)

    coords_col_sorted = coords[coords[:, 1].argsort()] #sort by col
    #check for [[r,c],[r,c+1],[r+1,c+1]]
    if coords_col_sorted[0,0] == coords_col_sorted[1,0] and \
       coords_col_sorted[0,1] == coords_col_sorted[1,1] -1 and \
       coords_col_sorted[1,0] == coords_col_sorted[2,0] -1 and \
       coords_col_sorted[1,1] == coords_col_sorted[2,1]:
        return (coords_col_sorted[1,0],coords_col_sorted[1,1]+1)
    return None

def transform(input_grid):
    """Transforms the input grid according to the rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        if is_l_shape(obj):
            insertion_point = find_insertion_point(obj)
            if insertion_point:
                row, col = insertion_point
                if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1]:
                    output_grid[row, col] = 1
    return output_grid