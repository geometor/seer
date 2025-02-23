# 00d62c1b • 008 • example_2 • investigate_coder

---

## Example 2

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

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF01B1150>

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

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF01B3AF0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, initially with values of 0 (white) and 3 (green). The transformation appears to involve a very localized change: a single pixel changes from 0 (white) to 4 (yellow). This changed pixel is surrounded by green pixels. The position is not constant.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      width: 10
      height: 10
      cells:
        - value: 0 # White
          color: white
        - value: 3 # Green
          color: green
        - value: 4 # Yellow
          color: yellow

  - type: pixel
    properties:
      color: [white, green, yellow]

actions:
  - name: change_color
    agent: unknown
    target: pixel
    precondition:
      target_color: white
      neighbor_colors:
              - green
              - green
              - green
              - green
    postcondition:
      target_color: yellow

relationships:
   - type: adjacency
     description: "Pixels are considered adjacent if they share a side (not diagonally)."
```


**Natural Language Program:**

1.  **Identify Target:** Find a white (0) pixel that is completely surrounded by four green (3) pixels (above, below, left, and right, *not* diagonally).

2. **Change Pixel:** Change the color of *only* that identified pixel to yellow (4).

3.  **Leave all other pixels unchanged.**

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
