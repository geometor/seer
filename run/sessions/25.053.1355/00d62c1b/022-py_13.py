"""
1.  **Find Largest Green Object:** Identify the largest contiguous region of green (3) pixels in the input grid. This is the "target object."

2.  **Expand the Object:** Create a temporary copy of the grid. Expand the target object in this copy by one pixel in all directions (horizontally, vertically, and *diagonally*).  This creates an "expanded object."

3.  **Flood Fill Background (Expanded Grid):**  On the *expanded* grid, flood-fill the background, starting from a known background pixel (e.g., the top-left corner).  Use a temporary color different from green and yellow.

4.  **Identify Interior Pixels:**  Compare the original grid to the expanded, flood-filled grid. The interior pixels of the target object are those pixels that are:
    *   Green (3) in the *original* grid.
    *   *Not* the background color (after flood fill) in the *expanded* grid.

5.  **Change Interior Color:** Change the color of all identified interior pixels in the *original* grid from green (3) to yellow (4).

6. **Preserve all other pixels:** All other pixels remain unchanged.
"""

import numpy as np

def find_largest_object(grid, color):
    visited = np.zeros_like(grid, dtype=bool)
    max_size = 0
    largest_object_coords = []

    def dfs(row, col, current_object_coords):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return 0

        visited[row, col] = True
        current_object_coords.append((row, col))
        size = 1
        size += dfs(row + 1, col, current_object_coords)
        size += dfs(row - 1, col, current_object_coords)
        size += dfs(row, col + 1, current_object_coords)
        size += dfs(row, col - 1, current_object_coords)
        return size

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object_coords = []
                current_size = dfs(row, col, current_object_coords)
                if current_size > max_size:
                    max_size = current_size
                    largest_object_coords = current_object_coords

    return largest_object_coords

def expand_object(grid, object_coords, temp_color):
    """Expands the object by one pixel in all directions."""
    expanded_grid = np.copy(grid)
    for row, col in object_coords:
        expanded_grid[row, col] = temp_color  # Set original object to temp color
        # Expand in all directions (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < grid.shape[0] and 0 <= new_col < grid.shape[1]:
                    expanded_grid[new_row, new_col] = temp_color
    return expanded_grid

def flood_fill(grid, row, col, target_color, replacement_color):
    """
    Performs a flood fill on the grid, starting from (row, col).
    Only fills pixels that are equal to target_color.
    """
    if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
            grid[row, col] != target_color):
        return
    grid[row, col] = replacement_color
    flood_fill(grid, row + 1, col, target_color, replacement_color)
    flood_fill(grid, row - 1, col, target_color, replacement_color)
    flood_fill(grid, row, col + 1, target_color, replacement_color)
    flood_fill(grid, row, col - 1, target_color, replacement_color)


def find_interior_pixels(grid, object_coords):
    """Identifies interior pixels using expansion and flood fill."""
    temp_object_color = -1
    expanded_grid = expand_object(grid, object_coords, temp_object_color)

    background_color = expanded_grid[0, 0]
    temp_background_color = -2

    if background_color != temp_object_color:
      flood_fill(expanded_grid, 0, 0, background_color, temp_background_color)

    interior_pixels = []
    for row, col in object_coords:
        if expanded_grid[row, col] != temp_background_color:
          interior_pixels.append((row,col))

    return interior_pixels


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find largest green object
    green_object_coords = find_largest_object(input_grid, 3)

    # find interior pixels using expansion and flood-filling
    interior_pixels = find_interior_pixels(input_grid, green_object_coords)

    # change interior pixels to yellow
    for row, col in interior_pixels:
        output_grid[row, col] = 4

    return output_grid