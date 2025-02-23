# AboveBelow3 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation involves moving the yellow rectangle at the top, one position downwards, keeping the rest.
"""

import numpy as np

def find_object(grid, color, shape_type=None, size=None):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                if shape_type == 'rectangle':
                    width, height = 0, 0
                    # Check for rectangle
                    c_temp = c
                    while c_temp < cols and grid[r, c_temp] == color:
                        width += 1
                        c_temp += 1
                    r_temp = r
                    while r_temp < rows and grid[r_temp, c] == color:
                        height += 1
                        r_temp += 1
                    
                    if size is None or (width, height) == size or (height, width) == size:
                         # Mark as visited
                        for i in range(r, r + height):
                            for j in range(c, c+width):
                                visited[i,j] = True
                        objects.append(( (r, c), (width, height) ))


                elif shape_type == 'square':
                    size_count = 0

                    #check for square

                    c_temp = c
                    while c_temp < cols and grid[r, c_temp] == color:
                        size_count +=1
                        c_temp += 1

                    r_temp = r
                    while r_temp < rows and grid[r_temp, c] == color:

                        if size_count != 0 and grid[r_temp,c:c+size_count].tolist() != [color]*size_count:
                            break
                        size_count_row = 0
                        for inner_c in range(c, c+size_count):
                            if inner_c < cols and grid[r_temp, inner_c] == color :
                                size_count_row +=1
                            else:
                                break

                        if size_count_row != size_count:

                            break;
                        r_temp+=1
                    
                    if size_count_row == size_count:


                        if size is None or size_count == size:

                            for i in range(r, r + size_count):
                                for j in range(c, c+size_count):
                                    visited[i,j] = True
                            objects.append(( (r, c), (size_count, size_count) ))

                else:
                    # No shape specified, just return the coordinate.  Not really an object.
                    objects.append(((r,c), (1,1)))
    return objects

def move_object(grid, start_pos, size, dr, dc):
    new_grid = np.copy(grid)
    r, c = start_pos
    width, height = size

    # Clear old position
    for i in range(r, min(r + height,new_grid.shape[0])):
        for j in range(c, min(c+width, new_grid.shape[1])):
            new_grid[i, j] = 0

    # Set new position
    new_r, new_c = r + dr, c + dc
    for i in range(new_r, min(new_r + height, new_grid.shape[0])):
        for j in range(new_c, min(new_c+width,new_grid.shape[1])):
            new_grid[i, j] = grid[r,c] #original color

    return new_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the 1x2 yellow rectangle
    yellow_rects = find_object(output_grid, 4, 'rectangle', (1,2))
    yellow_rect = None
    for rect in yellow_rects:
      if rect[0][0] < input_grid.shape[0]/2:
        yellow_rect = rect
        break


    if yellow_rect:

        # Move the yellow rectangle down by one row
      output_grid = move_object(output_grid, yellow_rect[0], yellow_rect[1], 1, 0)


    return output_grid
```
