# 2013d3e2 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 7 7 0 0 0 0
0 0 0 6 8 8 6 0 0 0
0 0 7 8 4 4 8 7 0 0
0 0 7 8 4 4 8 7 0 0
0 0 0 6 8 8 6 0 0 0
0 0 0 0 7 7 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7BFC443911E0>

**output:**
```
0 0 7
0 6 8
7 8 4
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC44391630>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves transforming a larger grid (10x10) into a smaller grid (3x3). The larger grid contains a central "shape" composed of non-zero colored pixels, surrounded by zero-valued (white) pixels. The smaller grid seems to extract a portion of this central shape. The colors and their spatial relationships are preserved in the output.  The output grid appears to capture the top-left "corner" of the central object where a non-white pixel exists. The size of the output (3 x 3) may be constant.

**YAML Block - Facts:**


```yaml
facts:
  - type: grid
    description: Input grid is 10x10, output grid is 3x3.
    input_size: [10, 10]
    output_size: [3, 3]
  - type: object
    description: A central, multi-colored object exists within the input grid, surrounded by background.
    properties:
      - colors: [7, 6, 8, 4] # Orange, Magenta, Azure, Yellow
      - shape: Irregular, but contained within a larger rectangular region.
  - type: transformation
    description: Extraction of a 3x3 subgrid.
    operation: Extract subgrid corresponding to top-left portion of the colored object.
    constraints:
      - Output grid contains only non-zero pixels from the original.
      - original color values retained
```


**Natural Language Program:**

1.  **Identify the Object:** Locate the bounding box of the contiguous non-zero pixels (the colored shape) within the input grid.
2.  **Locate top-left corner**: find the row and column of the top-left corner of the central object.
3.  **Extract Subgrid:** Extract a 3x3 subgrid from the input grid, starting from the top-left corner of the central object defined in the previous step.
4.  **Output:** The extracted 3x3 subgrid is the output.


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
