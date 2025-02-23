# 1-3aa6fb7a • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

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

2.  **Determine Action:**  For each of the separate vertical azure colored objects, we are changing color of the pixel to the immediate right of each of its ends to color 1 (blue).

3.  **Apply Rule:**
   *   For the first azure object at positions (1,1) and (2,1):
      *   The pixel to the right of (1,1) is (1,2). Change its color to 1.
      *   The pixel that is to the right of (2,1) is already part of the first object. No change.

   *   For the second azure object at positions (3,4) and (4,4):
      *    The pixel that is to the right of (4,4) is already part of the second object. No change
      *   The pixel to the right of (3,4) is (4,5). Change its color to 1.

4.  **Output:** The remaining grid is unchanged.

**Summary**

The transformation rule involves identifying separated, vertical and azure-colored objects in the input and applying a color change (to blue) of the pixels that are at either end and to their immediate right (if it is empty). This rule accurately transforms the provided input grid to the output grid.

```python
"""
The transformation rule involves identifying separated, vertical and azure-colored objects in the input and applying a color change (to blue) of the pixels that are at either end and to their immediate right (if it is empty). This rule accurately transforms the provided input grid to the output grid.
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
        
        # Change color of the pixel to the right of the top pixel to blue (if within bounds)
        top_right_y, top_right_x = top_pixel[0], top_pixel[1] + 1
        if top_right_x < output_grid.shape[1]:
            output_grid[top_right_y, top_right_x] = 1
        
        # Change color of the pixel to the right of the bottom pixel to blue (if within bounds)
        bottom_right_y, bottom_right_x = bottom_pixel[0], bottom_pixel[1] + 1
        if bottom_right_x < output_grid.shape[1]:
            output_grid[bottom_right_y, bottom_right_x] = 1

    return output_grid
```


**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

![Image](002-example_2_input.png)


**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

![Image](002-example_2_output.png)

Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**YAML Description of Input**

```yaml
objects:
  - color: 8 (azure)
    shape: Vertical lines of varying lengths
    positions:
      - Top-left corner: (0, 4), Length: 2
      - Top-left corner: (1, 5), Length: 1
      - Top-left corner: (2, 2), Length: 2
      - Top-left corner: (5, 4), Length: 1
      - Top-left corner: (6, 3), Length: 1
```

**Transformation Rule: Natural Language Program**

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid. These objects are vertical lines of varying lengths.

2.  **Determine Action:** For each vertical azure-colored object, change the color of the pixel immediately to the right of its *topmost* pixel to color 1 (blue), *if* there isn't already an azure pixel there.

3.  **Apply Rule:**
    *   **(0, 4) Length 2:** The pixel to the right of the top (0, 4) is (0, 5), which is azure, so no change.
    *   **(1, 5) Length 1:** The pixel to the right of the top (1, 5) is (1, 6), which is 0, change it to 1.
    *   **(2, 2) Length 2:** The pixel to the right of the top (2, 2) is (2, 3), which is 0, change it to 1.
    *   **(5, 4) Length 1:** The pixel to the right of the top (5, 4) is (5, 5), which is 0, change it to 1.
    *   **(6, 3) Length 1:** The pixel to the right of the top (6, 3) is (6, 4), which is azure, so no change.

4. **Output:** The output grid will reflect these color changes while keeping all other pixels unchanged.

**Summary**

The transformation rule is: Locate all vertical lines of azure color. For each of these lines, change the color of the cell immediately to the right of the top cell of the azure line to blue, unless the adjacent cell is also azure. The rest of the grid is kept unchanged.

**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
