"""
1.  **Identify Objects:** Identify all distinct objects in the input grid. An object is a contiguous group of pixels of the same color.
2.  **Preserve Diagonal:** If there is a gray (5) object in a diagonal line starting from the top-left, maintain its starting position.
3.  **Move Color Objects:** If there is azure (8) object, place to row 0. Place its leftmost pixel at column index 2. If there is red (2) object, place it to the right of azure object, on the same row.
4.  **Move Magenta:** If there is magenta (6) object, stack all pixels on top row starting from column index 2.
5. **Gray Fills:** If gray object is present and is split, the lowest and rightmost pixel of the object, will move to the left, staying on its row, occupying next empty cell, only if no same color pixel is present.
6.  **Fill Gaps:** Other color (0/white) objects fill empty spaces left by the movement of the objects above.
"""

import numpy as np

def find_objects(grid):
    """Identifies distinct objects in the grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, color, current_object)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c]:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append((grid[r, c], current_object))
    return objects

def move_object(grid, object_pixels, target_row, target_col_start):
    """Moves an object to a new location within the grid, filling with 0"""
    new_grid = np.copy(grid)

    # Clear old positions, filling with 0
    for r, c in object_pixels:
        new_grid[r, c] = 0

    # Compute and set new positions
    min_col = min([c for _, c in object_pixels])
    for r, c in object_pixels:
        new_col = target_col_start + (c - min_col)
        if 0 <= target_row < new_grid.shape[0] and 0 <= new_col < new_grid.shape[1]:
          new_grid[target_row, new_col] = grid[r, c]

    return new_grid

def move_object_stack(grid, object_pixels, target_row, target_col_start):
    """Moves and stacks object's pixel to target location"""

    new_grid = np.copy(grid)

    #clear old positions
    for r, c in object_pixels:
        new_grid[r,c] = 0

    for i, (r,c) in enumerate(object_pixels):
       if 0 <= target_row < new_grid.shape[0] and 0 <= target_col_start + i < new_grid.shape[1]:
            new_grid[target_row, target_col_start + i] = grid[r,c]

    return new_grid

def move_gray_left(grid, object_pixels):
    """Moves the lowest, rightmost pixel of a gray object to the left."""
    new_grid = np.copy(grid)

    if not object_pixels:
        return new_grid

    # Find lowest, rightmost pixel
    lowest_row = -1
    rightmost_col = -1
    for r, c in object_pixels:
        if r > lowest_row:
            lowest_row = r
            rightmost_col = c
        elif r == lowest_row and c > rightmost_col:
            rightmost_col = c

    # Check for an empty cell to the left
    if rightmost_col > 0 and new_grid[lowest_row, rightmost_col - 1] == 0:
        new_grid[lowest_row, rightmost_col] = 0
        new_grid[lowest_row, rightmost_col - 1] = 5

    return new_grid


def fill_gaps(grid, objects):
    """Fills gaps in the grid with pixels from object 0 (white)."""
    rows, cols = grid.shape
    new_grid = np.copy(grid)

    # Create a set of occupied positions
    occupied = set()
    for r in range(rows):
        for c in range(cols):
            if new_grid[r,c] != 0:
                occupied.add((r,c))


    white_object = None
    for color, pixels in objects:
      if color == 0:
        white_object = pixels
        break

    if white_object is None:
      return new_grid
    
    white_pixels_available = list(white_object)

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in occupied and white_pixels_available:
                # Find the closest white pixel and swap
              
                new_r, new_c = white_pixels_available.pop(0)  #remove first
                new_grid[r,c] = new_grid[new_r,new_c] #move
                new_grid[new_r, new_c] = 0 #clear

    return new_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Objects
    objects = find_objects(input_grid)

    #2. Preserve Diagonal Gray
    gray_diagonal = []
    for color, pixels in objects:
        if color == 5:  # Gray
            is_diagonal = True
            for i in range(min(rows,cols)):
               if (i,i) not in pixels:
                  is_diagonal = False
                  break

            if is_diagonal:
                for r,c in pixels:
                  output_grid[r,c] = 5
            else:
               gray_diagonal = pixels #not diagonal from top left
    

    # 3. Move Azure and Red Objects
    azure_object = None
    red_object = None
    for color, pixels in objects:
        if color == 8:
            azure_object = pixels
        elif color == 2:
            red_object = pixels

    if azure_object is not None:
        output_grid = move_object(output_grid, azure_object, 0, 2)
    if red_object is not None:
        if azure_object is not None:
            max_azure_col = -1
            for r,c in azure_object:
               if c > max_azure_col:
                  max_azure_col = c
            if max_azure_col > -1:
              output_grid = move_object(output_grid, red_object, 0, max_azure_col + 1)
        else:
            output_grid = move_object(output_grid, red_object, 0, 2)


    # 4. Move Magenta Objects
    magenta_object = None
    for color, pixels in objects:
       if color == 6:
          magenta_object = pixels
          break

    if magenta_object is not None:
       output_grid = move_object_stack(output_grid, magenta_object, 0, 2)


    #5. Gray Filling
    if len(gray_diagonal) > 0:
      output_grid = move_gray_left(output_grid, gray_diagonal)

    # 6. Fill gaps
    updated_objects = find_objects(output_grid)
    output_grid = fill_gaps(output_grid, updated_objects)

    return output_grid