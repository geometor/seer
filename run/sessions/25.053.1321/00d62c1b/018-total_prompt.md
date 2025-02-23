# 00d62c1b • 018 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 3 0 0 0 0
0 0 0 0 3 0 0 0 0 0
0 3 3 0 3 3 0 3 0 0
3 0 0 3 0 0 3 0 3 0
0 0 0 3 0 0 3 3 0 0
0 0 0 3 0 0 3 0 0 0
0 0 0 3 0 0 3 0 0 0
0 0 0 0 3 3 0 3 0 0
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x74153085B970>

**output:**
```
0 0 0 0 0 3 0 0 0 0
0 0 0 0 3 0 0 0 0 0
0 3 3 0 3 3 0 3 0 0
3 0 0 3 4 4 3 4 3 0
0 0 0 3 4 4 3 3 0 0
0 0 0 3 4 4 3 0 0 0
0 0 0 3 4 4 3 0 0 0
0 0 0 0 3 3 0 3 0 0
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7415308F9270>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves a grid of pixels, each with a numerical value representing a color. The primary colors observed are white (0) and green (3). The transformation seems to involve identifying a specific region within the green (3) pixels and changing the color of a subset of those pixels to yellow (4).

**YAML Fact Documentation:**


```yaml
facts:
  - object: grid
    properties:
      - dimensions: 10x10
      - elements: pixels
  - object: pixel
    properties:
      - color:
        - white: 0
        - green: 3
        - yellow: 4
  - observation: transformation_involves_color_change
  - action:
    - name: identify_region
    - description: A specific region of green pixels is selected.
  - action:
    - name: change_color
    - description: The color of the pixels within the identified region is changed from green to yellow.
  - relationship:
    - object1: green_pixels
    - object2: identified_region
    - type: subset
    - description: The region is fully enclosed by green (3).
  - relationship:
      - subject: identified_region
        predicate: is_contiguous
        object: True
```


**Natural Language Program:**

1.  **Identify the Input Object:** The input is a 10x10 grid of pixels, where each pixel has a color value (0 or 3 in the input, with 0, 3, and 4 in the output).

2.  **Locate the Region of Interest:** Find the largest contiguous region of green (3) pixels.

3. **Identify inner region**: Locate the set of pixels such that at least two pixels on opposite sides (vertical or horizontal) are the same color.

4.  **Transform the Region:** Change the color of the central pixels from green (3) to yellow (4). The central area are the green colored shapes that form an enclosed shape with a single open area of at least two green squares in horizontal and vertical directions.

5.  **Output:** Return the modified grid, now containing colors to 0, 3, and 4.

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
