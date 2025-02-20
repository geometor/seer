# 4-0d3d703e • 008 • example_4 - CODE

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

The transformation rule is a direct color substitution.  Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 3 (green) is transformed to color 4 (yellow).
- Color 1 (blue) is transformed to color 5 (gray).
- Color 2 (red) is transformed to color 6 (magenta).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
```python
"""
The transformation rule is a direct color substitution. Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 3 (green) is transformed to color 4 (yellow).
- Color 1 (blue) is transformed to color 5 (gray).
- Color 2 (red) is transformed to color 6 (magenta).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing colors based on a predefined mapping.
    
    Args:
        input_grid (numpy.ndarray): The input grid with integer color values.
    
    Returns:
        numpy.ndarray: The transformed grid with updated color values.
    """
    # Initialize the output grid as a copy of the input grid to preserve dimensions.
    output_grid = np.copy(input_grid)
    
    # Define the color mapping.
    color_map = {
        3: 4,  # Green to Yellow
        1: 5,  # Blue to Gray
        2: 6   # Red to Magenta
    }
    
    # Iterate through the color map and replace colors in the output grid.
    for old_color, new_color in color_map.items():
        output_grid[input_grid == old_color] = new_color
        
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

The transformation rule is a direct color substitution, where each color in the input grid is replaced by a new color according to a specific mapping.  The positions and arrangement of colors are maintained, and only the color values are altered. The grid dimensions remain unchanged. The color mapping is as follows:

- Color 2 (red) is transformed to color 6 (magenta).
- Color 3 (green) is transformed to color 4 (yellow).
- Color 8 (azure) is transformed to color 9 (maroon).
```python
"""
The transformation rule is a direct color substitution, where each color in the input grid is replaced by a new color according to a specific mapping. The positions and arrangement of colors are maintained, and only the color values are altered. The grid dimensions remain unchanged. The color mapping is as follows:

- Color 2 (red) is transformed to color 6 (magenta).
- Color 3 (green) is transformed to color 4 (yellow).
- Color 8 (azure) is transformed to color 9 (maroon).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing colors based on a predefined mapping.
    
    Args:
        input_grid (numpy.ndarray): The input grid with integer color values.
    
    Returns:
        numpy.ndarray: The transformed grid with updated color values.
    """
    # Initialize the output grid as a copy of the input grid to preserve dimensions.
    output_grid = np.copy(input_grid)
    
    # Define the color mapping.
    color_map = {
        2: 6,  # Red to Magenta
        3: 4,  # Green to Yellow
        8: 9   # Azure to Maroon
    }
    
    # Iterate through the color map and replace colors in the output grid.
    for old_color, new_color in color_map.items():
        output_grid[input_grid == old_color] = new_color
        
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

The transformation rule is a direct color substitution.  Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 5 (gray) is transformed to color 1 (blue).
- Color 8 (azure) is transformed to color 9 (maroon).
- Color 6 (magenta) is transformed to color 2 (red).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
```python
"""
The transformation rule is a direct color substitution. Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 5 (gray) is transformed to color 1 (blue).
- Color 8 (azure) is transformed to color 9 (maroon).
- Color 6 (magenta) is transformed to color 2 (red).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing colors based on a predefined mapping.
    
    Args:
        input_grid (numpy.ndarray): The input grid with integer color values.
    
    Returns:
        numpy.ndarray: The transformed grid with updated color values.
    """
    # Initialize the output grid as a copy of the input grid to preserve dimensions.
    output_grid = np.copy(input_grid)
    
    # Define the color mapping.
    color_map = {
        5: 1,  # Gray to Blue
        8: 9,  # Azure to Maroon
        6: 2   # Magenta to Red
    }
    
    # Iterate through the color map and replace colors in the output grid.
    for old_color, new_color in color_map.items():
        output_grid[input_grid == old_color] = new_color
        
    return output_grid
```


**input**
```
9 4 2
9 4 2
9 4 2
```

![Image](006-example_4_input.png)


**output**
```
8 3 6
8 3 6
8 3 6
```

![Image](006-example_4_output.png)

**Natural Language Program:**

The transformation rule is a direct color substitution.  Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 9 (maroon) is transformed to color 8 (azure).
- Color 4 (yellow) is transformed to color 3 (green).
- Color 2 (red) is transformed to color 6 (magenta).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
```python
"""
The transformation rule is a direct color substitution. Each color in the input grid is replaced with a new color according to a fixed mapping. Specifically:

- Color 9 (maroon) is transformed to color 8 (azure).
- Color 4 (yellow) is transformed to color 3 (green).
- Color 2 (red) is transformed to color 6 (magenta).

The positions and arrangement of the colors are preserved; only the color values themselves are changed. The dimensions of the grid remain the same.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing colors based on a predefined mapping.
    
    Args:
        input_grid (numpy.ndarray): The input grid with integer color values.
    
    Returns:
        numpy.ndarray: The transformed grid with updated color values.
    """
    # Initialize the output grid as a copy of the input grid to preserve dimensions.
    output_grid = np.copy(input_grid)
    
    # Define the color mapping.
    color_map = {
        9: 8,  # Maroon to Azure
        4: 3,  # Yellow to Green
        2: 6   # Red to Magenta
    }
    
    # Iterate through the color map and replace colors in the output grid.
    for old_color, new_color in color_map.items():
        output_grid[input_grid == old_color] = new_color
        
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
