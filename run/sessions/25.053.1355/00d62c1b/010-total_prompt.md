# 00d62c1b • 010 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 0 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FA38657820>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 4 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FA386F12D0>
Okay, here's my analysis of the provided example, broken down into perceptions, a YAML fact block, and a natural language program.

**Perception:**

The input grid contains a shape made of green (3) pixels. The output grid is identical to the input grid, except that a single pixel within the green shape has changed from green (3) to yellow (4). This modified pixel appears to be centrally located within the shape, specifically, surrounded by other green cells.

**YAML Fact Block:**


```yaml
facts:
  - object: shape
    color: green (3)
    description: A contiguous block of green pixels.
  - action: modification
    target: single pixel within shape
    from_color: green (3)
    to_color: yellow (4)
    location_criteria:  surrounded by other green pixels
```


**Natural Language Program:**

1.  **Identify the Shape:** Locate the contiguous block of green (3) pixels within the input grid.
2.  **Find Interior Pixel:** Within the identified shape, locate a single green pixel which surrounded by other green pixels.
3.  **Modify Pixel:** Change the color of this interior pixel from green (3) to yellow (4).
4.  **Preserve Remainder:** Copy the input grid data, with the changed pixel, creating the output grid.

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
