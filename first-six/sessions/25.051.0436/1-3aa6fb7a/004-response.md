# 1-3aa6fb7a • 004 • example_2 - CODE

---
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Input**

```yaml
objects:
  - color: 8 (azure)
    shape: Two separate 2x1 vertical lines
    positions:
      - (1,1) and (2,1) # y, x coordinates of the top-left corner
      - (3,4) and (4,4) # y, x coordinates of the top-left corner
```

**Transformation Rule: Natural Language Program**

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid. In this case, there are two separate 2x1 vertical lines of azure color.

2.  **Determine Action:** For each vertical azure-colored object, change the color of the pixel immediately to the right of its *topmost* and *bottom-most* pixels to color 1 (blue), *if* the pixel to its right is not azure.

3.  **Apply Rule:**
    *   For the first azure object at positions (1,1) and (2,1):
        *   The pixel to the right of (1,1) is (1,2). Change its color to 1.
    *   For the second azure object at positions (3,4) and (4,4):
        *   The pixel to the right of (4,4) is (4,5). Change its color to 1.

4.  **Output:** The remaining grid is unchanged.

**Summary**

The transformation rule involves identifying vertical azure-colored objects in the input and applying a color change (to blue) to the pixels immediately to the right of the top and bottom of each object, *if* the pixel to its right is not also azure. This rule accurately transforms the provided input grid to the output grid.

```python
"""
The transformation rule involves identifying vertical azure-colored objects in the input and applying a color change (to blue) to the pixels immediately to the right of the top and bottom of each object, *if* the pixel to its right is not also azure. This rule accurately transforms the provided input grid to the output grid.
"""

import numpy as np

def find_vertical_objects(grid, color):
    objects = []
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    def is_valid(y, x):
        return 0 <= y < rows and 0 <= x < cols

    def dfs(y, x, current_object):
        if not is_valid(y, x) or visited[y, x] or grid[y, x] != color:
            return
        visited[y, x] = True
        current_object.append((y, x))
        dfs(y + 1, x, current_object) # Only check downwards for vertical

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all azure (color 8) vertical objects
    azure_objects = find_vertical_objects(input_grid, 8)
    
    # Iterate through each azure object
    for obj in azure_objects:
        # Sort the object coordinates by row (y-coordinate)
        obj.sort()
        
        # Get the top and bottom pixels of the vertical object
        top_pixel = obj[0]
        bottom_pixel = obj[-1]
        
        # Change color of the pixel to the right of the top pixel to blue (if within bounds and not azure)
        top_right_y, top_right_x = top_pixel[0], top_pixel[1] + 1
        if top_right_x < output_grid.shape[1] and output_grid[top_right_y, top_right_x] != 8:
            output_grid[top_right_y, top_right_x] = 1
        
        # Change color of the pixel to the right of the bottom pixel to blue (if within bounds and not azure)
        bottom_right_y, bottom_right_x = bottom_pixel[0], bottom_pixel[1] + 1
        if bottom_right_x < output_grid.shape[1] and output_grid[bottom_right_y, bottom_right_x] != 8:
            output_grid[bottom_right_y, bottom_right_x] = 1

    return output_grid
```

