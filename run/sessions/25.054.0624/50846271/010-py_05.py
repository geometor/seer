"""
1.  **Identify Objects:** Identify all contiguous regions (objects) of pixels with the same color. Consider pixels cardinally adjacent (up, down, left, right) to be part of the same object. Diagonal adjacency does not connect objects.

2.  **Find Gray Objects:** Iterate through the list of objects, selecting those that are gray (color value 5).

3.  **Check for Red Adjacency:** For each gray object, check if *any* of its pixels are cardinally adjacent to a red pixel (color value 2).

4.  **Conditional Color Change (Object-Based):** If a gray object is adjacent to a red object, change *all* pixels within that gray object to azure (color value 8).

5.  **Preserve Other Pixels:** All pixels *not* part of a gray object that is adjacent to a red object retain their original color from the input grid.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the cardinal neighbors of a pixel."""
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

def flood_fill(grid, row, col, target_color, object_pixels):
    """Performs a flood fill to identify a contiguous object."""
    if (row, col) in object_pixels or grid[row, col] != target_color:
        return
    object_pixels.add((row, col))
    neighbors = get_neighbors(grid, row, col)
    for n_row, n_col in neighbors:
        flood_fill(grid, n_row, n_col, target_color, object_pixels)

def find_objects(grid):
    """Finds all contiguous objects in the grid."""
    rows, cols = grid.shape
    objects = []
    visited = set()

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                object_pixels = set()
                flood_fill(grid, row, col, grid[row, col], object_pixels)
                if object_pixels:
                    objects.append((grid[row,col], object_pixels)) # Store color and pixels
                    visited.update(object_pixels)
    return objects

def is_adjacent_to_red(grid, object_pixels):
    """Checks if a gray object is adjacent to a red pixel."""
    for row, col in object_pixels:
        neighbors = get_neighbors(grid, row, col)
        for n_row, n_col in neighbors:
            if grid[n_row, n_col] == 2:
                return True
    return False

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects
    objects = find_objects(input_grid)

    # 2. & 3. Find Gray Objects and Check for Red Adjacency
    for color, object_pixels in objects:
        if color == 5:  # Gray object
            if is_adjacent_to_red(input_grid, object_pixels):
                # 4. Conditional Color Change
                for row, col in object_pixels:
                    output_grid[row, col] = 8

    # 5. Preserve Other Pixels (already handled by initializing output_grid as a copy)
    return output_grid