# AboveBelow9 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 3 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 4 4 4
0 0 0 0 3 3 3 0 0 0 0 0
0 0 0 0 0 0 3 0 0 0 0 0
0 0 0 0 0 0 3 0 0 0 0 0
0 0 3 0 0 3 3 0 0 0 0 0
0 0 3 0 0 3 0 0 0 0 0 0
0 0 3 3 3 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x640 at 0x7995F445C190>

**output:**
```
0 0 0 0 3 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x640 at 0x7995F445E7D0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. Both grids contain single-digit integers (0-9), representing different colors. The primary colors observed are white (0), green (3), and yellow (4). The output grid appears to be a simplified or filtered version of the input grid. Specifically, the green (3) and some parts are removed, but the yellow remains.

**YAML Block (Facts):**


```yaml
objects:
  - id: grid_input
    type: grid
    description: 2D array of integers representing colors
    dimensions: 10x12
    elements:
      - color: white
        value: 0
      - color: green
        value: 3
      - color: yellow
        value: 4

  - id: grid_output
    type: grid
    description: 2D array of integers representing colors
    dimensions: 10x12
    elements:
      - color: white
        value: 0
      - color: yellow
        value: 4

actions:
  - name: remove_color
    description: Remove all pixels of a specific color from the grid.
    parameters:
      - color: The color to be removed.

relationships:
   - subject: grid_output
     relation: derived_from
     object: grid_input
     description:  grid_output is created by modifying grid_input
     rule: "All green (3) pixels in grid_input are changed to white (0) in grid_output. Yellow (4) stays."
```


**Natural Language Program:**

1.  **Identify** all pixels in the input grid that are green (value 3).
2.  **Change** the value of these identified pixels to white (value 0).
3.  **Keep** all other values. Specifically, keep all instances of yellow (4).
4. **Create** output is the modified input.

In essence, the transformation rule is to remove all green pixels while preserving other colored pixels, especially the yellow ones.

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
