# 3af2c5a8 • 008 • example_2 - CODE

---

# Example

**input:**
```
0 0 3 3
0 3 0 3
3 3 3 0
```

<PIL.Image.Image image mode=RGB size=256x192 at 0x7EF8F235FA60>

**output:**
```
0 0 3 3 3 3 0 0
0 3 0 3 3 0 3 0
3 3 3 0 0 3 3 3
3 3 3 0 0 3 3 3
0 3 0 3 3 0 3 0
0 0 3 3 3 3 0 0
```

<PIL.Image.Image image mode=RGB size=512x384 at 0x7EF8F235FA00>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Task Elements:**

The task involves transforming a smaller grid (input) into a larger grid (output). The primary element is the colored pixel, with values representing colors (0: white, 3: green). The input grid seems to be expanded or replicated in the output grid, with some potential mirroring or reflection involved. The shape changes from a 3x4 to a 6x8 grid.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    properties:
      - dimensions: [rows, columns]
      - elements: pixels
      - values: [0, 3] # white and green
  - observation: input_grid
    properties:
      - dimensions: [3, 4]
  - observation: output_grid
    properties:
      - dimensions: [6, 8]
  - action: expansion
    description: The input grid is expanded to create the output grid.
  - relationship:
      - subject: input_grid
      - relation: becomes
      - object: output_grid
      - details:
          - rows: doubled
          - columns: doubled
  - action: mirroring
    description: potential mirroring is observed along row and/or column
```


**Natural Language Program:**

1.  **Double Dimensions:** The input grid's dimensions (rows and columns) are doubled to determine the output grid's dimensions.
2.  **Replicate and Mirror:** The input seems to be duplicated, it looks like it is both reflected vertically and horizontally to fill the output grid.

In summary, the transformation rule is to double the input grid, and reflect on both axis.

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
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
