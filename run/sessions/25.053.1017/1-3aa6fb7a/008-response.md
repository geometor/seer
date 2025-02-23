# 1-3aa6fb7a • 008 • refine_coder

---
```python
"""
1.  **Identify Azure Objects:** Find all distinct, contiguous groups of azure (8) colored pixels in the input grid.

2.  **Process Each Object:** For each identified azure object:

    a. **Determine Boundaries:** Find the topmost row (minimum row index) and bottommost row (maximum row index) occupied by the object.

    b. **Identify Target Rows:** Determine two target rows:
        *   The row immediately *below* the topmost row, if and only if that row contains azure pixels that are a part of the object.
        *   The row immediately *above* the bottommost row, if and only if that row contains azure pixels that are a part of the object.

    c. **Modify Pixels:** In each of the target rows identified:
        *   Locate the *rightmost* azure pixel within that row.
        *    Change the color of this pixel from azure (8) to blue (1).

3.  **Output:** The result is the modified input grid, with all original pixels unchanged except where specifically altered according to the steps above.
"""

import numpy as np

def find_objects(grid, color):
    # Find contiguous blocks of the specified color
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find objects of color 8 (azure)
    azure_objects = find_objects(output_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Find the top and bottom rows of the object
        rows = [pixel[0] for pixel in obj]
        top_row = min(rows)
        bottom_row = max(rows)
        
        #select the target rows
        target_rows = []

        # Check if the row below the top row is part of the object and contains azure pixels
        if top_row + 1 in rows:
            target_rows.append(top_row + 1)

        # Check if the row above the bottom row is part of the object and contains azure pixels.
        if bottom_row - 1 in rows:
            target_rows.append(bottom_row - 1)

        # Modify the rightmost pixel in each target row
        for target_row in target_rows:
            target_pixels = [pixel for pixel in obj if pixel[0] == target_row and output_grid[pixel[0], pixel[1]] == 8]
            if target_pixels:
                rightmost_pixel = max(target_pixels, key=lambda x: x[1])
                output_grid[rightmost_pixel[0], rightmost_pixel[1]] = 1

    return output_grid
```
