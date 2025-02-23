# AboveBelow7 • 012 • refine_coder

---
```python
"""
1.  **Identify Objects:** Find all contiguous regions of azure (8) pixels. These are considered movable objects. Find all contiguous regions of red(2), yellow (4) and green (3). These are considered stationary objects.
2.  **Sort Azure Objects:** Sort the azure objects by their leftmost column position to maintain their relative horizontal order.
3.  **Move Azure Objects:** Iterate through the sorted azure objects. For each azure object:
    *   Calculate its bounding box.
    *   Attempt to place the object at the bottom of the grid.
    *   Iteratively check for collisions with any non-background (non-zero) pixels within the bounding box area.
    *   If a collision occurs, move the object's intended position upwards by one row and recheck for collisions.
    *   Repeat the upward movement until a non-colliding position is found. This ensures stacking.
    *   Place the azure object in the final non-colliding position.
4. **Stationary Objects:** The red, yellow and green objects will automatically remain in its original position because the algorithm initializes the `output_grid` with the contents of the `input_grid`.
5. **Background:** The black (0) background pixels are implicitly handled by not being part of any object and filling the remaining space.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of a specified color in the grid.
    Returns a list of object bounding boxes (min_row, min_col, max_row, max_col) and a list of the object coordinates.
    """
    visited = set()
    objects = []
    object_coords = []

    def dfs(row, col, current_object, current_coords):
        if (row, col) in visited or row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        current_coords.append((row,col))
        dfs(row + 1, col, current_object, current_coords)
        dfs(row - 1, col, current_object, current_coords)
        dfs(row, col + 1, current_object, current_coords)
        dfs(row, col - 1, current_object, current_coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                current_coords = []
                dfs(row, col, current_object, current_coords)
                # calculate bounding box
                min_row = min(current_object, key=lambda x: x[0])[0]
                min_col = min(current_object, key=lambda x: x[1])[1]
                max_row = max(current_object, key=lambda x: x[0])[0]
                max_col = max(current_object, key=lambda x: x[1])[1]
                objects.append( (min_row, min_col, max_row, max_col) )
                object_coords.append(current_coords)
    return objects, object_coords

def is_collision(grid, row_start, col_start, obj_height, obj_width):
    """
    Checks for collisions between a bounding box and non-background pixels in the grid.
    """
    for r in range(row_start, row_start + obj_height):
        for c in range(col_start, col_start + obj_width):
            if r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != 0:
                return True  # Collision detected
    return False

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find azure (8) objects
    azure_objects, azure_coords = find_objects(input_grid, 8)

    # Clear initial positions of azure objects in the output grid
    for obj_coords in azure_coords:
        for row, col in obj_coords:
            output_grid[row, col] = 0

    # Sort azure objects by their leftmost coordinate (min_col)
    azure_objects_sorted = sorted(zip(azure_objects, azure_coords), key=lambda x: x[0][1])

    # Calculate destination positions for azure objects
    for (min_row, min_col, max_row, max_col), obj_coords in azure_objects_sorted:
        obj_height = max_row - min_row + 1
        obj_width = max_col - min_col + 1
        dest_row = output_grid.shape[0] - obj_height  # Start at the bottom

        # Check for collisions and adjust dest_row upwards
        while is_collision(output_grid, dest_row, min_col, obj_height, obj_width):
            dest_row -= 1
            if dest_row < 0:
                break # stop if we get to the top

        # Place the azure object in the final non-colliding position
        if dest_row >=0:
          for row, col in obj_coords:
              output_grid[dest_row + (row - min_row), col] = 8

    return output_grid
```
