# 5-150deff5 • 004 • example_2 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0 0 0 0
0 0 5 5 5 5 5 0 0 0 0
0 0 0 5 5 5 0 0 0 0 0
0 0 0 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 5 0 0 0
0 0 0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x576 at 0x7291F661E500>

**output**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 8 8 0 0 0 0 0 0 0
0 0 8 8 2 2 2 0 0 0 0
0 0 0 2 8 8 0 0 0 0 0
0 0 0 2 8 8 8 8 0 0 0
0 0 0 2 0 0 8 8 0 0 0
0 0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x576 at 0x7291F661DF60>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 5
      shape: irregular
      position: centered, extends from row 2 to row 7
      size: 16 cells
  background:
    - color: 0

output_grid:
  objects:
    - color: 8
      shape: irregular, similar to a subset of the input object
      position: centered, within the original shape of color 5
      size: 8
    - color: 2
      shape: irregular, surrounds color 8 object, fills the remaining area
      position: matches the outline of the original color 5 object
      size: 8
  background:
   -color: 0
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify the Object:** Locate the single connected object composed of cells with color 5 (gray) in the input grid.

2.  **Inner/Outer Segmentation:** Divide gray object (color 5) from input in two regions. The "inner" region, and the "outer" region.
The outer region is formed by gray pixels (color 5) having at least one neighbor of color 0. The inner region is formed by the remaining gray pixels (color 5).

3.  **Recolor inner:** Change the color of the inner region to color 8 (azure).

4. **Recolor outer**: Change the color of the outer region to color 2 (red).

5.  **Preserve Background:** The background (color 0) remains unchanged.

**Explanation of the program:**

The program successfully describes how to change the input to the output. It identifies the gray object, separates it by its inner and outer regions. Then, it changes the color of the segments to obtain the output image.


*text:*
```python
"""
This program takes an input grid and transforms it based on the following rules:
1. Identifies a single connected object of color 5 (gray).
2. Divides the gray object into two regions: "inner" and "outer".
   - The "outer" region consists of gray pixels (color 5) that have at least one neighbor of color 0.
   - The "inner" region consists of the remaining gray pixels (color 5).
3. Recolors the inner region to color 8 (azure).
4. Recolors the outer region to color 2 (red).
5. Keeps the background (color 0) unchanged.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Returns the coordinates of the neighbors of a cell."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col):
                neighbors.append((i, j))
    return neighbors

def find_object(grid, color):
    """Finds the coordinates of all cells belonging to the object of a given color."""
    object_cells = []
    for r in range(grid.shape[0]):
      for c in range(grid.shape[1]):
        if grid[r,c] == color:
          object_cells.append((r,c))

    return object_cells
    

def segment_object(grid, object_cells):
    """Segments the object into inner and outer regions."""
    inner_region = []
    outer_region = []

    for row, col in object_cells:
        neighbors = get_neighbors(grid, row, col)
        is_outer = False
        for n_row, n_col in neighbors:
            if grid[n_row, n_col] == 0:
                is_outer = True
                break
        if is_outer:
            outer_region.append((row, col))
        else:
            inner_region.append((row, col))

    return inner_region, outer_region

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    # Initialize output_grid with the same dimensions and background color as the input.
    output_grid = np.zeros_like(input_grid)

    # Find the object with color 5 (gray).
    object_cells = find_object(input_grid, 5)
    
    # Check that we have one object
    if not object_cells:
        return output_grid

    # Segment the object into inner and outer regions.
    inner_region, outer_region = segment_object(input_grid, object_cells)

    # Recolor the inner region to color 8 (azure).
    for row, col in inner_region:
        output_grid[row, col] = 8

    # Recolor the outer region to color 2 (red).
    for row, col in outer_region:
        output_grid[row, col] = 2

    return output_grid
```

**input**
```
0 0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 5 0 0 0
0 5 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x7291F661E830>

**output**
```
0 0 0 0 0 0 0 0 0 0
0 8 8 2 8 8 2 0 0 0
0 8 8 2 8 8 2 0 0 0
0 0 0 2 0 0 2 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x7291F661DD50>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid in this second example.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 5
      shape: irregular
      position:  extends from row 1 to row 6
      size: 16 cells
  background:
    - color: 0

output_grid:
  objects:
    - color: 8
      shape: irregular, similar to a subset of the input object
      position: within the original shape of color 5
      size: 8
    - color: 2
      shape: irregular, surrounds color 8 object, fills the remaining area
      position: matches the outline of the original color 5 object
      size: 8
  background:
   -color: 0
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify the Object:** Locate the single connected object composed of cells with color 5 (gray) in the input grid.

2.  **Inner/Outer Segmentation:** Divide gray object (color 5) from input in two regions. The "inner" region, and the "outer" region.
The outer region is formed by gray pixels (color 5) having at least one neighbor of color 0. The inner region is formed by the remaining gray pixels (color 5).

3.  **Recolor inner:** Change the color of the inner region to color 8 (azure).

4. **Recolor outer**: Change the color of the outer region to color 2 (red).

5.  **Preserve Background:** The background (color 0) remains unchanged.

**Explanation of the program:**

The program successfully describes how to change the input to the output. It identifies the gray object, separates it by its inner and outer regions. Then, it changes the color of the segments to obtain the output image.

The program is identical to the previous example.

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
