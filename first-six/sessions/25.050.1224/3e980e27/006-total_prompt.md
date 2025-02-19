# 3e980e27 • 006 • example_3 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 1 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x832 at 0x79CABA166C80>

**output**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 1 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 2 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x832 at 0x79CABA165120>
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  size: 13x13
  objects:
    - color: 2 (red)
      positions: [(3,3), (8,7)]
      shape: single cell
    - color: 1 (blue)
      positions: [(3,4), (4,3), (4,4), (5,5)]
      shape: L-shape and single cell

output_grid:
  size: 13x13
  objects:
    - color: 2 (red)
      positions: [(3,3), (8,7)]
      shape: single cell
    - color: 1 (blue)
      positions: [(3,4), (4,3), (4,4), (5,5), (8,6), (9,6), (9,7), (10,5)]
      shape: original L and single cell and a mirrored and translated copy

```

**Natural Language Program: Description of the Transformation Rule**

1.  **Identify Objects:** In the input grid, we can identify two distinct types of objects:
    *   Red (color 2) single-cell objects.
    *   Blue (color 1) objects, which appear as a small "L" shape and a single cell.

2.  **Preservation of Red Objects:** The red single-cell objects at positions (3, 3) and (8, 7) remain unchanged in their position and color in the output grid.

3. **Copy, move and mirror of blue objects**: All blue object are copied, mirrored and moved to the bottom right,

4.  **Transformation of Blue Objects:** The blue objects undergo a transformation.
  * The existing blue objects from the input are kept at their original place.
  * The blue objects are moved to the bottom right. The amount is calculated by the position of the red point in the bottom right corner of the grid.
  * The blue object that triggered the translation (the one on the bottom right of the input grid) is mirrored along the axis that passes for the red point.

**Complete Description**
The blue shape is copied, mirrored, and translated in the grid based on the bottom-right red object. The red objects are not impacted.


```python
"""
The blue shape is copied, mirrored, and translated in the grid based on the bottom-right red object. The red objects are not impacted.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
        if (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] and
                grid[r, c] == color and (r, c) not in visited):
            visited.add((r, c))
            current_object.append((r, c))
            dfs(r + 1, c, current_object)
            dfs(r - 1, c, current_object)
            dfs(r, c + 1, current_object)
            dfs(r, c - 1, current_object)
        return current_object

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c, []))
    return objects

def translate_object(object_coords, row_translation, col_translation):
    translated_coords = []
    for r,c in object_coords:
        translated_coords.append( (r+row_translation, c+ col_translation))
    return translated_coords

def mirror_object(object_coords, red_coords):
    mirrored_coords = []
    r_ref, c_ref = red_coords
    for r,c in object_coords:
      mirrored_coords.append( (r + 2*(r_ref - r), c + 2*(c_ref - c)) )
    return mirrored_coords

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find red objects
    red_objects = find_objects(input_grid, 2)
    # Find blue objects
    blue_objects = find_objects(input_grid, 1)
    
    # Assume the translation reference is the last red object (bottom-right)
    if len(red_objects)>0:
        red_ref_row, red_ref_col = red_objects[-1][0]

        for blue_object in blue_objects:
            #Mirror
            mirrored_blue_object = mirror_object(blue_object, (red_ref_row, red_ref_col))
            #Translate
            #translated_blue_object = translate_object(blue_object, red_ref_row - blue_ref_row, red_ref_col - blue_ref_col )
            for r, c in mirrored_blue_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                  output_grid[r, c] = 1

    return output_grid.tolist()
```

**input**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 4 3 4 0 0 0 0 0
0 0 0 0 0 4 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 3 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x832 at 0x79CABA166B30>

**output**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 4 3 4 0 0 0 0 0
0 0 0 0 0 4 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 4 0 0 0 0 0 0 0 0 0 0
0 4 3 4 0 0 0 0 0 0 0 0 0
0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0 4 3 4 0 0
0 0 0 0 0 0 0 0 4 4 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x832 at 0x79CABA1659F0>
Okay, let's analyze the second example.

**YAML Summary of Observations**

```yaml
input_grid:
  size: 13x13
  objects:
    - color: 4 (yellow)
      positions: [(1,6), (2,5), (2,7), (3,5), (3,6)]
      shape: Cross-like shape
    - color: 3 (green)
      positions: [(2,6), (6,2), (9,9)]
      shape: Single cell
output_grid:
  size: 13x13
  objects:
    - color: 4 (yellow)
      positions: [(1,6), (2,5), (2,7), (3,5), (3,6), (6,1), (6,3), (7,1), (7,2), (9,8), (9, 10), (10,8), (10,9)]
      shape: Original cross shape and two new single cell.
    - color: 3 (green)
      positions: [(2,6), (6,2), (9,9)]
      shape: single cell

```

**Natural Language Program: Description of the Transformation Rule**

1.  **Identify Objects:**
    *   Yellow (color 4) objects form a cross-like shape.
    *   Green (color 3) objects are single cells.

2.  **Preservation of Green and Yellow Objects:** The original Yellow cross-like shape, and the green objects are kept.

3. **Copy and translate yellow cross:** The yellow cross shape is copied and moved.
    * The number of cells to move is calculated thanks to the position of each green point.
    * A yellow cross is moved based on each green point.

**Complete Description**
The yellow cross is duplicated and moved around based on the green points. The green object are not impacted.

```python
"""
The yellow cross is duplicated and moved around based on the green points. The green object are not impacted.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
        if (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] and
                grid[r, c] == color and (r, c) not in visited):
            visited.add((r, c))
            current_object.append((r, c))
            dfs(r + 1, c, current_object)
            dfs(r - 1, c, current_object)
            dfs(r, c + 1, current_object)
            dfs(r, c - 1, current_object)
        return current_object

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c, []))
    return objects

