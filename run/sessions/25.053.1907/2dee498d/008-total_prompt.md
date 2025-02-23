# 2dee498d • 008 • example_2 - CODE

---

# Example

**input:**
```
2 0 0 1 2 0 0 1 2 0 0 1
4 2 1 4 4 2 1 4 4 2 1 4
4 1 2 4 4 1 2 4 4 1 2 4
1 0 0 2 1 0 0 2 1 0 0 2
```

<PIL.Image.Image image mode=RGB size=768x256 at 0x7EF8F235FB50>

**output:**
```
2 0 0 1
4 2 1 4
4 1 2 4
1 0 0 2
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7EF8F235FA60>
Okay, here's my analysis of the example input-output pair:

**Perception of Elements:**

The input and output are both grids of colored pixels. The input grid is wider than the output grid. It appears that the output grid is a cropped version of the input grid. The colors and their relative positions within the overlapping region are identical between input and output. The cropping seems to be removing columns from the right side of the input grid.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      - name: input_grid
        dimensions: [4 x 12]
        colors: [0, 1, 2, 4]
      - name: output_grid
        dimensions: [4 x 4]
        colors: [0, 1, 2, 4]

actions:
  - type: cropping
    description: Removing columns from the right side of the input_grid.

relationships:
  - output_grid is a subset of input_grid.
  - color and relative position of pixels within the overlapping region is preserved

```


**Natural Language Program:**

The output grid is created by taking the leftmost portion of the input grid. Specifically, take the first four columns of the input grid to form the output grid. This is a simple horizontal cropping operation.

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
