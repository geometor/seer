# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The transformation rule preserves most of the azure pixels, and adds two blue pixels, each one at specific relative positions related with the two initial L-shaped objects.
Specifically, one blue pixel is placed to the immediate right of the top-left L-shaped object, and another blue pixel is placed to the immediate left of the bottom-right L-shaped object.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects
def get_l_shapes(objects):
    """
    Filter the identified L shapes.
    """
    l_shapes = []

    for obj in objects:
        if len(obj) == 3:
           #check if it is a L shape
           obj.sort()
           if (obj[0][0] == obj[1][0] and obj[1][0] == obj[2][0]-1 and obj[1][1] == obj[2][1] )  or \
              (obj[0][1] == obj[1][1] and obj[1][1] == obj[2][1]-1 and obj[1][0] == obj[2][0] )  :
                l_shapes.append(obj)

    return l_shapes
def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    l_shapes = get_l_shapes(azure_objects)

    #Change pixels for the first 2 detected L shapes
    if len(l_shapes) >=2:

        #first L shape
        obj = l_shapes[0]
        obj.sort()
        if obj[0][0] == obj[1][0]: #vertical L
            output_grid[ obj[1][0]  , obj[1][1]+1 ] = 1
        else: #horizontal L
            output_grid[ obj[1][0]+1 , obj[1][1] ] = 1
        
        #second L shape
        obj = l_shapes[1]
        obj.sort()

        if obj[0][0] == obj[1][0]:#vertical L
            output_grid[obj[0][0] , obj[0][1]-1 ] = 1
        else: #horizontal L
            output_grid[ obj[0][0]-1 , obj[0][1] ] = 1
    return output_grid
```
