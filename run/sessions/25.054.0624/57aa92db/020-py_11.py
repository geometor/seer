"""
1.  **Identify Objects:** Locate all contiguous blocks of non-white pixels in the input grid. These are our initial objects.
2.  **Green Object Expansion:** The green object expands. If it exists, increase its size by one pixel in all orthogonal directions (up, down, left, right).
3. **Yellow Object Expansion:** If exists, the yellow object will check if red squares are diagonal from it. If so, extend them to down and to the left, filling the area between them.
4.  **Preserve Other Objects:**  All other non-green, non-yellow objects (in this case, the azure and red objects) retain their original shape and position in the output grid.
5.  **Background:** All other pixels (white/0) remain unchanged.
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
                objects.append((grid[r, c], current_object))  # Store color and object pixels
    return objects

def expand_object(grid, object_pixels, color, diagonally=False):
  """Expands an object by one pixel in orthogonal directions."""
  new_pixels = set(object_pixels)
  rows, cols = grid.shape

  for r, c in object_pixels:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_pixels.add((nr,nc))
  return list(new_pixels)

def get_diagonal_neighbors(grid, r, c):
    """Returns the diagonal neighbors of a cell."""
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find all objects in the input grid
    objects = find_objects(input_grid)

    for color, obj_pixels in objects:
        if color == 3:  # Green object
            # expand green
            expanded_pixels = expand_object(input_grid, obj_pixels, 3)
            for r, c in expanded_pixels:
                output_grid[r,c] = 3
        elif color == 4: # Yellow Object
            output_pixels = obj_pixels[:]

            for r, c in obj_pixels:
              # Find diagonal neighbors
              diagonals = get_diagonal_neighbors(input_grid, r, c)

              # check diagonal for red
              for nr, nc in diagonals:
                if input_grid[nr, nc] == 2: # check if red
                  output_pixels.append((nr, nc))
            
            # Expand by one pixel to the down and to the left
            expanded_pixels = expand_object(input_grid, output_pixels, 4, True)

            # Fill the area between original yellow pixels and red pixels
            min_r = min(r for r, _ in expanded_pixels)
            max_r = max(r for r, _ in expanded_pixels)
            min_c = min(c for _, c in expanded_pixels)
            max_c = max(c for _, c in expanded_pixels)

            for r in range(min_r, max_r+1):
              for c in range(min_c, max_c+1):
                if (r,c) in expanded_pixels:
                    output_grid[r,c] = 4

        else: # Other
            for r, c in obj_pixels:
                output_grid[r, c] = color

    return output_grid