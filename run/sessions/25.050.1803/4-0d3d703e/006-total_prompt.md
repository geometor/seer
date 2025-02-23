# 4-0d3d703e • 006 • example_3 - CODE

---

**input**
```
3 1 2
3 1 2
3 1 2
```

![Image](000-example_1_input.png)


**output**
```
4 5 6
4 5 6
4 5 6
```

![Image](000-example_1_output.png)

**Natural Language Program:**

The transformation rule is a simple color replacement. For each cell in the input grid, perform the following color mapping: change color 3 (green) to color 4 (yellow), color 1 (blue) to color 5 (gray), and color 2 (red) to color 6 (magenta).  In essence, each distinct color present in the input grid is replaced by a new, distinct color in the output grid.
```python
"""
The transformation rule is a simple color replacement. For each cell in the input grid, perform the following color mapping:
change color 3 (green) to color 4 (yellow), color 1 (blue) to color 5 (gray), and color 2 (red) to color 6 (magenta).
In essence, each distinct color present in the input grid is replaced by a new, distinct color in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    3 (green) -> 4 (yellow)
    1 (blue) -> 5 (gray)
    2 (red) -> 6 (magenta)
    """
    # Initialize the output grid as a copy of the input grid to avoid modifying the original.
    output_grid = np.copy(input_grid)

    # Apply the color mapping.  Iterate through each cell and change the color according to the defined rule.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 1:
                output_grid[i, j] = 5
            elif output_grid[i, j] == 2:
                output_grid[i, j] = 6

    return output_grid
```


**input**
```
2 3 8
2 3 8
2 3 8
```

![Image](002-example_2_input.png)


**output**
```
6 4 9
6 4 9
6 4 9
```

![Image](002-example_2_output.png)

**Natural Language Program:**

The transformation rule is a color-to-color replacement applied to each cell in the input grid.  Specifically:
- Color 2 (red) is transformed into color 6 (magenta).
- Color 3 (green) is transformed into color 4 (yellow).
- Color 8 (azure) is transformed into color 9 (maroon).
All instances of these input colors are replaced by their corresponding output colors to produce the output grid.

```python
"""
The transformation rule is a color-to-color replacement applied to each cell in the input grid.
Specifically:
- Color 2 (red) is transformed into color 6 (magenta).
- Color 3 (green) is transformed into color 4 (yellow).
- Color 8 (azure) is transformed into color 9 (maroon).
All instances of these input colors are replaced by their corresponding output colors to produce the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    2 (red) -> 6 (magenta)
    3 (green) -> 4 (yellow)
    8 (azure) -> 9 (maroon)
    """
    output_grid = np.copy(input_grid)

    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9

    return output_grid
```
**input**
```
7 0 0 0
0 7 0 0
0 0 7 0
0 0 0 7
```

![Image](001-test_input.png)

**Natural Language Program:**

The transformation rule involves a color substitution based on the diagonal position of an orange (color 7) pixel relative to the main diagonal (top-left to bottom-right). If the orange pixel is on the main diagonal, it's changed to gray (color 5). If it isn't on the main diagonal, it is changed to black/white (color 0). Every other color is turned to white (0).

```python
"""
The transformation rule involves a color substitution based on the diagonal position of an orange (color 7) pixel relative to the main diagonal (top-left to bottom-right). If the orange pixel is on the main diagonal, it's changed to gray (color 5). If it isn't on the main diagonal, it is changed to black/white (color 0). Every other color is turned to white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    output_grid[:] = 0 # initialize to color 0 (white)

    # Iterate through the grid to find and process orange (color 7) pixels.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if input_grid[i, j] == 7:
                if i == j:  # Check if the pixel is on the main diagonal.
                    output_grid[i, j] = 5  # Change to gray (color 5).
                else:
                    output_grid[i,j] = 0

    return output_grid
```


**input**
```
5 8 6
5 8 6
5 8 6
```

![Image](004-example_3_input.png)


**output**
```
1 9 2
1 9 2
1 9 2
```

![Image](004-example_3_output.png)

**Natural Language Program:**

The transformation rule is a color-to-color replacement applied to each cell in the input grid. Specifically, color 5 (gray) is replaced with color 1 (blue), color 8 (azure) is replaced with color 9 (maroon), and color 6 (magenta) is replaced with color 2 (red). Each instance of these input colors is substituted with their corresponding output colors to generate the output grid.

```python
"""
The transformation rule is a color-to-color replacement applied to each cell in the input grid.
Specifically, color 5 (gray) is replaced with color 1 (blue), color 8 (azure) is replaced with color 9 (maroon), and color 6 (magenta) is replaced with color 2 (red).
Each instance of these input colors is substituted with their corresponding output colors to generate the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    5 (gray) -> 1 (blue)
    8 (azure) -> 9 (maroon)
    6 (magenta) -> 2 (red)
    """
    output_grid = np.copy(input_grid)

    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 5:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 2

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
