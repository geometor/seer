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

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two separate 2x1 rectangles
        positions:
          - (1,1), (2,1) # First rectangle
          - (3,4), (4,4) # Second rectangle
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two separate 2x1 rectangles
        positions:
          - (1,1), (2,1) # First rectangle
          - (3,4), (4,4) # Second rectangle
      - color: 1 (blue)
        shape: two separate 1x1 squares
        positions:
          - (1,2) # Next to the first rectangle
          - (4,3) # next to the second rectangle
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all azure (color 8) colored objects in the input grid. These exist as two separate 2x1 vertical rectangles.

2.  **Determine Placement:** For each azure rectangle, identify its location and dimensions.

3.  **Add Blue Pixels:** For each azure 2x1 rectangle:
    *   If the azure rectangle is in the top left quadrant of the grid add a blue (color 1) pixel to its right.
    *   If the azure rectangle is in the bottom rigth quadrant of the grid add a blue (color 1) pixel to its left.

4. **Maintain the rest:** All other cells in the input grid remain unchanged.

In essence, the transformation rule preserves the azure rectangles and adds a single blue pixel adjacent to specific sides of each azure rectangle based in its position.

```python
"""
The transformation rule preserves the azure (color 8) rectangles and adds a single blue (color 1) pixel adjacent to each azure rectangle. The blue pixel is added to the right of the rectangle if it is in the top-left quadrant, and to the left if in the bottom-right quadrant.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of (row, col) tuples for each object found.
    """
    objects = []
    visited = set()

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

def is_2x1_rectangle(object_coords):
    """
    Checks if the object represented by the given coordinates is a 2x1 rectangle.
    """
    if len(object_coords) != 2:
        return False

    row_coords = sorted(list(set([coord[0] for coord in object_coords])))
    col_coords = sorted(list(set([coord[1] for coord in object_coords])))

    if len(row_coords) == 2 and len(col_coords) == 1 and row_coords[1] - row_coords[0] == 1:
        return True
    
    return False
    

def transform(input_grid):
    """
    Transforms the input grid according to the rule: adds a blue pixel next to azure 2x1 rectangles.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for azure_object in azure_objects:
        if is_2x1_rectangle(azure_object):
            #get centroid
            centroid_row = sum([coord[0] for coord in azure_object]) / len(azure_object)
            centroid_col = sum([coord[1] for coord in azure_object]) / len(azure_object)

            rows, cols = input_grid.shape
            
            # get sorted row and cols
            row_coords = sorted(list(set([coord[0] for coord in azure_object])))
            col_coords = sorted(list(set([coord[1] for coord in azure_object])))
            
            if centroid_row < rows / 2 and centroid_col < cols/2:  # Top-left quadrant
                output_grid[row_coords[0], col_coords[0] + 1] = 1
            elif centroid_row >= rows/2 and centroid_col >= cols/2: # Bottom Right Quadrant
                output_grid[row_coords[0], col_coords[0] - 1] = 1
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

Okay, let's analyze the transformation between the second input and output grids.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: three separate 2x1 rectangles
        positions:
          - (0,4), (0,5) # First rectangle
          - (2,2), (3,2) # Second rectangle
          - (3,3), (6,3) # third rectangle
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: three separate 2x1 rectangles
        positions:
          - (0,4), (0,5) # First rectangle
          - (2,2), (3,2) # Second rectangle
          - (3,3), (6,3) # third rectangle
      - color: 1 (blue)
        shape: three separate 1x1 squares
        positions:
          - (1,4) # Next to the first rectangle
          - (2,3) # next to the second rectangle
          - (5,3)
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** Locate all azure (color 8) colored objects in the input grid. These exist as three separate 2x1 vertical/horizontal rectangles.

2.  **Determine Placement:** For each azure rectangle, identify its location and dimensions.

3.  **Add Blue Pixels:** For each azure 2x1 rectangle:
    *   If the azure rectangle is in the top right quadrant of the grid add a blue (color 1) pixel to its left. Specifically, the coordinate is calculated as:
        + x: the first row coordinate of the rectangle,
        + y: first column coordinate - 1.
    *   If the azure rectangle is in the top left quadrant of the grid add a blue (color 1) pixel to its right. Specifically, the coordinate is calculated as:
        + x: the first row coordinate of the rectangle,
        + y: first column coordinate + 1.
    * If the azure rectangle is in the bottom rigth quadrant of the grid add a blue (color 1) pixel to its left.
    *   If the azure rectangle is in the bottom left quadrant of the grid, check if the rectangule is at the border of the quadrant. For that, the coordinates must be calculated as:
         + x: the smallest row coordinate of the rectangle - 1,
         + y: first column coordinate.

4.  **Maintain the Rest:** All other cells in the input grid remain unchanged.

In essence, the transformation rule preserves the azure rectangles and adds a single blue pixel adjacent to specific sides of each azure rectangle based in its position, confirming the previously developed natural language description.

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
