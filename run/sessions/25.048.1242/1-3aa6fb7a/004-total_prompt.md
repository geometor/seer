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

<PIL.Image.Image image mode=RGB size=448x448 at 0x75B471615C60>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x75B471616E00>

*text:*
Okay, I'm ready to analyze the transformation between the input and output grids. Here's my breakdown:

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate L-shapes (one inverted)"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (3, 4), (3, 5), (4, 5)]
      shape: "Two separate L-shapes (one inverted)"
    - color: 1 (blue)
      positions: [(1,2), (4,4)]
      shape: "Two single separate pixels."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** In the input grid, we observe two distinct objects of color 8 (azure). One is an "L" shape formed by the pixels at (1, 1), (2, 1), and (2, 2). The other is an inverted "L" shape formed by pixels at (3, 4), (3, 5), and (4, 5).

2.  **Introduce Blue Pixels:**
    *   A blue pixel (color 1) is placed immediately to the right of the topmost azure pixel of the first "L" shape. In other words, from azure pixel (1,1), to the right is (1,2).
    *   A blue pixel (color 1) is placed immediately to the left of the lowest azure pixel of the second "L" shape. In other words, from azure pixel (4,5) to the left is (4,4).

3.  **Preserve other Azure Pixels.** The existing azure pixels from input are not modified.

**Transformation Rule Summary**

The transformation identifies the two azure L-shaped objects and adds a single blue pixel adjacent to a specific point on each of those objects. The first object is identified on the top-left side, and the second L-shaped object is identified on the middle-right side. The rest of the azure pixels remain unchanged.


*text:*
```python
"""
The transformation identifies the two azure L-shaped objects and adds a single blue pixel adjacent to a specific point on each of those objects. The first object is identified on the top-left side, and the second L-shaped object is identified on the middle-right side. The rest of the azure pixels remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        """Depth-first search to find contiguous cells."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_l_shape(object_coords):
    """Checks if a set of coordinates forms an L-shape (normal or inverted)."""
    if len(object_coords) != 3:
        return False

    # Convert list of tuples to a NumPy array for easier manipulation
    coords = np.array(object_coords)

    # Calculate differences between consecutive x and y coordinates
    dx = np.diff(coords[:, 0])
    dy = np.diff(coords[:, 1])
    
    if (np.all(dx == 0) and np.all(np.abs(dy) == 1)) or \
            (np.all(dy == 0) and np.all(np.abs(dx) == 1)):
      return False
    
    # Check for L-shape (2x1, 1x2)
    x_values = coords[:,0]
    y_values = coords[:,1]

    x_range = max(x_values) - min(x_values)
    y_range = max(y_values) - min(y_values)

    return (x_range == 1 and y_range ==1)

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Filter for L-shaped objects
    l_shaped_objects = [obj for obj in azure_objects if is_l_shape(obj)]
    l_shaped_objects.sort(key=lambda obj: (obj[0][0], obj[0][1]))  #sort by top-left

    if len(l_shaped_objects) >= 1:
      first_l_shape = l_shaped_objects[0]
      first_l_shape.sort()
      topmost_pixel = first_l_shape[0]  #top-left
      output_grid[topmost_pixel[0], topmost_pixel[1] + 1] = 1  #put blue to the right

    if len(l_shaped_objects) >= 2:
      second_l_shape = l_shaped_objects[1]
      second_l_shape.sort(reverse=True) # sort by down-right
      bottommost_pixel = second_l_shape[0]  # bottom-right
      output_grid[bottommost_pixel[0], bottommost_pixel[1] - 1] = 1   #put blue to the left

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x75B471615C30>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x75B471615990>

*text:*
Okay, I'm ready to analyze the second pair of input and output grids. Here's my breakdown:

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: "Three separate L-shapes (two inverted, one normal)"
  dimensions: [7, 7]

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(0, 4), (0, 5), (1, 5), (2, 2), (3, 2), (3, 3), (5, 4), (6, 3), (6, 4)]
      shape: "Three separate L-shapes (two inverted, one normal)"
    - color: 1 (blue)
      positions: [(1, 4), (2, 3), (5,3)]
      shape: "Three single separate pixels."
  dimensions: [7, 7]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** In the input grid, there are three distinct L-shaped objects of color 8 (azure).

2.  **Introduce Blue Pixels:**
    *   Consider the first L-shape at top-right. A blue pixel (color 1) is placed immediately to the left of the top-most pixel of the first "L" shape.
    *   Consider the second L-shape at middle-left. A blue pixel (color 1) is placed immediately to the right of the top-most pixel of the first "L" shape.
    *   Consider the third L-shape at bottom-center. A blue pixel (color 1) is placed to the left of the top-most pixel.

3.  **Preserve other Azure Pixels.** The existing azure pixels remain unchanged.

**Transformation Rule Summary**

This transformation identifies three azure L-shaped objects. It introduces three new blue pixels, one adjacent to each of the identified azure L-shapes. The logic to introduce the new blue pixels consistently targets the top-most azure pixel, adding the blue to the left or to the right depending on the position of the object.

```python
"""
This transformation identifies three azure L-shaped objects. It introduces three new blue pixels, one adjacent to each of the identified azure L-shapes. The logic to introduce the new blue pixels consistently targets the top-most azure pixel, adding the blue to the left or to the right depending on the position of the object.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous objects of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        """Depth-first search to find contiguous cells."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_l_shape(object_coords):
    """Checks if a set of coordinates forms an L-shape (normal or inverted)."""
    if len(object_coords) != 3:
        return False

    # Convert list of tuples to a NumPy array for easier manipulation
    coords = np.array(object_coords)

    # Calculate differences between consecutive x and y coordinates
    dx = np.diff(coords[:, 0])
    dy = np.diff(coords[:, 1])
    
    if (np.all(dx == 0) and np.all(np.abs(dy) == 1)) or \
            (np.all(dy == 0) and np.all(np.abs(dx) == 1)):
      return False
    
    # Check for L-shape (2x1, 1x2)
    x_values = coords[:,0]
    y_values = coords[:,1]

    x_range = max(x_values) - min(x_values)
    y_range = max(y_values) - min(y_values)

    return (x_range == 1 and y_range ==1)

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Filter for L-shaped objects
    l_shaped_objects = [obj for obj in azure_objects if is_l_shape(obj)]
    l_shaped_objects.sort(key=lambda obj: (obj[0][0], obj[0][1]))  #sort by top-left

    for i, l_shape in enumerate(l_shaped_objects):
        l_shape.sort() #top-left
        topmost_pixel = l_shape[0]
            
        if i % 2 == 0: #for the first and third object
            if topmost_pixel[1] > 0: # check index
              output_grid[topmost_pixel[0], topmost_pixel[1] - 1] = 1 #left
        else: #for the second object
          if topmost_pixel[1] < output_grid.shape[1] - 1:
            output_grid[topmost_pixel[0], topmost_pixel[1] + 1] = 1  #right

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
