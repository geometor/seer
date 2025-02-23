"""
Identifies azure colored objects, removes their exterior borders, and changes the remaining interior pixels to blue.
"""

import numpy as np

def find_objects(grid, color):
    """Finds all contiguous regions of the specified color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    objects = []

    def dfs(r, c, current_object):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_border(grid, object_pixels):
    """Finds the exterior border pixels of an object."""
    rows, cols = grid.shape
    border_pixels = set()

    for r, c in object_pixels:
        # Check neighbors for different color or edge of grid
        if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1 or
            grid[r-1, c] != grid[r,c] or
            grid[r+1, c] != grid[r,c] or
            grid[r, c-1] != grid[r,c] or
            grid[r, c+1] != grid[r,c]
            ):
          border_pixels.add((r,c))
    return list(border_pixels)

def find_interior(object_pixels, border_pixels):
    """Finds interior pixels by removing border from all object pixels."""
    return list(set(object_pixels) - set(border_pixels))

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.zeros_like(input_grid) # Initialize with background color (0)
    
    # Define the color of the objects and the target color
    azure = 8
    blue = 1

    # Find all azure objects
    azure_objects = find_objects(input_grid, azure)
    
    # For each azure object:
    for azure_object in azure_objects:
        # 2. Object Decomposition: Find exterior border and interior
        border = find_border(input_grid, azure_object)
        interior = find_interior(azure_object, border)

        # 3. Border Change: (Implicitly handled by initializing output_grid to 0)

        # 4. Interior Recoloring: Change all interior pixels to blue
        for r, c in interior:
            output_grid[r, c] = blue

    # 5. Output construction (handled in the steps above)
    return output_grid