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

**Observations and Documentation**

Here's a YAML block summarizing my initial findings:

```yaml
task: 001-example_1
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: L-shape (top-left)
      position: (1,1) , (2,1), (2,2)
    - color: 8 (azure)
      shape: L-shape (bottom-right)
      position: (3,4) , (3,5), (4,5)
    - color: 0 (white)
      shape: background
      position: fills the rest
output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: L-shape (top-left)
      position: (1,1) , (2,1), (2,2)
    - color: 8 (azure)
      shape: L-shape (bottom-right)
      position:  (3,4) , (3,5), (4,5)
    - color: 1 (blue)
      shape: single cell
      position: (1,2)
    - color: 1 (blue)
      shape: single cell
      position: (4,4)
    - color: 0 (white)
      shape: background
      position: fills the rest
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. In this case, there are two L-shaped objects.

2.  **Preserve Azure Objects:** The azure objects remain unchanged in their positions and shapes in the output grid.

3.  **Introduce Blue Pixels:** For each azure object, identify the cell immediately to the right of the top-most and left-most corner of the "L". Change the color of these cells to blue (color 1).

    *   For the top-left L-shape, this cell is (1, 2).
    *    For the bottom-right L-shape, this is the cell (4,4).

4. Fill with the color white all the cells that are not azure or blue.

**Natural Language Program**
```
input:  a grid of pixels with colors from 0 to 9.
output: a grid of pixels with colors from 0 to 9.

program:
  for each azure (8) object in input:
    copy object to the output
    let P be the top-left corner of the bounding box that contains the object
    paint in blue the pixel at P.right
  paint in white all other pixels
```

```python
"""
Copies azure (color 8) objects from the input grid to the output grid.
For each azure object, a blue (color 1) pixel is placed immediately to the right of the top-left corner of the object.
All other pixels are set to white (color 0).
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def get_top_left_corner(object_coords):
    min_row = min(coord[0] for coord in object_coords)
    min_col = min(coord[1] for coord in object_coords)

    #find the coordinate that has min_row and min_col
    for row,col in object_coords:
        if row == min_row and col == min_col:
          return (row,col)
    return None #should never happen


def transform(input_grid):
    # Initialize output_grid with zeros (white)
    output_grid = np.zeros_like(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Copy azure objects to output and place blue pixels
    for obj in azure_objects:
        for row, col in obj:
            output_grid[row, col] = 8  # Copy azure pixel
        top_left = get_top_left_corner(obj)

        #place to the right
        blue_row, blue_col = top_left
        blue_col +=1

        #check boundaries
        if blue_col < output_grid.shape[1]:
          output_grid[blue_row, blue_col] = 1  # Place blue pixel

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

![Image](003-example_2_input.png)


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

![Image](003-example_2_output.png)

Okay, let's analyze the second example.

**Observations and Documentation**

```yaml
task: 003-example_2
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: L-shape (top-right)
      position: (0,4), (0,5), (1,5)
    - color: 8 (azure)
      shape: L-shape (middle-left)
      position: (2,2), (3,2), (3,3)
    - color: 8 (azure)
      shape: L-shape (bottom-right)
      position: (5,4), (6,4), (6,5)
    - color: 0 (white)
      shape: background
      position: fills the rest
output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: L-shape (top-right)
      position: (0,4), (0,5), (1,5)
    - color: 8 (azure)
      shape: L-shape (middle-left)
      position: (2,2), (3,2), (3,3)
    - color: 8 (azure)
      shape: L-shape (bottom-right)
      position: (5,4), (6,4), (6,5)
    - color: 1 (blue)
      shape: single cell
      position: (0,5) -> (1,4)  # Corrected position
    - color: 1 (blue)
      shape: single cell
      position: (2,2) -> (3,3) # Corrected position
     - color: 1 (blue)
      shape: single cell
      position: (5,4) -> (6,3) # Corrected position
    - color: 0 (white)
      shape: background
      position: fills the rest
```

**Determining the Transformation Rule**

The transformation rule is identical to the previous example:

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid.

2.  **Preserve Azure Objects:** Copy all azure objects to the output grid without any changes in position or shape.

3.  **Introduce Blue Pixels:** For each azure object, add a blue (color 1) pixel. The blue pixel's location is immediately to the right of the top-left-most pixel of the azure object.

4.  **Fill Remaining Pixels:** The rest of the output grid remains filled with white (color 0).

**Natural Language Program**
```
input:  a grid of pixels with colors from 0 to 9.
output: a grid of pixels with colors from 0 to 9.

program:
  for each azure (8) object in input:
    copy object to the output
    let P be the top-left corner of the bounding box that contains the object
    paint in blue the pixel at P.right
  paint in white all other pixels
```

The Python code developed for the first example should work correctly for this example as well, as the underlying transformation rule is the same.

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
