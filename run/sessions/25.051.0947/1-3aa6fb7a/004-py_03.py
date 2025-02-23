"""
The transformation rule can be described as follows:

1.  **Identify Azure Objects:** Find all azure (color 8) objects in the input grid. These objects consist of two cells, either horizontally or vertically aligned.

2.  **Preserve Azure Objects:** Copy the azure objects to the output grid without any changes in position or shape.

3.  **Locate Top-Right Azure Pixel:** Find the azure pixel that has the largest column index (rightmost). If there is a tie between multiple azure pixels in column index, select the one with smallest row index (uppermost) among these.

4.  **Add Blue Pixel to the Top-Right:** Place a blue pixel (color 1) immediately to the right of the azure pixel identified in step 3. Ensure the new pixel is within the grid boundaries.

5. **Locate Bottom-Left Azure Pixel:** Find the azure object that has the smallest column value and and largest row index.

6.  **Add Blue Pixel to the Bottom-Left:** Place a blue pixel (color 1) immediately to the left of the azure pixel identified in step 5. Ensure the new pixel is within the grid boundaries.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds all contiguous objects of a given color in a grid.
    """
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Find top-right azure pixel
    top_right_pixel = (-1, -1)
    for obj in azure_objects:
        for r, c in obj:
            if c > top_right_pixel[1]:
                top_right_pixel = (r, c)
            elif c == top_right_pixel[1] and r < top_right_pixel[0]:
                top_right_pixel = (r, c)

    # Add blue pixel to the right
    if top_right_pixel != (-1, -1) and top_right_pixel[1] + 1 < output_grid.shape[1]:
        output_grid[top_right_pixel[0], top_right_pixel[1] + 1] = 1

    # Find bottom-left azure pixel
    bottom_left_pixel = (input_grid.shape[0], input_grid.shape[1] )

    for obj in azure_objects:
        for r,c in obj:
            if c < bottom_left_pixel[1]:
                bottom_left_pixel = (r,c)
            elif c == bottom_left_pixel[1] and r > bottom_left_pixel[0]:
                bottom_left_pixel = (r,c)

    # Add blue pixel to the left
    if bottom_left_pixel != (input_grid.shape[0], input_grid.shape[1] ) and bottom_left_pixel[1] - 1 >= 0:
        output_grid[bottom_left_pixel[0], bottom_left_pixel[1] - 1] = 1

    return output_grid