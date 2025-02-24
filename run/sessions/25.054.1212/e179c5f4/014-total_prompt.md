# e179c5f4 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC47F93F10>

**output:**
```
8 8 8 1
8 8 1 8
8 1 8 8
1 8 8 8
8 1 8 8
8 8 1 8
8 8 8 1
8 8 1 8
8 1 8 8
1 8 8 8
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC47585C30>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a transformation of a grid of single-digit integers (representing colors) into another grid of the same dimensions. The input grid appears to be mostly filled with 0s (white), with a single 1 (blue) in the bottom-left corner. The output grid replaces all 0s with 8s (azure) and the single 1 with, well, a pattern centered on the original location of the 1. The transformation seems to involve flood-filling with the 8s, then constructing a cross.

**YAML Fact Documentation:**


```yaml
facts:
  - object: input_grid
    type: grid
    properties:
      dimensions: 10x4 (height x width)
      elements: integers (0-9)
      dominant_color: 0 (white)
      special_element:
        value: 1 (blue)
        location: [9, 0] (row, column) - bottom-left

  - object: output_grid
    type: grid
    properties:
      dimensions: 10x4 (height x width)
      elements: integers (0-9)
      dominant_color: 8 (azure)
      special_pattern:
        center_value: 1 (blue)
        center_location: [9,0]
        pattern: cross
        pattern_elements: 1 (blue)

  - action: transformation
    type: replacement and pattern creation
    details:
      - replace all instances of 0 with 8
      - create a cross pattern of 1s centered at original location of the 1.
        - The '1' extends to each edge of the grid.
```


**Natural Language Program:**

1.  **Background Fill:** Replace all 0s in the input grid with 8s.

2.  **Cross Construction:**
    *   Locate the single cell with the value of 1 in the input grid
    *   In the output grid, set this original location to 1.
    *   From this position extend the value 1 outwards along the row and column to form the four points of the cross.

In short form: Fill the background and construct a centered cross from the 'seed' of the initial blue pixel.

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
