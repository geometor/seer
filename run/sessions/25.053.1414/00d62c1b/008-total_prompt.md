# 00d62c1b • 008 • example_2 - CODE

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

<PIL.Image.Image image mode=RGB size=640x640 at 0x7D261845B910>

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

<PIL.Image.Image image mode=RGB size=640x640 at 0x7D26184F12A0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, initially containing only white (0) and green (3) pixels. The transformation seems to involve a single, localized change: a single green (3) pixel within a cluster of green pixels changes to yellow (4).  The position chosen for the color change appears to be related to adjacency - the pixel above and to the right of a cluster of three green pixels in an L-shape.

**YAML Block (Facts):**


```yaml
objects:
  - name: grid
    type: 2D array
    elements: pixels
    properties:
      - width: 10
      - height: 10
      - color_values: [0, 3, 4]

  - name: pixel
    type: element
    properties:
      - color:
          type: integer
          values: [0, 3, 4]  # white, green, yellow
      - position:
          type: coordinate (row, column)

  - name: green_cluster
    type: object
    definition: contiguous block of green (3) pixels
    properties:
       - shape: [ L-shape ]

actions:
  - name: change_color
    agent: system
    target: single green pixel
    precondition: pixel is part of a green cluster
    postcondition: pixel color changes to yellow (4)
    constraints:
      - location : pixel is chosen based on green cluster shape and appears to follow a consistent rule.  Specifically, the green pixel that has a green pixel diagonally down and to the left, and a green pixel below it is changed.

relationships:
  - type: adjacency
    description: Pixels are considered adjacent if they share a side or a corner.
  - type: containment
    description: The grid contains pixels.
  - type: part_of
    description: A green pixel can be part of a green cluster.
```


**Natural Language Program:**

1.  **Identify Green Clusters:** Locate all contiguous blocks of green (3) pixels within the grid.
2.  **Locate Target Pixel:** If there are at least three green pixels forming an L-shape (2x2 minus the top-left pixel), select the single green pixel for modification that lies on the top-right tip of the L-shape.
3. **Change Pixel color to yellow (4) in the grid**.

In more detail, if an L-shape can be formed, we look for a green pixel (A) which is adjacent to:
 - green pixel below, and
 - green pixel diagonally down and to the left.

If such a pixel (A) is found, its color is changed from green to yellow.

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
