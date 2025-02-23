# 00d62c1b • 026 • example_4 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 3 3 3 0 0 0 0
0 0 3 0 0 3 0 0 0 0
0 0 3 0 0 3 0 3 0 0
0 0 3 3 3 3 3 3 3 0
0 0 0 3 0 0 0 0 3 0
0 0 0 3 0 0 0 3 3 0
0 0 0 3 3 0 0 3 0 3
0 0 0 3 0 3 0 0 3 0
0 0 0 0 3 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7398A12F68C0>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 3 3 3 0 0 0 0
0 0 3 4 4 3 0 0 0 0
0 0 3 4 4 3 0 3 0 0
0 0 3 3 3 3 3 3 3 0
0 0 0 3 0 0 0 0 3 0
0 0 0 3 0 0 0 3 3 0
0 0 0 3 3 0 0 3 4 3
0 0 0 3 4 3 0 0 3 0
0 0 0 0 3 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7398A1243490>
Okay, here's my analysis of the provided example, structured as requested:

**Perception of Elements:**

The task involves a grid of pixels, each with a numerical value representing a color. The primary colors observed are white (0) and green (3). In the output, some green (3) pixels are changed to yellow (4). The transformation seems to be localized and focused on specific green pixels. It appears that internal, isolated green pixels that are surrounded by other green pixels are the targets for transformation.

**YAML Block (Facts):**


```yaml
objects:
  - type: pixel
    properties:
      value: int # 0-9
      color: str # mapped from value
      position: (int, int) # row, column
    relationships:
      - adjacent_to: List[pixel] # pixels directly above, below, left, or right

actions:
  - name: change_color
    agent: system
    target: pixel
    precondition:
        - target.color == green
        - count_adjacent(target, green) == 4 # condition
        - count_adjacent(target, green, diagonal=True) in [4,5,6,7,8]
    postcondition:
      - target.value == 4
      - target.color == yellow

```


**Natural Language Program:**

1.  **Identify Target Pixels:** Iterate through all pixels in the input grid. For each pixel, check if it meets the following conditions:
    *   The pixel's color is green (value 3).
    *   The pixel is completely surrounded orthogonally (up, down, left, right) by other green pixels. Diagonal direction is not important, but a green pixel will change to yellow if at least 4 green pixels are immediate neighbors.
2.  **Change Color:** If a pixel meets all criteria (is a "surrounded" green pixel), change its value to 4 (yellow).
3.  **Output:** The output grid is the result of applying these changes to the input grid. The core concept is identifying and recoloring internal green pixels that are fully enclosed by other green pixels.

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
