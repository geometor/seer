"""
The transformation rule is: white cells adjacent to azure cells become blue, but only if the adjacent azure cell has at least one *other* azure neighbor in a different direction, thereby creating an azure "bridge".
"""

import numpy as np

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def get_adjacent_neighbors(r, c, rows, cols):
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc, rows, cols):
            neighbors.append((nr, nc))
    return neighbors

def get_all_neighbors(r, c, rows, cols):
     neighbors = []
     for dr in [-1, 0, 1]:
         for dc in [-1, 0, 1]:
             if dr == 0 and dc == 0:
                 continue
             nr, nc = r + dr, c + dc
             if is_valid(nr, nc, rows, cols):
                neighbors.append((nr,nc))
     return neighbors

def has_different_direction_neighbor(r, c, rows, cols, grid, target_color):
    neighbors = get_all_neighbors(r, c, rows, cols)
    neighbor_colors = [(nr, nc) for nr, nc in neighbors if grid[nr, nc] == target_color]

    if not neighbor_colors:
        return False

    directions = set()
    for nr, nc in neighbor_colors:
        dr, dc = nr - r, nc - c
        directions.add((dr, dc))
    
    return len(directions) > 1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through all cells
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is white
            if input_grid[r, c] == 0:
                # Get adjacent neighbors
                adjacent_neighbors = get_adjacent_neighbors(r, c, rows, cols)
                # Find azure neighbors
                azure_neighbors = [(nr, nc) for nr, nc in adjacent_neighbors if output_grid[nr, nc] == 8]

                # check directionality condition
                for ar, ac in azure_neighbors:
                    if has_different_direction_neighbor(ar, ac, rows, cols, output_grid, 8):
                        output_grid[r,c] = 1
                        break

    return output_grid