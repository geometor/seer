"""
Removes the largest contiguous region of white (0) pixels from the input grid.
"""

import numpy as np

def find_largest_object(grid, color):
    """
    Finds the largest connected region of pixels with the given color.
    Uses Depth First Search (DFS).
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    max_size = 0
    largest_object_coords = []

    def dfs(row, col, current_object_coords):
        """
        Recursive Depth First Search helper function.
        """
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return 0

        visited[row, col] = True
        current_object_coords.append((row, col))
        size = 1
        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                size += dfs(row + dr, col + dc, current_object_coords)
        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object_coords = []
                object_size = dfs(r, c, current_object_coords)
                if object_size > max_size:
                    max_size = object_size
                    largest_object_coords = current_object_coords

    return largest_object_coords

def transform(input_grid):
    """
    Transforms the input grid by removing the largest contiguous region of '0' (white) pixels.
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find the coordinates of the largest object with color 0
    largest_object_coords = find_largest_object(input_grid, 0)

    # Remove the largest object by setting those coordinates in output to input values
    #for row, col in largest_object_coords:
     #   output_grid[row, col] = input_grid[row,col] # not needed - it's a copy

    return output_grid.tolist()