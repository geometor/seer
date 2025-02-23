# AboveBelow1 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 4 0 0 4 4 4
0 0 0 4 4 4 4 0 0 4 4 4
0 0 0 4 4 4 4 0 0 4 4 4
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x7995F901BF40>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 0
0 0 0 4 4 4 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x7995F901BB20>
Okay, here's my analysis of the example input-output pair, formatted as requested:

**Perception of Task Elements:**

The task involves manipulating a grid of colored pixels. The primary colors involved appear to be white (0), yellow (4), and red (2). The transformation seems to involve removing or deleting certain colored regions based on their shape and position. The overall context appears to be object deletion based on some criteria, in this instance shape.

**YAML Block - Facts:**


```yaml
objects:
  - type: rectangle
    color: yellow (4)
    properties:
      - contiguous
      - horizontal_extent: 4
      - vertical_extent: 3
    actions:
      - deleted
    conditions:
      - top_left: [1,3]
      
  - type: rectangle
    color: yellow (4)
    properties:
      - contiguous
      - horizontal_extent: 3
      - vertical_extent: 3
    actions:
       - deleted
    conditions:
      - top_left: [8, 9]

  - type: rectangle
    color: red (2)
    properties:
      - contiguous
      - horizontal_extent: 12
      - vertical_extent: 1
    actions:
      - retained # Not deleted
    conditions:
      - top_left: [6, 0]

relationships:
  - object1: yellow rectangle 1
    relation: above
    object2: red rectangle
  - object1: yellow rectangle 2
    relation: below
    object2: red rectangle
```


**Natural Language Program:**

1.  **Identify** all contiguous rectangular regions of yellow (4) pixels.
2.  **Identify** all contiguous rectangular regions of red (2) pixels.
3.  **Delete** all identified yellow regions.
4.  **Retain** all identified red regions.
5.  The output grid consists of the remaining pixels after the deletion of the yellow regions.

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
