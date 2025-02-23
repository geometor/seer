# 5-150deff5 • 006 • example_3 - CODE

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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)


*error:*
No candidates returned in response.
```yaml
observations:
  - input_grid: |
      - The input grid is 11x9.
      - Contains multiple instances of the digit '0' and '5'.
      - The digit '5' forms several distinct shapes.
  - output_grid: |
      - The output grid is also 11x9.
      - Contains digits '0', '8', and '2'.
      - The digit '8' replaces some of the '5's, and '2' replaces others.

transformation_rules:
  - rule: |
      Replace some shapes formed by '5' with '8' and others with '2'. The replacement appears to be based on the shape or pattern formed by the '5's. Specifically, L-shaped structures of 5 are replaced by 8, and other parts are replaced by 2, keeping other parts of input unchanged.
```

```python
"""
Replace some shapes formed by '5' with '8' and others with '2'. The replacement appears to be based on the shape or pattern formed by the '5's. Specifically, L-shaped structures of 5 are replaced by 8, and other parts are replaced by 2, keeping other parts of input unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing some shapes of '5' with '8' and others with '2', based on their shape.
    L-shaped structures of '5' are replaced by '8', and others by '2'.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Helper function to find connected components
    def get_connected_components(grid, value):
        visited = set()
        components = []

        def dfs(r, c, current_component):
            if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != value:
                return
            visited.add((r, c))
            current_component.append((r, c))
            dfs(r + 1, c, current_component)
            dfs(r - 1, c, current_component)
            dfs(r, c + 1, current_component)
            dfs(r, c - 1, current_component)

        for r in range(grid.shape[0]):
            for c in range(grid.shape[1]):
                if grid[r, c] == value and (r, c) not in visited:
                    current_component = []
                    dfs(r, c, current_component)
                    components.append(current_component)
        return components

    # Find all connected components of '5'
    components_5 = get_connected_components(input_grid, 5)

    # Iterate through each component and determine the replacement
    for component in components_5:
        # Check if the component is L-shaped (size could be 3 or more for an L)
        if len(component) >= 3:
            is_L_shaped = False
            
            # Convert component tuples to a NumPy array for easier manipulation
            coords = np.array(component)
            min_r, min_c = np.min(coords, axis=0)
            max_r, max_c = np.max(coords, axis=0)

            # Check different possible simple L shapes.
            if (max_r - min_r == 1 and max_c - min_c >=1) or \
               (max_r - min_r >= 1 and max_c - min_c == 1):
                is_L_shaped = True
           

            # Replace based on shape
            if is_L_shaped:
                for r, c in component:
                    output_grid[r, c] = 8
            else:
                for r, c in component:
                    output_grid[r, c] = 2

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

![Image](002-example_2_input.png)


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

![Image](002-example_2_output.png)


*error:*
No candidates returned in response.
```yaml
observations:
  - input_grid: |
      - The input grid is 8x10.
      - Contains digits '0' and '5'.
      - The digit '5' forms several distinct shapes, including horizontal lines and vertical segments.
  - output_grid: |
      - The output grid is also 8x10.
      - Contains digits '0', '8', and '2'.
      - The digit '8' replaces some of the '5's, and '2' replaces others, based on their shape and position.

transformation_rules:
  - rule: |
      Replace specific shapes formed by '5' with '8' or '2'. L-shaped structures and horizontal lines of '5' are replaced by '8', while isolated or other specific patterns are replaced by '2'. The rule distinguishes between different configurations of '5's to determine the replacement.
```

```python
"""
Replace specific shapes formed by '5' with '8' or '2'. L-shaped structures and horizontal lines of '5' are replaced by '8', while isolated or other specific patterns are replaced by '2'. The rule distinguishes between different configurations of '5's to determine the replacement.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing some shapes of '5' with '8' and others with '2', based on their shape.
    L-shaped structures and horizontal lines of '5' are replaced by '8', while others by '2'.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Helper function to find connected components
    def get_connected_components(grid, value):
        visited = set()
        components = []

        def dfs(r, c, current_component):
            if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != value:
                return
            visited.add((r, c))
            current_component.append((r, c))
            dfs(r + 1, c, current_component)
            dfs(r - 1, c, current_component)
            dfs(r, c + 1, current_component)
            dfs(r, c - 1, current_component)

        for r in range(grid.shape[0]):
            for c in range(grid.shape[1]):
                if grid[r, c] == value and (r, c) not in visited:
                    current_component = []
                    dfs(r, c, current_component)
                    components.append(current_component)
        return components

    # Find all connected components of '5'
    components_5 = get_connected_components(input_grid, 5)

    # Iterate through each component and determine the replacement
    for component in components_5:
        # Check if the component is L-shaped or a horizontal line
        if len(component) >= 2:
            is_L_shaped = False
            is_horizontal_line = False

            # Convert component tuples to a NumPy array for easier manipulation
            coords = np.array(component)
            min_r, min_c = np.min(coords, axis=0)
            max_r, max_c = np.max(coords, axis=0)
            
            # Check for simple L shapes
            if (max_r - min_r == 1 and max_c - min_c >= 1) or \
               (max_r - min_r >= 1 and max_c - min_c == 1):
                is_L_shaped = True
                
            #Check for horizontal line
            if (max_r - min_r == 0 and max_c - min_c >=1):
                is_horizontal_line = True

            # Replace based on shape
            if is_L_shaped or is_horizontal_line:
                for r, c in component:
                    output_grid[r, c] = 8
            else:
                for r, c in component:
                    output_grid[r, c] = 2

    return output_grid
```


**input**
```
0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 0 0 0
0 0 0 0 5 5 0 0 0
0 0 0 5 0 0 0 0 0
0 0 0 5 5 5 0 0 0
0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](004-example_3_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 2 2 2 8 8 0 0 0
0 0 0 0 8 8 0 0 0
0 0 0 2 0 0 0 0 0
0 0 0 2 8 8 0 0 0
0 0 0 2 8 8 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](004-example_3_output.png)


*error:*
No candidates returned in response.
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
