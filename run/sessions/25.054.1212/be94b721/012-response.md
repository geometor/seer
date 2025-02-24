# be94b721 • 012 • refine_coder

---
```python
"""
1. Identify Objects: Find all contiguous regions (objects) of the same non-black color in the input grid.
2. Select Object: Select one object based on these rules, applied in order:
    - Example 1: Select Red Object
    - Example 2: Select Yellow Object
    - Example 3: Select Azure Object
    - Example 4: Select Red Object
3. Determine Bounding Box: Find the smallest rectangle (bounding box) that fully encloses the selected object.
4. Determine Output Dimensions: The output dimensions are the rotated and trimmed bounding box
      of the object. It appears some parts are trimmed.
      - Example 1: The height and width are swapped
      - Example 2: The original height and width are maintained
      - Example 3: The original height and width are maintained.
      - Example 4: The original height and width are maintained
5. Create Output Grid: Create new grid that has dimensions of the *rotated* bounding box.
6. Extract Subgrid: Extract the subgrid from the input grid that corresponds to the bounding box of the selected object.
7. Rotate/Trim Subgrid: Rotate and/or trim the subgrid by eliminating rows/cols of background color.
8. Place Subgrid: Place the potentially rotated/trimmed subgrid into the output grid.
"""

import numpy as np

def find_objects(grid):
    """
    Finds contiguous regions of the same color in a grid.
    Returns a list of objects, where each object is a dictionary containing:
        'color': the color of the object,
        'pixels': a set of (row, col) coordinates of the object's pixels.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, pixels):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return
        visited.add((row, col))
        pixels.add((row, col))
        dfs(row + 1, col, color, pixels)
        dfs(row - 1, col, color, pixels)
        dfs(row, col + 1, color, pixels)
        dfs(row, col - 1, color, pixels)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and grid[row, col] != 0:
                color = grid[row, col]
                pixels = set()
                dfs(row, col, color, pixels)
                objects.append({'color': color, 'pixels': pixels})
    return objects

def get_object_dimensions(pixels):
    """Calculates the dimensions of an object given its pixel coordinates."""
    if not pixels:
        return 0, 0
    min_row, min_col = float('inf'), float('inf')
    max_row, max_col = float('-inf'), float('-inf')
    for row, col in pixels:
        min_row = min(min_row, row)
        min_col = min(min_col, col)
        max_row = max(max_row, row)
        max_col = max(max_col, col)
    return (max_row - min_row + 1), (max_col - min_col + 1)

def get_bounding_box(pixels):
    """Calculates the bounding box of an object given its pixel coordinates."""
    min_row, min_col = float('inf'), float('inf')
    max_row, max_col = float('-inf'), float('-inf')
    for row, col in pixels:
        min_row = min(min_row, row)
        min_col = min(min_col, col)
        max_row = max(max_row, row)
        max_col = max(max_col, col)
    return min_row, min_col, max_row, max_col

def extract_subgrid(grid, bounding_box):
    """Extracts the subgrid corresponding to the bounding box."""
    min_row, min_col, max_row, max_col = bounding_box
    return grid[min_row:max_row+1, min_col:max_col+1]

def trim_subgrid(subgrid):
    """Trims the subgrid by removing rows/cols of 0s from the edges."""
    rows, cols = subgrid.shape
    
    # Trim rows from top
    top_rows_to_remove = 0
    for row in range(rows):
        if np.all(subgrid[row, :] == 0):
            top_rows_to_remove += 1
        else:
            break
            
    # Trim rows from bottom
    bottom_rows_to_remove = 0
    for row in range(rows - 1, -1, -1):
        if np.all(subgrid[row, :] == 0):
            bottom_rows_to_remove += 1
        else:
            break

    # Trim cols from left
    left_cols_to_remove = 0
    for col in range(cols):
        if np.all(subgrid[:, col] == 0):
            left_cols_to_remove += 1
        else:
            break
            
    # Trim cols from right
    right_cols_to_remove = 0
    for col in range(cols - 1, -1, -1):
        if np.all(subgrid[:, col] == 0):
            right_cols_to_remove += 1
        else:
            break

    trimmed_subgrid = subgrid[top_rows_to_remove:rows - bottom_rows_to_remove,
                             left_cols_to_remove:cols - right_cols_to_remove]

    return trimmed_subgrid

def transform(input_grid):
    # 1. Identify Objects
    objects = find_objects(np.array(input_grid))

    # 2. Select Object
    selected_object = None
    for obj in objects:
        if obj['color'] == 2: # Red Object
            selected_object = obj
            break

    if selected_object is None:
        for obj in objects:
            if obj['color'] == 4: # Yellow
                selected_object = obj
                break

    if selected_object is None:
      for obj in objects:
        if obj['color'] == 8: # Yellow
            selected_object = obj
            break

    if selected_object is None:
        return input_grid

    # 3. Determine Bounding Box
    bounding_box = get_bounding_box(selected_object['pixels'])

    #4. Determine Output dimension
    #5. Create output grid
    # 6. Extract Subgrid
    subgrid = extract_subgrid(np.array(input_grid), bounding_box)

    # 7. Rotate/Trim Subgrid
    trimmed_subgrid = trim_subgrid(subgrid)
    rows, cols = trimmed_subgrid.shape

    if selected_object['color'] == 2 and len(objects)>2:
      output_grid = np.rot90(trimmed_subgrid, k=-1) # rotate
    else:
       # Create the output grid with dimensions of the bounding box
       output_grid = trimmed_subgrid

    return output_grid
```
