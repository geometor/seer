# 1-3aa6fb7a • 006 • example_2 - CODE

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
        shape: two separate 2x1 vertical lines
        positions:
          - (1,1), (2,1)  # One line
          - (4,3), (5,3)  # Another line
      - color: 0 (white)
        shape: background
        positions: fills the remaining cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two separate 2x1 vertical lines
        positions:
          - (1,1), (2,1)  # One line
          - (4,3), (5,3)  # Another line
      - color: 1 (blue)
        shape: single cells
        positions:
          - (1,2) # Next to first azure line
          - (4,4)   # Next to second azure line
      - color: 0 (white)
        shape: background
        positions: fills the remaining cells

```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** In the input grid, we have two distinct vertical lines of color 8 (azure). Each line is two cells high and one cell wide.

2.  **Observe Changes:** We see in output that the first azure shape maintained as is. And, a new blue pixel (color 1) appears immediately to the right of the top pixel of each azure line.

3. **Describe the Rule:**
    - Scan the input grid from the upper shape to the lower shape.
    - For each top pixel of an azure shape, identify their right-adjacent position, in order.
    - Add new pixel by drawing at these positions with blue(color 1).


```python
"""
The transformation rule is as follows:
1. Identify all vertical azure (color 8) lines that are 2x1 in the input grid.
2. For each identified line, place a blue (color 1) pixel to the immediate right of the top pixel of the line.
"""

import numpy as np

def find_vertical_lines(grid, color, height, width):
    """
    Find vertical lines of specified color, height, and width in the grid.
    """
    lines = []
    rows, cols = grid.shape
    for r in range(rows - height + 1):
        for c in range(cols - width + 1):
            if all(grid[r+i, c] == color for i in range(height)):
                lines.append((r, c))
    return lines

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    1. Find 2x1 vertical lines of azure color.
    2. Add one blue pixel at the upper-right of each of these lines
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find all 2x1 vertical lines of color 8 (azure)
    azure_lines = find_vertical_lines(input_grid, 8, 2, 1)

    # For each azure line, place a blue pixel (color 1) to the right of the top pixel
    for line in azure_lines:
        r, c = line
        if c + 1 < output_grid.shape[1]:  # Check bounds
            output_grid[r, c + 1] = 1

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

![Image](005-example_2_input.png)


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

![Image](005-example_2_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: scattered segments
        positions:
          - (0,4), (0,5)  # Horizontal line segment
          - (1,5) # Single pixel
          - (2,2) # Single pixel
          - (3,2), (3,3) # Horizontal line segment
          - (5,4) # Single Pixel
          - (6,3), (6,4) # Horizontal line segment
      - color: 0 (white)
        shape: background
        positions: fills the remaining cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: same as input
        positions: same as input
      - color: 1 (blue)
        shape: single cells
        positions:
          - (1,4)   # Left to the segment (0,4)
          - (2,3)   # Right to the segment (2,2)
          - (5,3)  # Left to the segment (5,4)

      - color: 0 (white)
        shape: background
        positions: fills the remaining cells

```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** In the input grid, we have color 8 (azure) pixels.

2.  **Observe Changes:** We see in the output that azure pixels maintained as is. And, a new blue pixel (color 1) can appear immediately to the left or the right of an azure pixel, only once for an azure pixel.

3. **Describe the Rule:**
    - Scan the input grid from the upper shape to the lower shape.
    - For each azure shape, identify their right-adjacent and left-adjacent position, in order.
    - If a position doesn't have any colored pixel, add a new pixel by drawing at these positions with blue(color 1).

```python
"""
The transformation rule is as follows:
1. Identify all azure (color 8) pixels in the input grid.
2. For each identified pixel, check its immediate left or right. If it is empty, then place a blue (color 1) there.
"""

import numpy as np

def find_pixels(grid, color):
    """
    Find pixels of specified color.
    """
    pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                pixels.append((r, c))
    return pixels

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    1. Find all pixels of azure color.
    2. Add one blue pixel at the left or the right of each of these pixels
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find all pixels of color 8 (azure)
    azure_pixels = find_pixels(input_grid, 8)

    # For each azure pixel, place a blue pixel (color 1) to the left or right
    for pixel in azure_pixels:
        r, c = pixel
        if c - 1 >= 0 and output_grid[r, c - 1] == 0 :  # Check left side
            output_grid[r, c - 1] = 1
            continue
        if c + 1 < output_grid.shape[1] and output_grid[r, c+1] == 0:  # Check right side and bounds
            output_grid[r, c + 1] = 1


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
