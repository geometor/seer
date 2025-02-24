# 760b3cac • 016 • refine_coder

---
```python
"""
1.  **Identify Objects:** Find all pixels that are azure (8) and group them as a single object. Find all pixels that are yellow (4) and group them as a single object.
2.  **Yellow Object:** The yellow object remains unchanged in its original position and shape.
3.  **Azure Object:**
    *   Find the minimum and maximum row and column of the bounding box around the azure object.
    *   Copy the Azure object.
    *   If the minimum column of the Azure object is > 0, expand the Azure object to fill the area from column 0 to one less than the original minimum column.
    *   If the maximum column of the Azure object is < input_grid.shape[1] - 1, copy and paste each column from the bounding box starting at the first column after the bounding box until it is filled.
"""

import numpy as np

def find_object(grid, color):
    coords = np.argwhere(grid == color)
    if len(coords) == 0:
        return []
    return coords.tolist()

def get_bounding_box(coords):
    if not coords:
        return None
    min_row = min(coords, key=lambda p: p[0])[0]
    max_row = max(coords, key=lambda p: p[0])[0]
    min_col = min(coords, key=lambda p: p[1])[1]
    max_col = max(coords, key=lambda p: p[1])[1]
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify Objects
    azure_object = find_object(input_grid, 8)
    yellow_object = find_object(input_grid, 4)

    # Yellow Object (remains unchanged)
    #   for pixel in yellow_object:
    #     output_grid[pixel[0], pixel[1]] = 4

    # Azure Object Transformation
    if azure_object:
        min_row, max_row, min_col, max_col = get_bounding_box(azure_object)

        # Expand left
        if min_col > 0:
            for r in range(min_row, max_row + 1):
                for c in range(0, min_col):
                    output_grid[r, c] = 8

        # Expand Right
        if max_col < input_grid.shape[1] - 1:
            width = max_col - min_col + 1
            offset = 0
            for col in range(max_col + 1, input_grid.shape[1]):
              for row in range(min_row, max_row+1):
                original_col = min_col + (offset % width)
                output_grid[row, col] = input_grid[row, original_col]
              offset+=1

    return output_grid
```
