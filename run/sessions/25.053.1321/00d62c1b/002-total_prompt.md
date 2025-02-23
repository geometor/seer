# 00d62c1b • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x74153085B970>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x74153085B5B0>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a 6x6 grid. The input grid contains pixels of color 'white' (0) and 'green' (3). The output grid is identical to the input grid except for some green pixels that become 'yellow'(4). The change appears to affect only some green pixels. Examining the locations, It appears that the yellow pixels are always adjacent to two green pixels, on opposing sides.

**YAML Block - Facts:**


```yaml
task_description: |
  The task is to transform a grid of pixels, changing some green pixels to yellow.
objects:
  - type: grid
    properties:
      - dimensions: 6x6
      - elements: pixels
        properties:
          - color:
              values: [0, 3, 4] # white, green, yellow
  - type: pixel
    properties:
      - color:
          values: [0, 3, 4] # white, green, yellow
      - position:
          type: coordinates # (row, column)

actions:
  - name: change_color
    agent: system
    preconditions:
      - object: pixel
        property: color
        value: 3 # green
      - condition: A green pixel is adjacent to two other green pixels in opposite directions (horizontally or vertically).
    postconditions:
      - object: pixel
        property: color
        value: 4    # yellow

relationships:
    - type: adjacency
      description: Pixels can be adjacent horizontally, vertically, or diagonally.
      properties:
        - direction: [horizontal, vertical]

```


**Natural Language Program:**

1.  **Iterate** through each pixel in the input grid.
2.  **Identify** green (3) pixels.
3.  For each green pixel, **check for adjacency** with other green pixels:
    *   Check if there is a green pixel directly above AND directly below.
    *   Check if there is a green pixel directly to the left AND directly to the right.
4.  If *either* of the adjacency conditions in step 3 is true, **change** the pixel's color to yellow (4).
5.  **Return** the modified grid.

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
