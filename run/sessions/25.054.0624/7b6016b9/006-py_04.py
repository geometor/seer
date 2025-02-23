"""
1.  **Change Background:** Replace all white (0) pixels in the input grid with green (3).

2.  **Identify Enclosed Objects:**
    *   Find all contiguous objects (connected regions of the same color, excluding green).
    *   For each object:
        *   Perform an "inverse flood fill" starting from all edges of the grid, using the background color (green). This marks all background-connected pixels.
        *   If *any* pixels of a color different than the object's color are *not* reached by the inverse flood fill, the object is considered "enclosing".

3.  **Fill Enclosed Regions:**  For each object identified as "enclosing":
    * Find all pixels within the grid that are:
        * Not the same color as the enclosing object, AND
        * Are not reachable by an "inverse flood fill" of the background.
    * Change the color of *all* such pixels within the enclosed region to red (2).
        * **Constraint:** The filling should stay inside the object.
"""

import numpy as np

def get_objects(grid):
    """
    Finds objects of all colors in the grid.

    Args:
        grid: The input grid (NumPy array).

    Returns:
        A dictionary of objects, where keys are colors and values are lists of objects.
        Each object is a set of (row, col) coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, current_object):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or grid[row, col] != color
            or (row, col) in visited
        ):
            return
        visited.add((row, col))
        current_object.add((row, col))
        dfs(row + 1, col, color, current_object)
        dfs(row - 1, col, color, current_object)
        dfs(row, col + 1, color, current_object)
        dfs(row, col - 1, color, current_object)

    for row in range(rows):
        for col in range(cols):
            color = grid[row, col]
            if (row, col) not in visited:
                current_object = set()
                dfs(row, col, color, current_object)
                if color not in objects:
                    objects[color] = []
                objects[color].append(current_object)
    return objects

def inverse_flood_fill(grid, background_color):
    """
    Performs an inverse flood fill from the edges of the grid.

    Args:
        grid: The input grid.
        background_color: The color to flood with.

    Returns:
        A set of (row, col) coordinates that were reached by the flood fill.
    """
    rows, cols = grid.shape
    visited = set()
    q = []

    # Add all edge pixels to the queue
    for r in range(rows):
        if grid[r, 0] == background_color:
          q.append((r, 0))
        if grid[r, cols - 1] == background_color:
          q.append((r, cols - 1))
    for c in range(1, cols - 1):
        if grid[0, c] == background_color:
          q.append((0, c))
        if grid[rows - 1, c] == background_color:
          q.append((rows - 1, c))
    
    def get_neighbors(row,col):
        neighbors = []
        if row > 0:
            neighbors.append((row-1, col))
        if row < rows - 1:
            neighbors.append((row+1, col))
        if col > 0:
            neighbors.append((row, col-1))
        if col < cols-1:
            neighbors.append((row, col + 1))
        return neighbors

    # Perform BFS
    while q:
        row, col = q.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))

        for nr, nc in get_neighbors(row,col):
            if grid[nr,nc] == background_color:
                q.append((nr,nc))

    return visited


def find_enclosed_pixels(grid, object_pixels, object_color, background_reachable):
    """
    Finds pixels enclosed by the given object.
    """
    enclosed_pixels = set()
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if (r, c) not in object_pixels and (r, c) not in background_reachable and grid[r,c] != object_color:
                enclosed_pixels.add((r, c))
    return enclosed_pixels


def flood_fill(grid, start_pixels, target_color, replacement_color):
    """
    Performs a flood fill operation on the grid, starting from multiple seed pixels.
    Now includes a check to make sure we don't replace the border pixels.
    """

    rows, cols = grid.shape
    output_grid = np.copy(grid)
    q = list(start_pixels)
    visited = set()

    def get_neighbors(r, c):
      neighbors = []
      if r > 0:
          neighbors.append((r-1,c))
      if r < rows - 1:
          neighbors.append((r+1, c))
      if c > 0:
        neighbors.append((r, c - 1))
      if c < cols - 1:
        neighbors.append((r, c+1))
      return neighbors

    while q:
      row, col = q.pop(0)
      if (row,col) in visited:
          continue

      if output_grid[row,col] == target_color:
          visited.add((row,col))
          output_grid[row,col] = replacement_color

          for nr, nc in get_neighbors(row,col):
            q.append((nr,nc))

    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # change white background to green
    output_grid[output_grid == 0] = 3
    background_color = 3

    # Find all objects
    objects_by_color = get_objects(output_grid)

    # Iterate through objects and fill interiors
    for color, objects in objects_by_color.items():
        if color == background_color:  # Skip background color
            continue
        for obj in objects:
            # Inverse flood fill to find background-reachable pixels
            background_reachable = inverse_flood_fill(output_grid, background_color)

            # Find enclosed pixels
            enclosed_pixels = find_enclosed_pixels(output_grid, obj, color, background_reachable)
            
            if enclosed_pixels:
                #get the target color from the first enclosed pixel
                first_enclosed_pixel = next(iter(enclosed_pixels))
                target_color = output_grid[first_enclosed_pixel]

                output_grid = flood_fill(output_grid, enclosed_pixels, target_color, 2)

    return output_grid