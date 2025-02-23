"""
1.  **Object Identification:** Identify all contiguous objects (connected components of non-white pixels) in the input grid.
2.  **Green Expansion:** For each green (color 3) object, expand it by one pixel in all orthogonal directions (up, down, left, right) where it is directly adjacent to *any* other non-white colored pixel.
3.  **Yellow Expansion:** For each yellow (color 4) object, expand one pixel orthogonally in any direction where a red object is directly adjacent.
4.  **Magenta Expansion:** For each magenta (color 6) object: if a red pixel exists diagonally up and to the left (NW), expand the magenta object by one pixel to the left and one pixel up.
5. **Azure Expansion:** If there is an Azure colored square, expand one pixel to the left and one to the right.
6.  **Preservation:** All other objects retain their original shape and position.
7.  **Background:** White pixels (0) remain unchanged unless filled by an expanding object.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous objects in a grid."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, obj_color, current_object):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != obj_color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, obj_color, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append((grid[r, c], current_object))
    return objects

def expand_adjacent_to_any(grid, object_pixels):
    """Expands object by one pixel in orthogonal directions adjacent to any other object."""
    new_pixels = set(object_pixels)
    rows, cols = grid.shape

    for r, c in object_pixels:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] != 0:
                new_pixels.add((nr, nc))
    return list(new_pixels)
    
def expand_adjacent_to_red(grid, object_pixels):
    """Expands yellow object by one pixel in orthogonal directions adjacent to red object."""
    new_pixels = set(object_pixels)
    rows, cols = grid.shape
    
    for r,c in object_pixels:
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 2:
                new_pixels.add((nr, nc))
    return list(new_pixels)

def expand_magenta(grid, object_pixels):
    """Expands magenta object left and up if red is NW."""
    new_pixels = set(object_pixels)
    rows, cols = grid.shape

    for r, c in object_pixels:
        if r > 0 and c > 0 and grid[r-1, c-1] == 2:
            new_pixels.add((r-1, c))  # Up
            new_pixels.add((r, c-1))  # Left
    return list(new_pixels)
    
def expand_azure_square(grid, object_pixels):
    """Expands azure squares to the left and right."""
    new_pixels = set(object_pixels)
    rows, cols = grid.shape

    # Check if it's a square
    rs, cs = zip(*object_pixels)
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)

    if (max_r - min_r) == (max_c - min_c):
        # Expand left
        if min_c > 0:
            for r in range(min_r, max_r + 1):
              if grid[r, min_c -1] == 0:
                new_pixels.add((r, min_c - 1))
        # Expand right
        if max_c < cols - 1:
            for r in range(min_r, max_r + 1):
              if grid[r, max_c + 1] == 0:
                new_pixels.add((r, max_c + 1))

    return list(new_pixels)

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all objects
    objects = find_objects(input_grid)

    for color, obj_pixels in objects:
        if color == 3:  # Green
            expanded_pixels = expand_adjacent_to_any(input_grid, obj_pixels)
            for r, c in expanded_pixels:
                output_grid[r, c] = 3
        elif color == 4:  # Yellow
            expanded_pixels = expand_adjacent_to_red(input_grid, obj_pixels)
            for r, c in expanded_pixels:
                output_grid[r,c] = 4
        elif color == 6:  # Magenta
            expanded_pixels = expand_magenta(input_grid, obj_pixels)
            for r, c in expanded_pixels:
                output_grid[r, c] = 6
        elif color == 8:  # Azure
            expanded_pixels = expand_azure_square(input_grid, obj_pixels)
            for r, c in expanded_pixels:
                output_grid[r, c] = 8

    return output_grid