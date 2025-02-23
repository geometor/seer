"""
Identifies contiguous green regions in a grid and changes the color of green
pixels to yellow if they are on the bottom or right side of a horizontal or
vertical green segment and have at least one adjacent green pixel (up, down,
left, or right).
"""

import numpy as np

def get_neighbors(grid, r, c, color):
    """Gets the neighbors of a given cell, including diagonals."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if (i != r or j != c) and grid[i, j] == color:
                neighbors.append((i, j))
    return neighbors


def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.

    Args:
        input_grid (list of lists): The input grid of pixel values.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = set()

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Process only green pixels that haven't been visited
            if input_grid[r, c] == 3 and (r, c) not in visited:
                green_region = []
                queue = [(r, c)]
                visited.add((r, c))

                # Find contiguous green region using BFS
                while queue:
                    curr_r, curr_c = queue.pop(0)
                    green_region.append((curr_r, curr_c))

                    for nr, nc in get_neighbors(input_grid, curr_r, curr_c, 3):
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                
                # Iterate through identified green region
                for gr, gc in green_region:
                    neighbors = get_neighbors(input_grid, gr, gc, 3)
                    is_right_edge = True
                    is_bottom_edge = True
                    
                    # check if right edge or bottom edge
                    for nr, nc in neighbors:
                        if nr == gr and nc > gc:
                            is_right_edge = False
                        if nc == gc and nr > gr:
                            is_bottom_edge = False
                    
                    # if there are horizontal or vertical green neighbors, change edge to yellow
                    cardinal_neighbors = 0
                    for nr, nc in neighbors:
                         if nr == gr or nc == gc:
                            cardinal_neighbors += 1
                    if cardinal_neighbors > 0 and (is_right_edge or is_bottom_edge):
                        output_grid[gr, gc] = 4

    return output_grid.tolist()