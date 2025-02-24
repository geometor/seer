# b8cdaf2b • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0
0 2 0
2 4 2
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC48A63190>

**output:**
```
4 0 4
0 2 0
2 4 2
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC4423F730>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves a 3x3 grid of colored pixels. The colors are represented by integers. The transformation seems to involve a change in the color of specific pixels based on their initial color and possibly their position. Specifically, the white (0) pixels in the top row are changing to yellow (4).

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    dimensions: 3x3
    elements: pixels
    properties:
      - color:
        mapping:
          0: white
          2: red
          4: yellow

observations:
  - input:
      top_row: [0, 0, 0]
      middle_row: [0, 2, 0]
      bottom_row: [2, 4, 2]
  - output:
      top_row: [4, 0, 4]
      middle_row: [0, 2, 0]
      bottom_row: [2, 4, 2]

actions:
  - change_color:
      from: 0 #white
      to: 4   #yellow
      conditions:
          location: top row
          original_color: 0 #white
```


**Natural Language Program:**

1.  **Identify** the top row of the input grid.
2.  **For each pixel** in the top row:
    *   **If** the pixel's color is white (0), **change** its color to yellow (4).
3.  **Keep** all other pixels unchanged.
4.  **Construct** output using modified and non-modified rows.

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
