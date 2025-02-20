# 2-0ca9ddb6 • 006 • example_3 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
  background_color: 0 (white)

output_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
    - color: 4 (yellow)
      positions: [(2, 1), (2, 3), (4, 1), (4, 3)]
      shape: four single cells forming a pattern around red
    - color: 7 (orange)
      positions: [(5, 5), (6, 5), (7, 5), (6, 7)]
      shape: four single cells in L-shape around the blue object
  background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Single-Cell Objects:** Locate all objects in the input grid that consist of a single cell. In this case, we have a red cell at (3, 2) and a blue cell at (6, 6).

2.  **Yellow Surround:** For the red object, place yellow (4) cells above, below, and two cells placed horizontally to form a mirrored L-shape around the red cell on the left. The pattern looks like two vertical lines, placed one row above and other below the identified object.

3. **Orange Surround:** For the blue cell create an L-shape using orange object (color 7) to surround it on the left, using 3 orange cells at the left of the blue object and one cell at the bottom-right, at a distance of one cell.

4.  **Preserve Original Objects:** The original red and blue cells remain in their original positions in the output grid.

**Natural Language Program**
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.

```python
"""
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell two positions to its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all single-cell objects
    objects = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                # Check if it's a single-cell object (not part of a larger object)
                is_single = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) or not (0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]):
                            continue
                        if grid[y + dy, x + dx] == grid[y, x]:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    objects.append((y, x, grid[y, x]))
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)
    
    # Process each single-cell object
    for y, x, color in single_cell_objects:
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4
            if x > 0:
                output_grid[y+1,x-1] = 4
            
        elif color == 1:  # Blue
            if x > 0:
              for i in range(3):
                if 0 <= y - 1 + i < output_grid.shape[0] :
                  output_grid[y - 1 + i, x - 1] = 7  # Left
            if y < output_grid.shape[0] - 1 and x < output_grid.shape[1] -1 :
              output_grid[y + 1, x + 1] = 7  # Bottom-right
    
    return output_grid
```

**input**
```
0 0 0 8 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0 0
0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](002-example_2_input.png)


**output**
```
0 0 0 8 0 0 0 0 0
0 0 0 0 0 4 0 4 0
0 0 7 0 0 0 2 0 0
0 7 1 7 0 4 0 4 0
0 0 7 0 0 0 0 0 0
0 0 0 0 0 0 7 0 0
4 0 4 0 0 7 1 7 0
0 2 0 0 0 0 7 0 0
4 0 4 0 0 0 0 0 0
```

![Image](002-example_2_output.png)

Okay, let's analyze the second example.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 8 (azure)
      position: (0, 3)
      shape: single cell
    - color: 2 (red)
      position: (2, 6)
      shape: single cell
    - color: 1 (blue)
      position: (3, 2)
      shape: single cell
    - color: 1 (blue)
      position: (6, 6)
      shape: single cell
    - color: 2 (red)
      position: (7,1)
      shape: single cell
  background_color: 0 (white)

output_grid:
  size: 9x9
  objects:
    - color: 8 (azure)
      position: (0, 3)
      shape: single cell
    - color: 2 (red)
      positions: (2, 6), (7,1)
      shape: single cell
    - color: 1 (blue)
      positions: (3, 2), (6,6)
      shape: single cell
    - color: 4 (yellow)
      positions: [(1, 5), (1, 7), (3, 5), (3, 7), (6,0), (6,2), (8,0), (8,2)]
      shape: single cells forming a pattern
    - color: 7 (orange)
      positions: [(2,1),(2,2),(4,2),(3,1),(3,3),(5,6), (6,5), (7, 6), (6, 7)]
      shape: single cells forming a pattern
  background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Single-Cell Objects:** Locate all objects consisting of a single cell in the input, disregarding those with color 8. This includes red cells at (2, 6), (7,1), and blue cells at (3, 2), (6,6).

2.  **Yellow Surround:** For each red object, place yellow (4) cells above, below, and two cells placed horizontally to form a mirrored L-shape around the red cell on the left. The pattern looks like two vertical lines, placed one row above and other below the identified object.

3. **Orange Surround:** For each blue cell create an L-shape using orange object (color 7) to surround it on the left, using 3 orange cells at the left of the blue object and one cell at the bottom-right, at a distance of one cell.

4.  **Preserve Original Objects:** The original single cell objects with colors different to 0 remain in their original positions in the output grid.

**Natural Language Program**
1. Find every object of size 1 in the input, except those of color 8.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1, except those of color 8.

This is essentially the same rule as in the first example, with the additional condition of ignoring single-cell objects of color 8. The Python code developed for the first example can be reused, with just a minor addition, the condition to ignore single cell of color 8.

```python
"""
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell two positions to its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all single-cell objects
    objects = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                # Check if it's a single-cell object (not part of a larger object)
                is_single = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) or not (0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]):
                            continue
                        if grid[y + dy, x + dx] == grid[y, x]:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    objects.append((y, x, grid[y, x]))
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)
    
    # Process each single-cell object
    for y, x, color in single_cell_objects:
        if color == 8:
          continue
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4
            if x > 0:
                output_grid[y+1,x-1] = 4
            
        elif color == 1:  # Blue
            if x > 0:
              for i in range(3):
                if 0 <= y - 1 + i < output_grid.shape[0] :
                  output_grid[y - 1 + i, x - 1] = 7  # Left
            if y < output_grid.shape[0] - 1 and x < output_grid.shape[1] -1 :
              output_grid[y + 1, x + 1] = 7  # Bottom-right
    
    return output_grid
```

```python
"""
1. Find every object of size 1 in the input, except those of color 8.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
     - Place a yellow cell diagonally up and to the left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1, except those of color 8.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all single-cell objects
    objects = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                # Check if it's a single-cell object (not part of a larger object)
                is_single = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) or not (0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]):
                            continue
                        if grid[y + dy, x + dx] == grid[y, x]:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    objects.append((y, x, grid[y, x]))
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)
    
    # Process each single-cell object
    for y, x, color in single_cell_objects:
        if color == 8:
          continue
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4 # Up and to the left
            if x > 0:
                output_grid[y,x-1] = 4 # to the left
            if x > 0 and y < output_grid.shape[0]-1:   
                output_grid[y+1,x-1] = 4
            
        elif color == 1:  # Blue
            if x > 0:
              for i in range(3):
                if 0 <= y - 1 + i < output_grid.shape[0] :
                  output_grid[y - 1 + i, x - 1] = 7  # Left
            if y < output_grid.shape[0] - 1 and x < output_grid.shape[1] -1 :
              output_grid[y + 1, x + 1] = 7  # Bottom-right
    
    return output_grid
