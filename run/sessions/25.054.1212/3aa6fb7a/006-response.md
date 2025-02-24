# 3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify Azure Objects:** Find all distinct, contiguous groups of azure (8) pixels in the input grid.

2.  **Determine Bounding Box:**  Calculate the bounding box for each azure object.

3.  **Blue Pixel Placement:** For each azure object, place a *single* blue (1) pixel adjacent to one of the azure pixels of that object, if possible. Placement follows this logic:
    - check to see if placing *to the right* of a top-right azure pixel is possible
    - if not possible, then check to see if placing to the *left* of a bottom-left azure pixel is possible.
    - if not possible (edge of grid, or non-white adjacent cell), then do not place a blue pixel

4.  **Preservation:** All non-azure pixels in the input, that are not chosen for blue pixel placement, remain unchanged in the output grid.
"""

import numpy as np

def find_objects(grid, color):
    """Finds all contiguous objects of a given color."""
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_bounding_box(obj):
    """Calculates the bounding box of an object."""
    min_row = min(pixel[0] for pixel in obj)
    max_row = max(pixel[0] for pixel in obj)
    min_col = min(pixel[1] for pixel in obj)
    max_col = max(pixel[1] for pixel in obj)
    return (min_row, min_col), (max_row, max_col)

def get_top_right_azure_pixel(obj):
    """Returns the top-right azure pixel within an object"""
    top_right = None
    for r,c in obj:
        if top_right is None:
            top_right = (r,c)
        elif r < top_right[0]: # lower row number is higher
            top_right = (r,c)
        elif r == top_right[0] and c > top_right[1]: # rightmost is bigger col
            top_right = (r,c)

    return top_right

def get_bottom_left_azure_pixel(obj):
    """Returns the bottom-left azure pixel"""
    bottom_left = None
    for r, c in obj:
        if bottom_left is None:
            bottom_left = (r,c)
        elif r > bottom_left[0]:
            bottom_left = (r,c)
        elif r == bottom_left[0] and c < bottom_left[1]:
            bottom_left = (r,c)

    return bottom_left
    
def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through azure objects
    for obj in azure_objects:
        
        placed = False
        # attempt to place to right of top-right azure pixel
        top_right_azure = get_top_right_azure_pixel(obj)
        
        if top_right_azure is not None:
            tr_row, tr_col = top_right_azure
            if tr_col + 1 < input_grid.shape[1] and input_grid[tr_row, tr_col + 1] == 0:
                output_grid[tr_row, tr_col+1] = 1
                placed = True

        # attempt to place to left of bottom-left azure pixel, if no placement yet
        if not placed:
            bottom_left_azure = get_bottom_left_azure_pixel(obj)
            
            if bottom_left_azure is not None:
                bl_row, bl_col = bottom_left_azure
                if bl_col - 1 >= 0 and input_grid[bl_row, bl_col-1] == 0:
                   output_grid[bl_row, bl_col - 1] = 1
                   placed = True # not strictly necessary

    return output_grid
```
