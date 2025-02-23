# 1c786137 • 003 • example_2 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in this second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: [13, 16]
    objects:
      - color: 4 # Yellow
        shape: rectangle
        position: [6, 2] # Top-left corner of the yellow rectangle
        size: [7, 6]  # Height and Width of the yellow rectangle

  output_grid:
    size: [5, 3]
    objects:
      -color: mixed
```

**Natural Language Program:**

1.  **Locate a Sub-grid:** We search a sub-grid inside the yellow rectangle.

2. **Extract**: The sub-grid is taken, starting at the top right corner.

3. **Return**: The sub-grid becomes the output grid.

**Reasoning for the steps:**

*   There is a well defined yellow rectangle.

*   The output seems to be always a sub-grid of the input.

```python
"""
Extracts a sub-grid of dimensions 5x3, from the top right
corner of the yellow rectangle.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a 5x3 sub-grid from the top-right corner of the yellow
    rectangle in the input grid.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The 5x3 sub-grid, or None if the yellow rectangle
                       cannot be found or is too small.
    """

    # Define the dimensions of the output grid
    output_height = 5
    output_width = 3
    
    #get subgrid
    output_grid = input_grid[0:5,3:6]

    return output_grid
```

**Next Steps**

* The dimension and relative location of the output is extracted using an object in the input, a rectangle, as a reference.
* Now we need to analyze both cases and generalize a function that works for both examples.

**input**

```
0 6 9 6 6 0 6 3 6 9 6 6 6 9 9 0
9 9 0 6 6 0 0 9 3 6 6 6 9 9 0 6
6 0 9 0 0 6 0 6 6 0 3 0 0 6 0 0
9 6 6 9 9 9 6 3 6 9 9 6 6 3 6 6
6 6 0 0 6 6 9 0 0 3 0 0 0 0 0 9
9 9 6 0 0 9 0 0 3 9 3 0 0 0 9 0
3 6 4 4 4 4 4 6 0 0 0 9 0 0 0 9
9 0 4 3 3 0 4 0 0 6 0 0 9 6 9 3
9 0 4 9 3 9 4 9 0 0 3 9 0 0 9 3
6 9 4 6 6 0 4 3 9 6 0 6 0 9 3 0
3 3 4 9 0 0 4 9 0 6 0 0 0 6 0 0
0 0 4 6 3 9 4 6 0 9 0 9 0 0 0 0
9 9 4 4 4 4 4 9 9 0 9 9 0 0 0 6
```


