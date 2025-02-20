# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The program identifies each 2x1 azure rectangle. The blue cell is placed to the left of the top-most rectangle. Then, it processes the following rectangles, placing a blue cell to the right of the second top-most rectangle, and a blue cell to the left of the next rectangle.
It does nothing with the single azure cell.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
    objects = []
    visited = set()

    def is_valid(pos):
        return 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]

    def dfs(pos, current_object):
        if not is_valid(pos) or grid[pos] != color or pos in visited:
            return
        visited.add(pos)
        current_object.append(pos)
        neighbors = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]),
                     (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
        for neighbor in neighbors:
            dfs(neighbor, current_object)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color and (i, j) not in visited:
                current_object = []
                dfs((i, j), current_object)
                objects.append(current_object)
    return objects

def is_2x1_rectangle(obj, grid):
    # checks that shape is a 2x1 rectangle
    if len(obj) != 2:
        return False
    coords = np.array(obj)
    min_row, min_col = np.min(coords, axis=0)
    max_row, max_col = np.max(coords, axis=0)

    return (max_row - min_row == 1 and max_col - min_col == 0) or \
           (max_row - min_row == 0 and max_col - min_col == 1)

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find all azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)

    # Filter for 2x1 rectangles
    rectangles_2x1 = [obj for obj in azure_objects if is_2x1_rectangle(obj, input_grid)]
    
    # Sort rectangles based on their top-left corner's row, then column
    rectangles_2x1.sort(key=lambda obj: (min(r for r, _ in obj), min(c for _, c in obj)))
    
    # Process the rectangles
    if len(rectangles_2x1) >= 1:
        # Top rectangle: Add a blue cell to the immediate left
        top_rect = rectangles_2x1[0]
        top_rect_coords = np.array(top_rect)
        top_left_coord = (top_rect_coords[0,0], np.min(top_rect_coords[:, 1]) - 1)

        
        if 0 <= top_left_coord[0] < output_grid.shape[0] and 0 <= top_left_coord[1] < output_grid.shape[1]:
            output_grid[top_left_coord] = 1

    if len(rectangles_2x1) >= 2:

        # Second rectangle, add a blue cell immediately to the right.
        second_rect = rectangles_2x1[1]
        second_rect_coords = np.array(second_rect)

        second_right_coord = (second_rect_coords[0,0], np.max(second_rect_coords[:, 1]) + 1)

        if 0 <= second_right_coord[0] < output_grid.shape[0] and 0<= second_right_coord[1] < output_grid.shape[1]:
            output_grid[second_right_coord] = 1
            
    if len(rectangles_2x1) >= 3:

        # Third rectangle, add a blue cell immediately to the left.
        third_rect = rectangles_2x1[2]
        third_rect_coords = np.array(third_rect)

        third_left_coord = (third_rect_coords[0,0], np.min(third_rect_coords[:, 1]) - 1)

        if 0 <= third_left_coord[0] < output_grid.shape[0] and 0<= third_left_coord[1] < output_grid.shape[1]:
            output_grid[third_left_coord] = 1

    return output_grid
```
