"""
1.  Iterate through each pixel of the input grid.
2.  For pixels that contain the color maroon(9).
3.  Replace all instances of a 9 with a 0 except for the big maroon object in the center.
4.  For pixel that contain the color green (3) in a 2x2 square shape, replace all it's neighbor pixels around of this 2x2 green pixel.
5. Output the modified grid.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous objects of a specific color in the grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)
        dfs(row + 1, col + 1, current_object)  # Check diagonals
        dfs(row + 1, col - 1, current_object)
        dfs(row - 1, col + 1, current_object)
        dfs(row - 1, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def find_2x2_square(grid, color):
    """
    Finds 2x2 squares of a specific color.
    """
    squares = []
    for r in range(grid.shape[0] - 1):
        for c in range(grid.shape[1] - 1):
            if (grid[r, c] == color and grid[r + 1, c] == color and
                    grid[r, c + 1] == color and grid[r + 1, c + 1] == color):
                squares.append((r,c))
    return squares

def get_neighbors(grid, row, col):
    """Gets the 8 neighbors of a cell (diagonal included)."""
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                neighbors.append((nr, nc))
    return neighbors
    

def transform(input_grid):
    """
    Transforms the input grid according to the rules.
    """
    output_grid = np.copy(input_grid)

    # Find and replace maroon (9) with white(0)
    maroon_objects = find_objects(input_grid, 9)
    
    # Find largest maroon object (approximation: largest area)
    largest_maroon = []
    if maroon_objects:  
        largest_maroon = max(maroon_objects, key=len)
    
    for obj in maroon_objects:
       if obj != largest_maroon: 
            for row, col in obj:
                output_grid[row, col] = 0


    # Find 2x2 green(3) squares
    green_squares = find_2x2_square(input_grid, 3)

    # Replace neighbors of 2x2 green squares
    for r, c in green_squares:
        for neighbor_row, neighbor_col in get_neighbors(input_grid, r, c):
            output_grid[neighbor_row, neighbor_col] = input_grid[neighbor_row,neighbor_col] #get the original value
        for neighbor_row, neighbor_col in get_neighbors(input_grid, r+1, c):
            output_grid[neighbor_row, neighbor_col] = input_grid[neighbor_row,neighbor_col]
        for neighbor_row, neighbor_col in get_neighbors(input_grid, r, c+1):
            output_grid[neighbor_row, neighbor_col] = input_grid[neighbor_row,neighbor_col]   
        for neighbor_row, neighbor_col in get_neighbors(input_grid, r+1, c+1):
            output_grid[neighbor_row, neighbor_col] = input_grid[neighbor_row,neighbor_col]   

    return output_grid