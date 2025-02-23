"""
1.  **Identify the Cross:** Find the "X" shaped cross formed by intersecting diagonal lines in the grid.  The cross can be any color, and the lines must intersect at the center. The cross may have a thickness greater than 1.
2.  **Determine Cross Interior:** The spaces within the arms of the "X" are considered the interior.
3.  **Recolor Cross Interior:** Change the color of the pixels *inside* the cross (excluding the outline) to yellow (color 4).
4.  **Recolor Background in Proximity to Cross Outline:**
    -   Identify the outline of the cross.  The outline consists of the outermost pixels of the cross.
    -   Identify cells adjacent to the cross outline (Manhattan distance of 1).
    -   Change the color of these adjacent background pixels to green (color 3).
5.  **Recolor Remaining Background:** Change the color of the remaining background pixels (those not adjacent to the cross outline, and not part of the cross) to yellow (color 4).
"""

import numpy as np

def get_objects(grid):
    """
    Detects distinct objects in the grid.  An object is a contiguous block of
    non-background pixels. Uses a flood-fill algorithm.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    objects = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def flood_fill(r, c, color):
        object_pixels = []
        stack = [(r, c)]
        visited[r, c] = True

        while stack:
            curr_r, curr_c = stack.pop()
            object_pixels.append((curr_r, curr_c))

            neighbors = [
                (curr_r - 1, curr_c),
                (curr_r + 1, curr_c),
                (curr_r, curr_c - 1),
                (curr_r, curr_c + 1),
            ]

            for nr, nc in neighbors:
                if is_valid(nr, nc) and not visited[nr, nc] and grid[nr, nc] == color:
                    visited[nr, nc] = True
                    stack.append((nr, nc))
        return object_pixels

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                object_pixels = flood_fill(r, c, grid[r, c])
                objects.append(object_pixels)

    return objects

def is_cross(object_pixels, grid):
    """
    Checks if a set of pixels forms a cross shape.  Considers thickness.
    The object must stretch from edge to edge of the grid.
    """
    if not object_pixels:
        return False

    rows, cols = grid.shape
    min_row = min(r for r, _ in object_pixels)
    max_row = max(r for r, _ in object_pixels)
    min_col = min(c for _, c in object_pixels)
    max_col = max(c for _, c in object_pixels)

    # Check if the object spans the entire grid in either dimension.
    if not ((min_row == 0 and max_row == rows -1) or (min_col == 0 and max_col == cols - 1)):
      return False
    
    #Basic check to ensure we have both diagonal components
    has_top_left = False
    has_top_right = False
    has_bottom_left = False
    has_bottom_right = False

    for r, c in object_pixels:
        if r < (max_row + min_row) // 2 and c < (max_col + min_col) // 2:
            has_top_left = True
        if r < (max_row + min_row) // 2 and c > (max_col + min_col) // 2:
            has_top_right = True
        if r > (max_row + min_row) // 2 and c < (max_col + min_col) // 2:
            has_bottom_left = True
        if r > (max_row + min_row) // 2 and c > (max_col + min_col) // 2:
            has_bottom_right = True

    return has_top_left and has_top_right and has_bottom_left and has_bottom_right

def get_cross_outline(cross_pixels):
    """
    Gets the outline pixels of the cross.
    """
    outline = set()
    for r, c in cross_pixels:
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
            (r - 1, c - 1),
            (r - 1, c + 1),
            (r + 1, c - 1),
            (r + 1, c + 1),
        ]
        is_outline = False
        for nr, nc in neighbors:
            if (nr, nc) not in cross_pixels:
                is_outline = True
                break
        if is_outline:
            outline.add((r, c))
    return list(outline)

def get_cross_interior(grid, cross_pixels, outline_pixels):
    """
    Determine Cross Interior by performing a flood fill on all
    background pixels and then identify any background pixels
    surrounded by the cross object.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    interior_pixels = set()
    
    #mark all cross pixels as visited
    for r, c in cross_pixels:
        visited[r,c] = True

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def flood_fill(r, c):
        #find connected background pixels
        background_pixels = []
        stack = [(r, c)]
        visited[r, c] = True
        
        while stack:
            curr_r, curr_c = stack.pop()
            background_pixels.append((curr_r, curr_c))
            
            neighbors = [
                (curr_r - 1, curr_c),
                (curr_r + 1, curr_c),
                (curr_r, curr_c - 1),
                (curr_r, curr_c + 1),
            ]
            
            for nr, nc in neighbors:
                if is_valid(nr, nc) and not visited[nr, nc] and grid[nr, nc] == 0:
                    visited[nr, nc] = True
                    stack.append((nr, nc))
        
        #check if all neighbors are cross pixels. if so, it's interior
        is_interior = True
        for br, bc in background_pixels:
            neighbors = [
                (br - 1, bc),
                (br + 1, bc),
                (br, bc - 1),
                (br, bc + 1),
            ]
            for nr, nc in neighbors:
                if is_valid(nr,nc) and (nr,nc) not in cross_pixels:
                    is_interior = False
                    break
            if not is_interior:
                break
        if is_interior:
            for p in background_pixels:
                interior_pixels.add(p)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] == 0:
                flood_fill(r,c)

    return list(interior_pixels)

def recolor_pixels(grid, pixels, color):
    """Recolors the specified pixels in the grid to the given color."""
    new_grid = np.copy(grid)
    for r, c in pixels:
        new_grid[r, c] = color
    return new_grid

def get_adjacent_background_pixels(grid, outline_pixels):
    """
    Finds background pixels adjacent to the cross outline.
    """
    rows, cols = grid.shape
    adjacent_pixels = set()
    for r, c in outline_pixels:
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
        ]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
                adjacent_pixels.add((nr, nc))
    return list(adjacent_pixels)

def transform(input_grid):
    # Find objects in the grid
    objects = get_objects(input_grid)
    
    # Initialize output grid as a copy of the input
    output_grid = np.copy(input_grid)

    cross_pixels = None
    for obj in objects:
        if is_cross(obj, input_grid):
            cross_pixels = obj
            break  # Assume only one cross
    
    if cross_pixels is None:
        return output_grid #no cross found

    # Get the outline of the cross
    cross_outline = get_cross_outline(cross_pixels)

    # Get the interior of the cross
    cross_interior = get_cross_interior(input_grid, cross_pixels, cross_outline)
    
    # Recolor cross interior to yellow (4)
    output_grid = recolor_pixels(output_grid, cross_interior, 4)

    # Get adjacent background pixels
    adjacent_background = get_adjacent_background_pixels(output_grid, cross_outline)

    # Recolor adjacent background pixels to green (3)
    output_grid = recolor_pixels(output_grid, adjacent_background, 3)
    
    # Recolor remaining background to yellow.
    for r in range(output_grid.shape[0]):
        for c in range(output_grid.shape[1]):
            if output_grid[r,c] == 0:
                output_grid[r,c] = 4

    return output_grid