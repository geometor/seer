# 72ca375d • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 4 4 0 0 0 0 0 0
0 0 4 4 0 0 8 8 8 0
0 0 0 0 0 0 8 0 8 8
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 2 2 2 2 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7BFC4890A0E0>

**output:**
```
4 4
4 4
```

<PIL.Image.Image image mode=RGB size=128x128 at 0x7BFC47FBB6D0>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Task Elements:**

The task involves transforming a grid of colored pixels (represented by numbers 0-9) into a smaller grid. The input grid contains several distinct colored regions, while the output grid seems to represent only one of these regions. The colors in the output are the same as in the input. The output size appears substantially smaller than the input size. The most notable aspect is the selection of a specific colored object.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      rows: 10
      columns: 10
      elements: integers (0-9) representing colors
    role: input

  - type: grid
    properties:
      rows: 2
      columns: 2
      elements: integers (0-9) representing colors
    role: output
  - type: object
    properties:
       color: 4 # yellow
       shape: rectangle
       location:
          start: [1,2] #row, col
          end: [2,3]
    role: selected_object

relationships:
   -  type: contains
      from: input
      to: selected_object

actions:
  - type: select
    agent: implicit
    target: object of color 4
    description: The 2x2 yellow rectangle at the top-left of input

```


**Natural Language Program:**

1.  **Identify:** Locate the 2x2 square region of yellow (color 4) pixels in the input grid.
2.  **Extract:** Copy this 2x2 square region.
3.  **Output:** The output grid is the extracted 2x2 yellow square.

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
