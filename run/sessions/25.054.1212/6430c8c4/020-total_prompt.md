# 6430c8c4 • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
7 0 7 0
0 0 7 7
7 0 7 7
7 7 0 0
4 4 4 4
0 0 2 2
0 0 0 0
2 0 0 2
0 2 0 2
```

<PIL.Image.Image image mode=RGB size=256x576 at 0x7BFC48A615A0>

**output:**
```
0 3 0 0
3 3 0 0
0 3 0 0
0 0 3 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7BFC47F93CD0>
Okay, here's a breakdown of my observations and a proposed natural language program for the transformation:

**Perception of Elements:**

*   **Input Grid:** A larger grid (9x4) containing various colors represented by digits 0-7, with apparent clusters or shapes.  There's a distinct horizontal line of yellow (4) pixels. Below this line are red (2) and white (0) pixels. Above the line, we have orange (7) and white (0) pixels.
*   **Output Grid:** A smaller grid (4x4). It seems to exclusively use green (3) and white (0) pixels. The green pixels appear in the top-left quadrant of what we imagine the input looks like mapped onto this smaller grid, corresponding to where orange was most prominent above the yellow line.
* **Transformation:** A reduction in both dimensions and a color change. It appears related to the position and configuration of non-zero colored pixels above the yellow horizontal divider line.

**YAML Facts:**


```yaml
facts:
  - object: input_grid
    type: grid
    dimensions: 9x4
    elements:
      - color: 0 # white
        value: 0
      - color: orange
        value: 7
      - color: yellow
        value: 4
      - color: red
        value: 2
    features:
      - horizontal_line:
          color: yellow
          row: 4

  - object: output_grid
    type: grid
    dimensions: 4x4
    elements:
      - color: 0 # white
        value: 0
      - color: green
        value: 3
    features:
      - upper_left_quadrant_focus: true
```


**Natural Language Program:**

1.  **Identify Divider:** Locate the horizontal line of yellow (4) pixels in the input grid. This line divides the input grid into an "upper region" and "lower region".
2.  **Focus on Upper Region:** Disregard the "lower region" of the input grid (everything at or below the yellow line).
3. **Determine output size:** The output size is the dimensions of the "upper region".
4.  **Map to Output:** Create an output grid of the dimensions determined in the previous step. For each non-white pixel in the "upper region", change the color to green (3). Change all the white pixels to 0.


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
