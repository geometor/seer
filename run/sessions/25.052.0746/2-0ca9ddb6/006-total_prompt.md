# 2-0ca9ddb6 • 006 • example_2 - CODE

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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

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
    - color: 0 (white)
      position: all other cells
      shape: background

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
      position: (2, 1), (2, 3), (4, 1), (4, 3)
      shape: single cells forming a plus shape around the red cell, but not directly touching
    - color: 7 (orange)
      position: (5,6), (6,5), (6,7), (7,6)
      shape: single cells forming a plus shape, around the blue cell, but not directly touching
    - color: 0 (white)
      position: all other cells
      shape: background
```

**Natural Language Description of the Transformation Rule**

1.  **Identify Singular Color Cells:** Locate all the cells with colors, each being the unique member of that color in the input grid. The example colors provided are Red (2) at (3,2) and Blue(1) at (6,6).

2.  **Create Plus Shapes:** For each identified single-color cell:
    *   Generate a "plus" shape centered around, but not touching the original cell with a new color. The shapes and colors around the red and blue cells are the same, and are at a one cell distance.
    *   For the red cell (color 2), place yellow (color 4) cells in a plus shape around the center. The arms of each "plus" extend one cell away from the original cell.
    *    For the blue cell (color 1), place orange(color 7) cells in a plus shape around the center. The arms of each "plus" extend one cell away from the original cell.

3. **Background:** All other cells remain unchanged (color 0).

In summary, the transformation identifies single-color cells, then constructs "plus-shaped" patterns of a specific different color around them, using those original color cells as the center of each plus (but not included in the plus).

```python
"""
1.  **Identify Singular Color Cells:** Locate all the cells with colors, each being the unique member of that color in the input grid. The example colors provided are Red (2) at (3,2) and Blue(1) at (6,6).

2.  **Create Plus Shapes:** For each identified single-color cell:
    *   Generate a "plus" shape centered around, but not touching the original cell with a new color. The shapes and colors around the red and blue cells are the same, and are at a one cell distance.
    *   For the red cell (color 2), place yellow (color 4) cells in a plus shape around the center. The arms of each "plus" extend one cell away from the original cell.
    *    For the blue cell (color 1), place orange(color 7) cells in a plus shape around the center. The arms of each "plus" extend one cell away from the original cell.

3. **Background:** All other cells remain unchanged (color 0).
"""

import numpy as np

def find_unique_color_cells(grid):
    # Count occurrences of each color
    color_counts = np.bincount(grid.flatten(), minlength=10)
    
    # Find colors that appear only once
    unique_colors = np.where(color_counts == 1)[0]
    
    # Find the coordinates of these unique colors
    unique_cells = []
    for color in unique_colors:
        coords = np.where(grid == color)
        unique_cells.append((color, (coords[0][0], coords[1][0])))
    
    return unique_cells

def create_plus_shape(grid, center, color):
    # Define the offsets for the plus shape (up, down, left, right)
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Get the dimensions of the grid
    rows, cols = grid.shape
    
    # Place the new color around the center
    for offset in offsets:
        new_row = center[0] + offset[0]
        new_col = center[1] + offset[1]
        
        # Check if the new coordinates are within the grid bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            grid[new_row, new_col] = color
    
    return grid

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find unique color cells
    unique_cells = find_unique_color_cells(input_grid)

    # Create plus shapes around each unique cell
    for color, center in unique_cells:
        if color == 2:  # Red cell
          output_grid = create_plus_shape(output_grid, center, 4)  # Yellow plus
        elif color == 1:  # Blue cell
            output_grid = create_plus_shape(output_grid, center, 7)    # Orange Plus

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

![Image](005-example_2_input.png)


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

![Image](005-example_2_output.png)

Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 8 (azure)
      position: (0, 3)
      shape: single cell
    - color: 2 (red)
      position: (2, 6), (7,1)
      shape: single cell
    - color: 1 (blue)
      position: (3, 2), (6, 6)
      shape: single cell
    - color: 0 (white)
      position: all other cells
      shape: background

output_grid:
  size: 9x9
  objects:
    - color: 8 (azure)
      position: (0, 3)
      shape: single cell
    - color: 2 (red)
      position: (2, 6), (7,1)
      shape: single cell
    - color: 1 (blue)
      position: (3, 2), (6, 6)
      shape: single cell
    - color: 4 (yellow)
      position: (1, 5), (1, 7), (3, 5), (3, 7), (7,0), (7,2), (9,0), (9,2)
      shape: single cells forming a plus shape around red cells, but not directly touching them.
    - color: 7 (orange)
      position: (2,1), (2,3), (3,0), (3,4), (4,3), (5,6), (6,5), (6,7), (8,6)
      shape: single cells forming a plus shape around blue cells, but not directly touching them
    - color: 0 (white)
      position: all other cells
      shape: background
```

**Natural Language Description of the Transformation Rule**

1.  **Identify Target Color Cells:** Locate cells with colors blue (1) and red (2).

2.  **Create Plus Shapes:**
    *   For each identified red cell (color 2), generate a "plus" shape centered around, but *not* touching, the original cell using yellow (color 4).  The "arms" of the plus extend one cell away from the red cell.
    *   For each identified blue cell (color 1), generate a "plus" shape centered around, but *not* touching, the original cell using orange (color 7). The "arms" of the plus extend one cell away from the blue cell.

3.  **Preserve Other Cells:** Any cell that is not part of the generated "plus" shapes retains its original color (including azure (8) in this case and 0, the background).

In summary, the transformation identifies blue and red cells, then constructs "plus-shaped" patterns of specific colors around them. Azure cells are considered as the background and are not modified.

```python
"""
1.  **Identify Target Color Cells:** Locate cells with colors blue (1) and red (2).

2.  **Create Plus Shapes:**
    *   For each identified red cell (color 2), generate a "plus" shape centered around, but *not* touching, the original cell using yellow (color 4).  The "arms" of the plus extend one cell away from the red cell.
    *   For each identified blue cell (color 1), generate a "plus" shape centered around, but *not* touching, the original cell using orange (color 7). The "arms" of the plus extend one cell away from the blue cell.

3.  **Preserve Other Cells:** Any cell that is not part of the generated "plus" shapes retains its original color (including azure (8) in this case and 0, the background).
"""

import numpy as np

def create_plus_shape(grid, center, color):
    """Creates a plus shape around a center cell with a specified color."""
    rows, cols = grid.shape
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in offsets:
        r, c = center[0] + dr, center[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            grid[r, c] = color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:  # Red cell
                output_grid = create_plus_shape(output_grid, (r, c), 4)  # Yellow plus
            elif input_grid[r, c] == 1:  # Blue cell
                output_grid = create_plus_shape(output_grid, (r, c), 7)  # Orange plus

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
