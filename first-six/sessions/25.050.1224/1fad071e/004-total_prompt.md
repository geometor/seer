# 1fad071e • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 2 2 0 0 1
0 1 1 0 2 2 0 0 0
0 1 1 0 0 0 0 2 2
0 0 0 0 0 0 0 2 2
1 0 2 2 0 0 0 0 0
0 0 2 2 0 1 1 0 0
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 1
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x79CABB63B6D0>

**output**
```
1 1 0 0 0
```

<PIL.Image.Image image mode=RGB size=320x64 at 0x79CABB63B520>
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation**

```yaml
input_grid:
  size: [9, 9]
  objects:
    blue:
      - shape: irregular
        positions: [[1, 1], [1, 2], [2, 1], [2, 2], [6,5], [6,6], [5,5], [5,6], [0,8], [8,1], [8,8]]
    red:
      - shape: square
        positions: [[0, 4], [0, 5], [1, 4], [1, 5]]
      - shape: square
        positions: [[2, 7], [2, 8], [3, 7], [3, 8]]
      - shape: square
        positions: [[4, 2], [4, 3], [5, 2], [5, 3]]
    white:
      - shape: background
        positions: all other cells
```

**Natural Language Program**

Here's a step-by-step description of the transformation, focusing on objects, predicates, and actions:

1.  **Identify Objects:** In the input grid, we observe objects of three colors, blue, red, and white. The blue and red colors create squares (composed by 4 cells of same color). The rest of the cells are white (color 0), and they form an irregular shape.

2.  **Predicate:** The predicate of interest is location and shape. There is not an agent.

3.  **Filter specific objects:** Select the first two blue objects starting from the upper left corner and scanning each row from left to right.
    The two selected blue objects have coordiantes:
      - [[1, 1], [1, 2], [2, 1], [2, 2]]
      - [[0, 8]]

4.  **Extract a Property:** List of the unique x-coordinates occupied by selected blue objects.
     - [1,2]
     - [8]

5.  **Build the output:** Create an output of length equal to the double of the previous list plus one. Put 1 in each cell of the output that have index included in the list, and zero otherwise.

**Transformation Rule Summary**

The transformation consists on:
   - scanning the grid from left to right and from top to bottom.
   - selecting the first two blue objects.
   - extracting the x-coordinates of their cells.
   - removing duplicates,
   - creating a new grid 1 row grid
   - setting its values to 1 when their index exists in the x-coordinates list or 0 otherwise.

```python
"""
The transformation consists on:
   - scanning the grid from left to right and from top to bottom.
   - selecting the first two blue objects.
   - extracting the x-coordinates of their cells.
   - removing duplicates,
   - creating a new grid 1 row grid
   - setting its values to 1 when their index exists in the x-coordinates list or 0 otherwise.
"""

import numpy as np

def get_objects(grid, color):
    """
    Find objects of a specific color in the grid.
    Returns a list of lists of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))
        
        # Explore adjacent cells
        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Find blue objects
    blue_objects = get_objects(input_grid, 1)

    # Select the first two blue objects
    selected_objects = blue_objects[:2]

    # Extract x-coordinates
    x_coordinates = []
    for obj in selected_objects:
        for x, y in obj:
            x_coordinates.append(y)

    # Remove duplicates and sort
    unique_x_coordinates = sorted(list(set(x_coordinates)))

    #create output grid
    output_length = len(unique_x_coordinates)*2+1
    output_grid = np.zeros(output_length, dtype=int)

    #set 1
    for x in unique_x_coordinates:
      output_grid[x] = 1

    return output_grid.reshape(1,-1)
```

