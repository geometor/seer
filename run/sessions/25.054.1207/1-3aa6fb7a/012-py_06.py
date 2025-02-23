"""
The transformation involves adding a blue (1) pixel adjacent to each connected component (object) of azure (8) pixels. The placement of the blue pixel prioritizes the right, down, up, and left sides of the right-most, bottom-most, top-most, then left-most azure pixel of the object.
"""

import numpy as np

def get_connected_components(grid, color):
    """
    Finds connected components of a given color in the grid.
    Uses a depth-first search approach.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    components = []

    def dfs(row, col, current_component):
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_component.append((row, col))
        dfs(row + 1, col, current_component)
        dfs(row - 1, col, current_component)
        dfs(row, col + 1, current_component)
        dfs(row, col - 1, current_component)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and not visited[row, col]:
                current_component = []
                dfs(row, col, current_component)
                components.append(current_component)
    return components

def get_neighbors(grid, row, col):
    """
    Gets the coordinates of the neighbors of a cell (no diagonals).
    """
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors


def transform(input_grid):
    """
    Transforms the input grid by placing a blue pixel adjacent to each azure object.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects (Connected Components of Azure)
    azure_objects = get_connected_components(input_grid, 8)

    # 2. Process Each Object
    for obj in azure_objects:
        # Find right-most, bottom-most, top-most and left-most pixels
        obj_array = np.array(obj)
        
        # Sort by x-coordinate (col) descending to find right-most, then y ascending.
        right_most_pixels = obj_array[obj_array[:, 1].argsort()[::-1]]
        right_most_pixel = right_most_pixels[0]

        # Sort by x coordinate (col) ascending to find left-most.
        left_most_pixels = obj_array[obj_array[:,1].argsort()]
        left_most_pixel = left_most_pixels[0]

        # Sort by y coordinate (row) descending
        bottom_most_pixels = obj_array[obj_array[:,0].argsort()[::-1]]
        bottom_most_pixel = bottom_most_pixels[0]
        
        # Sort by y coordinate (row) ascending
        top_most_pixels = obj_array[obj_array[:,0].argsort()]
        top_most_pixel = top_most_pixels[0]

        priority_pixels = [right_most_pixel, bottom_most_pixel, top_most_pixel, left_most_pixel]
        
        placed = False
        for pixel in priority_pixels:
            if placed:
                break

            row, col = pixel
                
            # Prioritized neighbor checking (Right, Down, Up, Left)
            priority_neighbors = [
                (row, col + 1),  # Right
                (row + 1, col),  # Down
                (row - 1, col),  # Up
                (row, col - 1),  # Left
            ]

            for neighbor_row, neighbor_col in priority_neighbors:
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    if output_grid[neighbor_row, neighbor_col] == 0:
                        output_grid[neighbor_row, neighbor_col] = 1
                        placed = True #placed once
                        break  # Move to the next object

    return output_grid