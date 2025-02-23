# 5-150deff5 • 006 • example_2 - CODE

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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_objects:
  - object_1:
      color: 5 (gray)
      shape: irregular, but roughly rectangular sections connected diagonally and orthogonally
      position: centered vertically and horizontally, extends across multiple rows and columns
      size: spans rows 2-7 and columns 3-8, varies in width and height
output_objects:
  - object_1:
      color: 8 (azure)
      shape: maintains a similar shape to the gray object but with some color changes
      position: occupies the same grid cells as the gray object in the input
      size: matches input size but the color 2 sections are carved out of the previous shape.
  - object_2:
      color: 2 (red)
      shape: fills the spaces within the largest connected sections of the azure object
      position: embedded within the azure object, occupying spaces previously held by gray (5)
      size: varies, conforming to the internal spaces of the azure object

```

**Natural Language Description of the Transformation Rule**

1.  **Identify the Gray Object:** In the input grid, locate the contiguous gray (color 5) object. This object is the primary focus of the transformation.

2.  **Change all Gray to Azure:** For all locations where the original object (gray) was, now all will be azure (color 8).

3.  **Change central-connected pixels to Red:** Inside of the gray object, now azure, there are some locations where a pixel has four neighbors (up, down, left, and right). If that is the case, and it creates a connected component inside the azure shape, change it to red (color 2).

**Step-by-step explanation:**
* We have a grey (5) shape.
* We change grey to azure (8)
* Inside, there is a new red (2) shape formed by the following rule.
* A pixel becomes red if it has four azure neighbors, and with other red pixels, forms a connected component.


```python
"""
1. **Identify the Gray Object:** In the input grid, locate the contiguous gray (color 5) object. This object is the primary focus of the transformation.
2. **Change all Gray to Azure:** For all locations where the original object (gray) was, now all will be azure (color 8).
3. **Change central-connected pixels to Red:** Inside of the gray object, now azure, there are some locations where a pixel has four neighbors (up, down, left, and right). If that is the case, and it creates a connected component inside the azure shape, change it to red (color 2).
"""

import numpy as np

def get_neighbors(grid, r, c):
    """ Return 4 neighbors of the cell in grid"""

    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Change all gray (5) to azure (8)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                output_grid[r, c] = 8

    # Change central-connected pixels to red (2)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 8:
                neighbors = get_neighbors(output_grid, r, c)
                neighbor_colors = [output_grid[nr, nc] for nr, nc in neighbors]
                if all(color == 8 for color in neighbor_colors) and len(neighbors) == 4:
                    output_grid[r,c] = 2

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

![Image](005-example_2_input.png)


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

![Image](005-example_2_output.png)

Okay, let's analyze the transformation between the input and output grids for the second example.

**YAML Description of Observations**

```yaml
input_objects:
  - object_1:
      color: 5 (gray)
      shape: irregular, with disconnected parts and varying widths
      position: spans rows 2-7 and columns 1-7, not uniformly distributed
      size: scattered across multiple rows and columns with gaps
output_objects:
  - object_1:
      color: 8 (azure)
      shape: mirrors the shape of the input gray object, replacing most of the gray areas
      position: occupies the same grid cells as the initial gray object
      size: matches the input gray object's size in respective locations
  - object_2:
      color: 2 (red)
      shape: fills in spaces within the azure object where gray was previously connected on four sides
      position: embedded within the azure object, occupying spaces originally held by gray
      size: forms based on connectivity within the azure object

```

**Natural Language Description of the Transformation Rule**

1.  **Identify the Gray Object:** Locate the contiguous gray (color 5) areas in the input grid. This forms the basis of the transformation.

2.  **Change Gray to Azure:** All instances of gray (color 5) are changed to azure (color 8).

3. **Change central-connected pixels to Red:** Inside the azure areas, if a pixel originally colored gray (5) had four neighbors that were also gray (up, down, left, right, orthogonal), it is changed to red (color 2). The resulting red pixels are adjacent to one another and form a connected object (component).

**Step-by-step explanation:**

*   We start with a scattered gray (5) object.
*   We change the gray color to azure (8) everywhere there was gray before.
*   Inside the new azure object, a red (2) object is formed by checking if it has four immediate neighbors, forming a connected component, changed to red.

```python
"""
1.  **Identify the Gray Object:** Locate the contiguous gray (color 5) areas in the input grid. This forms the basis of the transformation.
2.  **Change Gray to Azure:** All instances of gray (color 5) are changed to azure (color 8).
3. **Change central-connected pixels to Red:** Inside the azure areas, if a pixel originally colored gray (5) had four neighbors that were also gray (up, down, left, right, orthogonal), it is changed to red (color 2). The resulting red pixels are adjacent to one another.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """ Return 4 neighbors of the cell in grid"""

    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Change all gray (5) to azure (8)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                output_grid[r, c] = 8

    # Create a temporary grid to track the original positions of gray pixels
    temp_grid = np.copy(input_grid)

    # Change central-connected pixels to red (2)
    for r in range(rows):
        for c in range(cols):
            if temp_grid[r, c] == 5:
                neighbors = get_neighbors(temp_grid, r, c)
                # Ensure that we only consider neighbors within the bounds of the grid
                valid_neighbors = [(nr, nc) for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols]
                neighbor_colors = [temp_grid[nr, nc] for nr, nc in valid_neighbors]
                if all(color == 5 for color in neighbor_colors) and len(valid_neighbors) == 4:
                    output_grid[r, c] = 2
    return output_grid
```
The core logic remains identical between both examples. The description and the code are generalized to apply to various configurations of the gray shape. The important modification in this version is to use the `temp_grid`, which corresponds to input grid, for the calculation of four neighbors of the same value, to determine where the red pixels should be in the final output.

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
