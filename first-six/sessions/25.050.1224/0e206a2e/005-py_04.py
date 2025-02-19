"""
The transformation rule involves moving azure (color 8) objects. The movement is influenced by rows containing blue and red cells. Azure objects are shifted to rows with both blue and red cells.

1.  **Identify Objects:** Locate all azure (8), blue (1), and red (2) colored objects in the input grid.

2.  **Determine Target Rows:**
    *   Identify rows that contain *both* blue (1) and red (2) colored objects.

3.  **Move Azure Objects:**
    *   Move *all* azure (8) objects from the entire grid to the rows identified in step 2.
    *   The azure objects are placed to fill the identified row(s) starting from the leftmost available position.
        * The shape is not preserved.

4. Other objects are not moved, except for azure objects that have been moved to the target row.
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
    grid = np.array(input_grid)
    output_grid = np.copy(grid)

    # 1. Find objects of interest
    azure_objects = find_objects(grid, 8)
    blue_objects = find_objects(grid, 1)
    red_objects = find_objects(grid, 2)
    
    #get rows with blue and red
    blue_rows = set()
    for blue_object in blue_objects:
        for r,c in blue_object:
            blue_rows.add(r)
            
    red_rows = set()
    for red_object in red_objects:
        for r,c in red_object:
            red_rows.add(r)
            
    target_rows = list(blue_rows.intersection(red_rows))

    # 2. Clear the original positions of azure objects
    for azure_object in azure_objects:
        for row, col in azure_object:
            output_grid[row, col] = 0

    # 3. Move azure objects to target rows
    azure_cells = []
    for azure_object in azure_objects:
        azure_cells.extend(azure_object)
    
    cell_index = 0
    for target_row in target_rows:
        for col in range(grid.shape[1]):  # Iterate through columns in the target row
           if cell_index < len(azure_cells):
                output_grid[target_row,col] = 8
                cell_index+=1
    
    return output_grid.tolist()
