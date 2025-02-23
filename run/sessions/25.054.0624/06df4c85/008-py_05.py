"""
1. **Identify Colored Objects:** Locate all contiguous blocks of pixels with colors other than white (0) and blue (1). These are the initial "colored objects" (red, yellow, maroon, and azure).

2. **Horizontal Expansion:** Iterate through each row of the grid.
    *   If a pixel is blue (1) and is horizontally adjacent to the *same* colored object on *both* its left and right, change the blue pixel's color to match that of the object.
    * if a blue pixel has different colored objects to its left and right, then maintain its color

3.  **Iterate through colored objects:**
    * For the objects with the colors, maroon(9) and azure(8), expand the objects within their respective vertical sections in the entire column if there is an azure object.

4. **No vertical consideration:** The color propagation/modification of the blue pixel happens only horizontally within a row.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous objects of the same color, excluding white (0) and blue (1)."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def dfs(row, col, color, obj):
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(rows):
        for col in range(cols):
            if not visited[row, col] and grid[row, col] not in [0, 1]:
                obj = []
                dfs(row, col, grid[row, col], obj)
                objects.append((grid[row, col], obj))  # Store color and object pixels
    return objects

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    objects = find_objects(input_grid)

    # Horizontal Expansion
    for row in range(rows):
        for col in range(1, cols - 1):  # Iterate through inner columns
            if output_grid[row, col] == 1:
                left_color = output_grid[row, col - 1]
                right_color = output_grid[row, col + 1]
                if left_color == right_color and left_color not in [0, 1]:
                    output_grid[row, col] = left_color

    # Vertical Expansion of maroon(9) and azure(8) objects
    for color, obj_pixels in objects:
         if color in [8, 9]:
            obj_rows = [p[0] for p in obj_pixels]
            obj_cols = [p[1] for p in obj_pixels]

            min_col = min(obj_cols)
            max_col = max(obj_cols)

            
            for r in range(rows):
              for c in range(min_col, max_col+1):
                  if input_grid[r,c] == 1:
                    left_color = -1
                    right_color = -1

                    for i in range(c-1, -1, -1):
                      if input_grid[r,i] in [8,9]:
                        left_color = input_grid[r,i]
                        break
                    for i in range(c+1, cols):
                      if input_grid[r,i] in [8,9]:
                        right_color = input_grid[r,i]
                        break
                    if left_color == right_color and left_color == color:

                        output_grid[r,c] = color

    return output_grid