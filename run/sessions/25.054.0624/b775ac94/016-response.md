# b775ac94 • 016 • refine_coder

---
```python
"""
Duplicates and expands colored objects in a grid, with specific rules for colors 1, 2, 3, 4, 6, 7 and 8.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous colored regions (objects) in the grid.
    Returns a dictionary where keys are colors and values are lists of (row, col) coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj_coords):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return
        visited.add((row, col))
        obj_coords.append((row, col))
        dfs(row + 1, col, color, obj_coords)
        dfs(row - 1, col, color, obj_coords)
        dfs(row, col + 1, color, obj_coords)
        dfs(row, col - 1, color, obj_coords)

    for row in range(rows):
        for col in range(cols):
            color = grid[row, col]
            if color != 0 and (row, col) not in visited:
                obj_coords = []
                dfs(row, col, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)
    return objects

def get_object_width(obj_coords):
    """Calculates the width of an object."""
    if not obj_coords:
        return 0
    min_col = min(c for _, c in obj_coords)
    max_col = max(c for _, c in obj_coords)
    return max_col - min_col + 1

def get_object_height(obj_coords):
    """Calculates the height of an object."""
    if not obj_coords:
        return 0
    min_row = min(r for r, _ in obj_coords)
    max_row = max(r for r, _ in obj_coords)
    return max_row - min_row + 1


def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find all objects in the input grid
    objects = find_objects(input_grid)
    
    # Duplicate based on color
    for color, obj_list in objects.items():
        for obj_coords in obj_list:
            obj_width = get_object_width(obj_coords)
            obj_height = get_object_height(obj_coords)

            if color != 8:  # All colors except 8
                # Duplicate one full object-width to the right
                for r, c in obj_coords:
                    output_grid[r,c] = color
                    new_c = min(cols - 1, c + obj_width)
                    
                    #check other color on the right
                    if output_grid[r,new_c] !=0 and output_grid[r,new_c]!=color:
                        output_grid[r,new_c] = color
                    else:
                        output_grid[r,new_c] = color
            
            elif color == 8:
                for r,c in obj_coords:
                    output_grid[r,c] = 8
                
                #check adj
                has_adjacent = False
                adjacent_obj_coords = []
                for r, c in obj_coords:
                    if c + 1 < cols and input_grid[r,c+1] != 8 and input_grid[r,c+1]!=0:
                        has_adjacent = True
                        adjacent_obj_coords.append((r,c+1))

                    elif c -1 >= 0 and input_grid[r,c-1] !=8 and input_grid[r,c-1] !=0:
                        has_adjacent = True
                        adjacent_obj_coords.append((r,c-1))
                if has_adjacent:
                    first_adj_r = adjacent_obj_coords[0][0]
                    first_adj_c = adjacent_obj_coords[0][1]
                    adj_color = input_grid[first_adj_r,first_adj_c]

                    #get obj 8 min row
                    min_r = min(r for r,_ in obj_coords)
                    for i in range(obj_height * 2):
                        if min_r - 1 - i >=0:
                            output_grid[min_r - 1 - i,first_adj_c] = 8

    #Expand
    for color, obj_list in objects.items():
            for obj_coords in obj_list:
                obj_width = get_object_width(obj_coords)
                if color == 1:  # Color 1
                    min_row = min(r for r, _ in obj_coords)
                    max_row = max(r for r, _ in obj_coords)
                    for r, c in obj_coords:
                        # Check for adjacent color 2
                        if (r, c + 1) in [(r,c) for obj in objects.get(2,[]) for r,c in obj]: #check for any 2 obj coord
                            for i in range(max_row - min_row+1):
                                output_grid[min(rows-1,r+1+i),c] = 1

                        if output_grid[r,c] !=1: #prevent override
                           output_grid[r,c] = 1
                        
                
                elif color == 6: #color 6
                    for r,c in obj_coords:
                        output_grid[r,min(cols-1,c+obj_width)] = 6
    

    return output_grid
```
