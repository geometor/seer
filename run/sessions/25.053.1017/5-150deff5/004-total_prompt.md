# 5-150deff5 • 004 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 5 0 0 0
0 5 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x75C2E517EC80>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 8 8 2 8 8 2 0 0 0
0 8 8 2 8 8 2 0 0 0
0 0 0 2 0 0 2 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x75C2E517D330>
Okay, here's my analysis of the example input-output pair:

**Perception of Elements:**

The task involves transforming a grid of colored pixels. The primary colors involved seem to be gray (5) in the input and azure (8) and red (2) in the output. The output grid appears to maintain the overall shape and dimensions of the input grid. The transformation seems to involve a color substitution based on the arrangement of the gray pixels, specifically creating an outline.

**YAML Block (Facts):**


```yaml
objects:
  - name: input_grid
    type: grid
    properties:
      dimensions: 8x10
      colors: [0, 5]
  - name: output_grid
    type: grid
    properties:
      dimensions: 8x10
      colors: [0, 2, 8]
  - name: gray_object
    type: object
    properties:
      color: 5
      shape: irregular
      location: varies

actions:
  - name: color_substitution
    agent: system
    input: gray_object
    parameters:
      - rule: "If a gray (5) pixel is adjacent to a white(0) pixel, change to azure(8), if not change to red(2)"

relationships:
  - type: adjacency
    subject: gray_pixel
    object: white_pixel
    result: color_change_to_azure

  - type: contained
    subject: gray_object
    object: input_grid

  - type: correspondence
    subject: input_grid
    object: output_grid
    properties: [dimensions]
```


**Natural Language Program:**

1.  **Identify the Input:** The input is a grid of pixels, primarily containing white (0) and gray (5) pixels.
2.  **Locate Gray Pixels:** Identify all pixels with the color gray (5).
3. **Determine the adjacent pixels:** For each gray pixel look at the directly adjacent pixels - do not include diagonals.
4.  **Apply Color Substitution Rules:**
    *   If a gray (5) pixel is adjacent to at least one white (0) pixel, change its color to azure (8) in the output grid.
    *   If the Gray(5) pixel has no adjacent white(0) pixels, change its color to red(2).
5.  **Maintain Other Pixels:** All white (0) pixels in the input grid remain white (0) in the output grid.
6.  **Output:** The output is a grid of the same dimensions as the input, with the gray pixels replaced according to the adjacency rule and all other pixels are the same.

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