def translate_object(object_coords, row_translation, col_translation):
    translated_coords = []
    for r,c in object_coords:
        new_r = r + row_translation
        new_c = c + col_translation
        if 0<= new_r < 13 and 0<= new_c < 13:
             translated_coords.append((new_r, new_c))
    return translated_coords

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find green objects
    green_objects = find_objects(input_grid, 3)

    # Find yellow objects
    yellow_objects = find_objects(input_grid, 4)

    for green_object in green_objects:
        gr, gc = green_object[0] #Consider only the position

        for yellow_object in yellow_objects:
                # Calculate translation based on the FIRST yellow object as reference
                yellow_ref_row, yellow_ref_col = yellow_object[0]
                row_translation = gr - yellow_ref_row
                col_translation = gc - yellow_ref_col
                translated_yellow = translate_object(yellow_object, row_translation, col_translation)

                for r,c in translated_yellow:
                    output_grid[r,c] = 4

    return output_grid.tolist()
```

```python
"""
The transformation rule involves identifying blue and red objects, preserving red objects, and copying, mirroring, and translating the blue objects based on the position of the bottom-right red object.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
        if (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] and
                grid[r, c] == color and (r, c) not in visited):
            visited.add((r, c))
            current_object.append((r, c))
            dfs(r + 1, c, current_object)
            dfs(r - 1, c, current_object)
            dfs(r, c + 1, current_object)
            dfs(r, c - 1, current_object)
        return current_object

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c, []))
    return objects

def mirror_object(object_coords, red_coords):
    """Mirrors the object coordinates with respect to the red object coordinates."""
    mirrored_coords = []
    r_ref, c_ref = red_coords
    for r, c in object_coords:
        mirrored_coords.append((r + 2 * (r_ref - r), c + 2 * (c_ref - c)))
    return mirrored_coords

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find red objects
    red_objects = find_objects(input_grid, 2)
    # Find blue objects
    blue_objects = find_objects(input_grid, 1)

    # Assume the translation reference is the last red object (bottom-right)
    if red_objects:
        red_ref_row, red_ref_col = red_objects[-1][0]

        for blue_object in blue_objects:
            # Mirror the blue object
            mirrored_blue_object = mirror_object(blue_object, (red_ref_row, red_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_blue_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 1

    return output_grid.tolist()
```


**input**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 2 0 0
0 0 3 8 8 0 0 0 0 0 0 0 0
0 0 8 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 2 0 0 0 0 0
0 3 0 0 0 0 0 4 4 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x832 at 0x79CABA197340>

**output**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 2 4 0
0 0 3 8 8 0 0 0 0 4 4 0 0
0 0 8 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 2 0 0 0 0 0
0 3 8 8 0 0 0 4 4 0 0 0 0
0 8 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x832 at 0x79CABB63B6D0>
Okay, let's analyze the third example provided.

**YAML Summary of Observations**

```yaml
input_grid:
  size: 13x13
  objects:
    - color: 2 (red)
      positions: [(1, 10), (7, 7)]
      shape: single cell
    - color: 3 (green)
      positions: [(2, 2), (8, 1)]
      shape: single cell
    - color: 8 (azure)
      positions: [(2, 3), (2, 4), (3, 2)]
      shape: L-shape
    - color: 4 (yellow)
      positions:  [(7, 6), (8, 7), (8, 8)]
      shape: L-shape

output_grid:
  size: 13x13
  objects:
    - color: 2 (red)
      positions: [(1, 10), (7, 7)]
      shape: single cell
     - color: 3 (green)
      positions: [(2, 2), (8, 1)]
      shape: single cell
    - color: 8 (azure)
      positions: [(2, 3), (2, 4), (3, 2), (8,2), (9,1), (9,2)]
      shape: Two distinct L shapes, one original, one mirrored on X axis.
    - color: 4 (yellow)
      positions:  [(1,11), (2, 10), (2, 11), (7, 6), (8, 7), (8, 8)]
      shape: L-shape and Mirrored shape
```

**Natural Language Program: Description of the Transformation Rule**

1.  **Identify Objects:** In the input grid, there are four types of objects:
    *   Red (color 2) single-cell objects.
    *   Green (color 3) single-cell objects.
    *   Azure (color 8) L-shaped object.
    *  Yellow (color 4) L-Shaped object.

2.  **Preservation of Single-Cell Objects:**  The red and green single-cell objects remain in their original positions and colors in the output grid.

3.  **Mirror some objects** Azure and Yellow objects are mirrored according to the position of some red objects:
 * Azure Object (color 8) are mirrored based on the green objects.
 * Yellow Object (color 4) are mirrored based on the red objects.

4.  **Transformation Details:**
    *   The original azure and yellow objects are preserved.
    *   The mirrored object appears in the output grid.

**Complete Description**

The azure and yellow objects are mirrored based on the position of the green and red, respectively. The single-cell red and green objects do not change.

```python
"""
The azure and yellow objects are mirrored based on the position of the green and red, respectively. The single-cell red and green objects do not change.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
        if (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] and
                grid[r, c] == color and (r, c) not in visited):
            visited.add((r, c))
            current_object.append((r, c))
            dfs(r + 1, c, current_object)
            dfs(r - 1, c, current_object)
            dfs(r, c + 1, current_object)
            dfs(r, c - 1, current_object)
        return current_object

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c, []))
    return objects

def mirror_object(object_coords, ref_coords):
    """Mirrors the object coordinates with respect to the ref object coordinates."""
    mirrored_coords = []
    r_ref, c_ref = ref_coords
    for r, c in object_coords:
        mirrored_coords.append((r + 2 * (r_ref - r), c + 2 * (c_ref - c)))
    return mirrored_coords
def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find red objects
    red_objects = find_objects(input_grid, 2)
    # Find green objects
    green_objects = find_objects(input_grid, 3)
    # Find azure objects
    azure_objects = find_objects(input_grid, 8)
    # Find yellow objects
    yellow_objects = find_objects(input_grid, 4)
    #Mirror Yellow object
    for red_object in red_objects:
        red_ref_row, red_ref_col = red_object[0]
        for yellow_object in yellow_objects:
            # Mirror the yellow object
            mirrored_yellow_object = mirror_object(yellow_object, (red_ref_row, red_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_yellow_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 4
    #Mirror Azure Object
    for green_object in green_objects:
        green_ref_row, green_ref_col = green_object[0]
        for azure_object in azure_objects:
            # Mirror the yellow object
            mirrored_azure_object = mirror_object(azure_object, (green_ref_row, green_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_azure_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 8
    return output_grid.tolist()
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
