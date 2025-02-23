# 1-3aa6fb7a • 008 • example_2 - CODE

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

Okay, let's analyze the provided input and output grids to understand the transformation.

Here's a breakdown of my observations and the deduced transformation rule:


```yaml
observations:
  - grid_size: 7x7
  - input_colors:
    - 0: white
    - 8: azure
  - output_colors:
    - 0: white
    - 1: blue
    - 8: azure
  - object_types:
    - azure_shapes: Two separate L-shaped objects, one in the top-left and another in the bottom-right.
  - changes:
      - One azure pixel in each of the L shapes becomes blue.
      - The azure to blue change is always the pixel that is "inside" the "L" shape or "adjacent to the vertical and horizontal lines of the L"
```


**Natural Language Program:**

1.  **Identify Objects:** Locate all connected azure (8) shapes in the input grid. In this case identify "L" shaped azure objects.
2.  **Locate Inner Pixel**: Find, in each L shape, the azure pixel where a vertical and horizontal azure pixel neighbor it.
3.  **Change color**: Change the color of identified pixel to blue (1).
4. **Preserve other pixels:** All other pixels in the input grid retain the same color.

In summary, the transformation identifies "L"-shaped azure colored objects, and changes
the "inside" pixel from azure to blue while all other pixels remain the same.

```python
"""
Identify "L"-shaped azure colored objects, and changes the "inside" pixel from azure to blue while all other pixels remain the same.
"""

import numpy as np

def find_l_shapes(grid, color):
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                # Check for L shape (2x2 block with one missing corner)
                if r + 1 < rows and c + 1 < cols:
                    if grid[r+1, c] == color and grid[r, c+1] == color:
                         l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Define the color of the L shapes and the target color
    azure = 8
    blue = 1

    # Find the coordinates of pixels that are part of L-shapes
    l_shape_coords = find_l_shapes(input_grid, azure)
    
    # Identify and change the inside pixel
    for r,c in l_shape_coords:
        output_grid[r+1,c-1] = blue
        output_grid[r-1,c+1] = blue

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

![Image](007-example_2_input.png)


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

![Image](007-example_2_output.png)

Okay, let's analyze the second example pair.


```yaml
observations:
  - grid_size: 7x7
  - input_colors:
    - 0: white
    - 8: azure
  - output_colors:
    - 0: white
    - 1: blue
    - 8: azure
  - object_types:
    - azure_shapes: Three separate L-shaped objects, one in the top-right, one in the middle-left, and another in the bottom-right.
  - changes:
      - One azure pixel in each of the L shapes becomes blue.
      - The azure to blue change is always the pixel that is "inside" the "L" shape or "adjacent to the vertical and horizontal lines of the L"
```


**Natural Language Program:**

The transformation rule appears to be consistent with the first example.

1.  **Identify Objects:** Locate all connected azure (8) shapes in the input grid. Specifically, identify "L"-shaped azure objects (a 2x2 block of azure pixels with any single pixel removed).
2.  **Locate Inner Pixel**: Within each identified "L" shape, find the single azure pixel, that if removed would still leave the other two azure pixels adjacent.
3.  **Change color**: Change the color of the identified "inner" pixel to blue (1).
4.  **Preserve other pixels:** All other pixels in the input grid retain their original colors.

The core concept remains: find "L"-shaped azure structures and change the color of a specific azure pixel within each "L" to blue.


```python
"""
Identify "L"-shaped azure colored objects, and changes the "inside" pixel from azure to blue while all other pixels remain the same.
"""

import numpy as np

def is_l_shape(grid, r, c, color):
    """Checks if the cell at (r, c) is part of an L-shape of the given color."""
    if grid[r, c] != color:
        return False

    rows, cols = grid.shape
    count = 0
    neighbors = []

    # Check adjacent cells
    if r > 0 and grid[r-1, c] == color:
        count += 1
        neighbors.append((r - 1, c))
    if r < rows - 1 and grid[r+1, c] == color:
        count += 1
        neighbors.append((r + 1, c))
    if c > 0 and grid[r, c-1] == color:
        count += 1
        neighbors.append((r, c - 1))
    if c < cols - 1 and grid[r, c+1] == color:
        count += 1
        neighbors.append((r, c + 1))

    # Check if it forms an L-shape (exactly two neighbors that are either both horizontal or both vertical)
    if count == 2:
        if neighbors[0][0] == neighbors[1][0] or neighbors[0][1] == neighbors[1][1]:  # Check rows or cols
            return True

    return False
    
def find_l_shapes(grid, color):
    """Finds all pixels that are part of L-shapes of a given color."""
    l_shapes = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if is_l_shape(grid, r, c, color):
               l_shapes.append((r,c))
    return l_shapes

def transform(input_grid):
    """Transforms the input grid according to the L-shape rule."""
    output_grid = np.copy(input_grid)
    azure = 8
    blue = 1

    l_shape_coords = find_l_shapes(input_grid, azure)
    
    
    rows, cols = input_grid.shape

    for r, c in l_shape_coords:
       # Check adjacent cells for the 'inside' pixel to turn blue
        if r > 0 and r+1 < rows and input_grid[r-1,c] == azure and input_grid[r+1,c] == azure:
             output_grid[r,c] = blue
        elif c > 0 and c+1 < cols and input_grid[r,c-1] == azure and input_grid[r,c+1] == azure:
             output_grid[r,c] = blue        

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
