# 0e206a2e • 006 • example_3 - CODE

---
```python
"""
The transformation rule involves moving azure (color 8) objects, influenced by blue (color 1) objects if present in the row. Azure (8) moves to the rightmost open position in the same row. 

1.  **Identify Objects:** Locate all azure (8) and blue (1) colored objects in the input grid.

2. **Iterate**:
  + Consider each row where blue cell exist.
  + find the azure objects in this row.

3.  **Move Azure Objects:** For each azure object in rows with at least a blue cell.
    +   Move that object to the right side of the grid, immediately to the left of the rightmost non-zero element.
    + For connected azure objects, perform the displacement for all of them, maintaining their original shape.

4. Other colors remain in their cells.
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
            
    #2. Process rows with blue cells
    for row_index in blue_rows:
        # find azure object in the current row
        azure_objects = find_objects(np.array([grid[row_index]]), 8)
        
        #get rightmost position
        rightmost = grid.shape[1]-1
        
        # check is there are other non-zero objects
        for c in range(grid.shape[1]-1, -1, -1):
          if grid[row_index,c] !=0:
            break
          rightmost = c
        
        #move each azure shape to the right
        aux = 0
        for azure_object in azure_objects:
            for r,c in azure_object:
                #clear previous azure position
                output_grid[row_index, c] = 0
            for r,c in azure_object:
                #move cell to the correct position
                output_grid[row_index, rightmost-aux] = 8
                aux += 1
            aux=0

    return output_grid.tolist()
```

