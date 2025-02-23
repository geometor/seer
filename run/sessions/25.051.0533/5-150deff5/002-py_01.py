"""
The transformation rule can be summarized as follows:

- Replace all gray (5) cells with azure (8) cells.
- Fill the one-cell-thick spaces between azure objects with red (2).
- Ensure that the bounding box of the gray regions in the input is conserved.
"""

import numpy as np

def find_objects(grid, color):
    """
    Find contiguous regions of the specified color.
    Returns a list of objects, where each object is a set of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.add((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = set()
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_bounding_box(objects):
    """
    Compute the bounding box encompassing all objects.
    Returns (min_row, min_col, max_row, max_col).
    """
     
    min_row = min(row for obj in objects for row, _ in obj)
    min_col = min(col for obj in objects for _, col in obj)
    max_row = max(row for obj in objects for row, _ in obj)
    max_col = max(col for obj in objects for _, col in obj)
    return min_row, min_col, max_row, max_col
    

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize output grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find gray objects
    gray_objects = find_objects(input_grid, 5)
    
    # Replace gray with azure
    for obj in gray_objects:
        for row, col in obj:
            output_grid[row, col] = 8

    # Get the bounding box
    min_row, min_col, max_row, max_col = get_bounding_box(gray_objects)

    # Fill spaces between azure objects with red
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col+1):
            if output_grid[r,c] == 8:
                #check right
                if c + 1 < cols and output_grid[r,c+1] == 0:
                    c2 = c + 1
                    while c2 < cols and output_grid[r,c2] == 0:
                        c2 +=1
                    if c2 < cols and output_grid[r,c2] == 8:
                        for k in range(c+1,c2):
                            output_grid[r,k] = 2

                #check down
                if r + 1 < rows and output_grid[r+1,c] == 0:
                    r2 = r + 1
                    while r2 < rows and output_grid[r2,c] == 0:
                        r2 += 1
                    if r2 < rows and output_grid[r2,c] == 8:
                        for k in range(r+1, r2):
                            output_grid[k,c] = 2
    return output_grid