**input**
```
1 1 0 2 0 0 0 0 2
1 1 0 0 0 1 1 0 0
0 0 0 2 0 1 1 0 0
0 0 0 0 0 0 0 0 1
0 1 1 0 2 2 0 0 0
0 1 1 0 2 2 0 0 2
0 0 0 0 0 0 0 0 0
0 0 0 2 2 0 1 1 0
0 1 0 2 2 0 1 1 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x79CABB63B6A0>

**output**
```
1 1 1 1 0
```

<PIL.Image.Image image mode=RGB size=320x64 at 0x79CABAB78640>
Okay, let's analyze the second example.

**YAML Observation**

```yaml
input_grid:
  size: [9, 9]
  objects:
    blue:
      - shape: square
        positions: [[0, 0], [0, 1], [1, 0], [1, 1]]
      - shape: square
        positions: [[1, 5], [1, 6], [2, 5], [2, 6]]
      - shape: single
        positions: [[3,8]]
      - shape: square
        positions: [[4,1], [4,2], [5,1], [5,2]]    
      - shape: single
        positions: [[8,1]]
      - shape: square
        positions: [[7,6], [7,7], [8,6], [8,7]]          
    red:
      - shape: single
        positions: [[0,3]]
      - shape: single
        positions: [[2,3]]
      - shape: square
        positions: [[4, 4], [4, 5], [5, 4], [5, 5]]
      - shape: single
        positions: [[0,8]]
      - shape: single
        positions: [[5,8]]
      - shape: square
        positions: [[7,3],[7,4], [8,3], [8,4]]
    white:
      - shape: background
        positions: all other cells
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** The input grid contains objects of color blue, red, and white. We are only interested in blue objects.

2.  **Predicate:** The predicate of interest is object order based on a top-to-bottom, left-to-right scan.

3. **Filter Objects:**  Select the first two blue objects, scanning the cells from top to bottom and from left to right.
      - [[0, 0], [0, 1], [1, 0], [1, 1]]
      - [[1, 5], [1, 6], [2, 5], [2, 6]]

4.  **Extract a Property:** List of the unique x-coordinates occupied by selected blue objects.
     - [0,1]
     - [5,6]

5.  **Build the output:** Create an output of length equal to the double of the previous list plus one. Put 1 in each cell of the output that have index included in the list, and zero otherwise.

**Transformation Rule Summary**

The transformation is identical to the first example, but the second example gives a new insight on the first two selected blue squared.
The new rule is:
   - scanning the grid from left to right and from top to bottom.
   - selecting the first two blue objects.
   - extracting the x-coordinates of their cells.
   - removing duplicates,
   - creating a new grid 1 row grid
   - setting its values to 1 when their index exists in the x-coordinates list or 0 otherwise.

```python
"""
The transformation is identical to the first example, but the second example gives a new insight on the first two selected blue squared.
The new rule is:
   - scanning the grid from left to right and from top to bottom.
   - selecting the first two blue objects.
   - extracting the x-coordinates of their cells.
   - removing duplicates,
   - creating a new grid 1 row grid
   - setting its values to 1 when their index exists in the x-coordinates list or 0 otherwise.
"""

import numpy as np

def get_objects(grid, color):
    """
    Find objects of a specific color in the grid.
    Returns a list of lists of coordinates.
    """
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))
        
        # Explore adjacent cells
        dfs(x + 1, y, current_object)
        dfs(x - 1, y, current_object)
        dfs(x, y + 1, current_object)
        dfs(x, y - 1, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # Find blue objects
    blue_objects = get_objects(input_grid, 1)

    # Select the first two blue objects
    selected_objects = blue_objects[:2]

    # Extract x-coordinates
    x_coordinates = []
    for obj in selected_objects:
        for x, y in obj:
            x_coordinates.append(y)

    # Remove duplicates and sort
    unique_x_coordinates = sorted(list(set(x_coordinates)))

    #create output grid
    output_length = len(unique_x_coordinates)*2+1
    output_grid = np.zeros(output_length, dtype=int)

    #set 1
    for x in unique_x_coordinates:
      output_grid[x] = 1

    return output_grid.reshape(1,-1)
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
