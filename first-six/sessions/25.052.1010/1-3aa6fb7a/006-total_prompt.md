# 1-3aa6fb7a • 006 • example_2 - CODE

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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Block Summary**

```yaml
observations:
  - object_1:
      color: 8 (azure)
      shape: Two separate 2x1 rectangles
      position: 
        - Top rectangle: Starts at row 2, column 2
        - Bottom rectangle: Starts at row 4, column 5
      count: 2
  - object_2:
      color: 1 (blue)
      shape: single cell 
      position: NA
      count: 2 in the output.
```

**Natural Language Description of the Transformation**

1.  **Identify Objects:** In the input grid, we can identify two separate objects of color 8 (azure). Each object is a 2x1 rectangle.

2.  **Transformation Rule:**
    *   Locate the top right corner of object 1 (top rectangle). Insert color 1 (blue) at this cell.
    *   Locate the bottom left corner of object 2 (bottom rectangle). Insert color 1 (blue) at this cell.

**Explanation of the "Story"**

The transformation rule looks like adding number "1" (blue color) at the corners of shape 8.


```python
"""
The transformation rule involves adding the number "1" (blue color) at specific corners of the azure (color 8) shapes. 
Specifically, a blue cell is inserted at the top-right corner of the top 2x1 azure rectangle and at the bottom-left corner of the bottom 2x1 azure rectangle.
"""

import numpy as np

def find_objects(grid, color):
    """
    Find and return the positions of all 2x1 rectangles of the specified color.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and c+1 < cols and grid[r + 1, c] == color:
                objects.append((r, c))
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find all 2x1 rectangles of color 8 (azure)
    azure_objects = find_objects(output_grid, 8)
    
    # Check if exactly two azure objects are found to apply the rule.
    if len(azure_objects) >= 2:
        # Locate the top-right corner of the first object and insert color 1 (blue)
        top_right_corner = (azure_objects[0][0], azure_objects[0][1] + 1)
        output_grid[top_right_corner] = 1

        # Locate the bottom-left corner of the second object and insert color 1 (blue)
        # Assuming second object is always at the expected index
        bottom_left_corner = (azure_objects[1][0] + 1, azure_objects[1][1])
        output_grid[bottom_left_corner] = 1

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

![Image](005-example_2_input.png)


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

![Image](005-example_2_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Block Summary**

```yaml
observations:
  - object_1:
      color: 8 (azure)
      shape: Three separate 2x1 rectangles and one 1x2 rectangle
      position:
        - Rectangle 1: Starts at row 1, column 5
        - Rectangle 2: Starts at row 3, column 3
        - Rectangle 3: Starts at row 6, column 4
        - Rectangle 4: Starts at row 7, column 3
      count: 4
  - object_2:
      color: 1 (blue)
      shape: single cell
      position: NA
      count: 3 in the output.
```

**Natural Language Description of the Transformation**

1.  **Identify Objects:** In the input grid, we can identify four separate objects of color 8 (azure). Three objects are a 2x1 rectangle, and object 4 is a 1x2 rectangle.

2.  **Transformation Rule:**
    *   Locate the top right corner of object 1 (top rectangle). Insert color 1 (blue) at this cell.
    *   Locate the bottom left corner of object 2 (middle rectangle). Insert color 1 (blue) at this cell.
    *   Locate the top left corner of object 3. Insert color 1 (blue) at this cell.
    * Object 4 is a horizontal rectangle, and there is no modification on this object.

**Explanation of the "Story"**

The transformation rule looks like adding number "1" (blue color) at the corners of shape 8. For the vertical 2x1 rectangles, if the insertion point is at the top-right corner, then insert blue there. Otherwise, if it's at the bottom-left, insert there.

```python
import numpy as np

def find_objects(grid, color):
    """
    Find and return the positions of all 2x1 rectangles of the specified color.
    Also, distinguish between vertical and horizontal rectangles.
    """
    vertical_objects = []
    horizontal_objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            # Vertical 2x1 rectangle
            if r + 1 < rows and grid[r, c] == color and grid[r + 1, c] == color:
                vertical_objects.append((r, c))
            # Horizontal 1x2 rectangle
            if c + 1 < cols and grid[r, c] == color and grid[r, c + 1] == color:
                horizontal_objects.append((r, c))
    return vertical_objects, horizontal_objects

def transform(input_grid):
    output_grid = np.copy(input_grid)
    vertical_azure_objects, horizontal_azure_objects = find_objects(output_grid, 8)
    
    # Apply rules for vertical rectangles
    for obj in vertical_azure_objects:
        r, c = obj
        # Check if it's the top one (by checking above)
        if r > 0 and output_grid[r - 1, c] == 8:  # Part of a >2x1 vertical block
            output_grid[r, c-1] = 1
            
        elif c + 1 < output_grid.shape[1] and output_grid[r,c+1] != 1:  # Can insert at top-right
                output_grid[r, c + 1] = 1
           
        else:
            
            output_grid[r + 1, c] = 1 # Bottom-left insertion
    
    return output_grid
```

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