```


**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](004-example_3_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 7 0 0 0 0 0
0 0 7 1 7 0 0 0 0
0 0 0 7 0 0 0 0 0
```

![Image](004-example_3_output.png)

Okay, let's analyze the third example.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (2, 2)
      shape: single cell
    - color: 1 (blue)
      position: (7, 3)
      shape: single cell
    - color: 6 (magenta)
      position: (5,6)
      shape: single cell
  background_color: 0 (white)

output_grid:
  size: 9x9
  objects:
    - color: 2 (red)
      position: (2, 2)
      shape: single cell
    - color: 1 (blue)
      position: (7, 3)
      shape: single cell
    - color: 6 (magenta)
      position: (5,6)
      shape: single cell
    - color: 4 (yellow)
      positions: [(1, 1), (1, 3), (3, 1), (3, 3)]
      shape: single cells forming a pattern
    - color: 7 (orange)
      positions: [(6, 2), (7, 2), (8, 2), (7, 4)]
      shape: single cells forming a pattern
  background_color: 0 (white)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Single-Cell Objects:** Locate all objects consisting of a single cell. This includes a red cell at (2, 2), a blue cell at (7, 3) and a magenta cell at (5,6).

2.  **Yellow Surround:** For the red object, place yellow (4) cells above, below, and two cells placed horizontally to form a mirrored L-shape around the red cell on the left. The pattern looks like two vertical lines, placed one row above and other below the identified object.

3.  **Orange Surround:** For the blue cell, create an L-shape using orange object (color 7) to surround it on the left, using 3 orange cells at the left of the blue object and one cell at the bottom-right, at a distance of one cell.

4. **Preserve all single cells:** The original single cells remain in their original positions in the output grid. The magenta cell is kept.

**Natural Language Program**

1.  Find every object of size 1 in the input.
2.  For each of those objects:
    -   if the object is red:
        -   Place a yellow cell above it.
        -   Place a yellow cell below it.
        - Place a yellow cell at its left.
        - Place a yellow cell diagonally up and to the left
    -   if the object is blue:
        -   Place 3 orange cells to form a vertical line at its left.
        -   Place one orange cell at the bottom-right of the blue cell, with distance 1.
3.  Maintain original objects of size 1.

This transformation rule is consistent with the previous examples, confirming that single objects are sorrounded based on the rules for the red and blue color. Additionally all the single objects are kept, including the magenta cell.
The python implementation does not require changes.

```python
"""
1. Find every object of size 1 in the input, except those of color 8.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell at its left.
     - Place a yellow cell diagonally up and to the left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1, except those of color 8.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all single-cell objects
    objects = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                # Check if it's a single-cell object (not part of a larger object)
                is_single = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) or not (0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]):
                            continue
                        if grid[y + dy, x + dx] == grid[y, x]:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    objects.append((y, x, grid[y, x]))
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)
    
    # Process each single-cell object
    for y, x, color in single_cell_objects:
        if color == 8:
          continue
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4 # Up and to the left
            if x > 0:
                output_grid[y,x-1] = 4 # to the left
            if x > 0 and y < output_grid.shape[0]-1:   
                output_grid[y+1,x-1] = 4
            
        elif color == 1:  # Blue
            if x > 0:
              for i in range(3):
                if 0 <= y - 1 + i < output_grid.shape[0] :
                  output_grid[y - 1 + i, x - 1] = 7  # Left
            if y < output_grid.shape[0] - 1 and x < output_grid.shape[1] -1 :
              output_grid[y + 1, x + 1] = 7  # Bottom-right
    
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
