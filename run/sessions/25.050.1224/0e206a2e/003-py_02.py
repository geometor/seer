"""
The transformation this time consolidates green (color 3) objects to the bottom right, influenced by rows that contains blue color (1).

1.  **Identify Objects:** Locate all green (3) and blue(1) objects within the input grid.

2. **Iterate**:
  + Consider each row where blue cell exist.
  + find the green objects in the input.

3.  **Consolidate green:**
    +   All green objects in the grid are moved and combined to the most-bottom right position in the rows where blue cell(s) exist, preserving connectivity and extending to adjacent rows if needed.
    +   The moving of green objects only affect to row(s) with blue object(s).
    + The shape tries to maintain the horizontal shape.
    + The shape will fill the lower index columns in case of overflow.

4. Other objects remain in their initial cell, except green object.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(row, col):
        """Depth-first search to find connected components."""
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []

        visited.add((row, col))
        object_cells = [(row, col)]

        object_cells.extend(dfs(row + 1, col))
        object_cells.extend(dfs(row - 1, col))
        object_cells.extend(dfs(row, col + 1))
        object_cells.extend(dfs(row, col - 1))
        return object_cells

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                objects.append(dfs(row, col))
    return objects

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    grid = np.array(input_grid)  # Convert to NumPy array for easier manipulation
    output_grid = np.copy(grid)

     # 1. Find blue cells
    blue_objects = find_objects(grid, 1)
    
    #collect rows with blue cells
    blue_rows = set()
    for blue_object in blue_objects:
        for r,c in blue_object:
            blue_rows.add(r)
            
    #2. Find green cells
    green_objects = find_objects(grid, 3)
    
    green_cells_count = sum([len(obj) for obj in green_objects])
    
    #3. Clear green cells
    for green_object in green_objects:
      for r,c in green_object:
        if r in blue_rows:
          output_grid[r,c] = 0
    
    # get positions to locate green cells
    aux = 0
    for row_index in sorted(list(blue_rows), reverse=True):
      #fill the row
      for col_index in range(grid.shape[1]-1, -1, -1):
        if aux < green_cells_count:
          output_grid[row_index, col_index] = 3
          aux += 1
        else:
          break

    return output_grid.tolist()