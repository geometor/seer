# 3-1e0a9b12 • 006 • example_3 - CODE

---
```python
"""
The program slides clusters of colored pixels down, merging similar objects, and fills empty pixels.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous non-zero pixel regions in a grid, considering each row separately."""
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        current_object = []
        for c in range(cols):
            if grid[r, c] != 0:
                current_object.append((r, c))
            else:
                if current_object:
                    objects.append(current_object)
                    current_object = []
        if current_object:  # Handle objects at the end of a row
            objects.append(current_object)
    return objects

def move_object_down(grid, object_pixels):
    """Moves an object down one step, merging if necessary."""
    rows, cols = grid.shape
    new_positions = []
    can_move = True
    
    #Check for merge, by checking spots under
    merge_target_row = -1
    for r, c in object_pixels:
        if r + 1 >= rows: #Object cannot move if at the bottom
           can_move = False
           break
        if grid[r + 1, c] != 0 and (r + 1, c) not in object_pixels:  # Check for merge
            merge_target_row = r+1
            break

    if not can_move:
        return object_pixels, False #Return original

    if merge_target_row > -1:
       #Merge is happening
       combined_object_pixels = object_pixels.copy()
       for r in range(merge_target_row,rows):
          for c in range(cols):
             if grid[r,c] != 0 and (r,c) not in combined_object_pixels:
                combined_object_pixels.append((r,c))
       #remove dupes and sort
       combined_object_pixels = sorted(list(set(combined_object_pixels)))
       return move_object_down(grid, combined_object_pixels)

    #Normal Move
    for r, c in object_pixels:
        if r + 1 >= rows or (grid[r + 1, c] != 0 and (r+1,c) not in object_pixels):  # Check for collision or boundary
            can_move = False
            break
        new_positions.append((r + 1, c))

    if can_move:
        return new_positions, True
    else:
        return object_pixels, False
    

def transform(input_grid):
    """
    Transforms the input grid by sliding clusters of colored pixels down, merging,
    and filling the background.
    """
    grid = np.array(input_grid)  # Work with a NumPy array
    output_grid = np.zeros_like(grid)

    objects = find_objects(grid)

    # Move objects down iteratively until no more movement is possible
    moved = True
    while moved:
        moved = False
        new_objects = []
        
        for obj in objects:
          
            moved_obj, did_move = move_object_down(grid, obj)

            if did_move:
                moved = True

            new_objects.append(moved_obj)
           
        #Rebuild the grid
        grid = np.zeros_like(grid)
        for obj_pix in new_objects:
          for r,c in obj_pix:
            grid[r,c] = input_grid[obj_pix[0][0],obj_pix[0][1]] #Original color
            
        objects = new_objects #Update current objects

    # Copy final moved positions from grid
    output_grid = grid.copy()
    
    return output_grid.tolist()
```
