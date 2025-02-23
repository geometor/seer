# c1d99e64 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
3 0 3 3 3 3 3 0 3 3 3 0 3 0 3
3 0 3 0 3 3 3 0 3 0 3 0 0 3 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3 0 0 3 0 0 3 3 0 3 0 3 3 0 0
3 0 3 3 3 3 3 3 3 3 0 3 3 3 3
3 0 3 3 3 3 3 3 0 0 3 3 0 3 3
0 0 3 0 3 0 3 0 3 0 0 3 3 3 0
3 0 0 3 3 3 0 0 3 0 3 3 0 0 3
3 0 3 3 3 3 3 0 3 3 3 3 3 0 3
3 0 0 3 3 0 3 3 3 3 3 3 3 3 0
3 0 3 3 3 3 3 3 0 3 3 3 0 3 3
3 0 3 3 3 0 3 0 0 3 0 3 3 3 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
3 0 3 0 0 3 0 3 3 0 3 3 3 3 0
3 0 0 3 0 3 3 0 3 0 3 3 0 0 3
3 0 0 3 3 3 3 3 0 3 3 0 0 3 3
0 0 3 3 0 3 3 0 0 3 0 3 0 3 0
```

<PIL.Image.Image image mode=RGB size=960x1088 at 0x70FFF0F9D600>

**output:**
```
3 2 3 3 3 3 3 0 3 3 3 0 3 0 3
3 2 3 0 3 3 3 0 3 0 3 0 0 3 0
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
3 2 0 3 0 0 3 3 0 3 0 3 3 0 0
3 2 3 3 3 3 3 3 3 3 0 3 3 3 3
3 2 3 3 3 3 3 3 0 0 3 3 0 3 3
0 2 3 0 3 0 3 0 3 0 0 3 3 3 0
3 2 0 3 3 3 0 0 3 0 3 3 0 0 3
3 2 3 3 3 3 3 0 3 3 3 3 3 0 3
3 2 0 3 3 0 3 3 3 3 3 3 3 3 0
3 2 3 3 3 3 3 3 0 3 3 3 0 3 3
3 2 3 3 3 0 3 0 0 3 0 3 3 3 0
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
3 2 3 0 0 3 0 3 3 0 3 3 3 3 0
3 2 0 3 0 3 3 0 3 0 3 3 0 0 3
3 2 0 3 3 3 3 3 0 3 3 0 0 3 3
0 2 3 3 0 3 3 0 0 3 0 3 0 3 0
```

<PIL.Image.Image image mode=RGB size=960x1088 at 0x70FFF0F9D4E0>
Okay, here's my analysis of the provided input-output example:

**Perception of Elements:**

The input and output grids are the same size (17x15). The primary colors involved seem to be green (3), white (0), and red (2). The transformation appears to involve a selective replacement of white (0) pixels with red (2) pixels, while green (3) pixels remain unchanged. The red pixels appear to form horizontal lines in the regions where the white pixels were.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 17x15
      elements: pixels
      colors: [green, white, red]

  - type: pixel
    properties:
      color:
        green: 3
        white: 0
        red: 2

actions:
  - name: replace_color
    properties:
      source_color: white
      target_color: red
    constraints:
      - "Only replace white pixels which neighbor a green pixel, if we consider it as a starting point. Every row of green starting point changes from up to down, till the line of 0 changes completely."
      
relationships:
  - type: adjacency
    description: Pixels are considered adjacent if they share a side (not diagonally).
  - type: containment
    description: The grid contains pixels.
```


**Natural Language Program:**

1.  **Identify Starting Points:** Locate all white (0) pixels that are directly adjacent (above, below, left, or right) to a green (3) pixel.
2. **Horizontal Replacement - Row by row:**
      - Every row which contain the green color, change every 0 to 2 in the same row starting from the top.
3.  **Leave Other Pixels Unchanged:** All green (3) pixels, and any white(0) that do not satisfy conditions from horizontal replacement, remain the same.

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
