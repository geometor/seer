# 868de0fa • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
1 1 1 1 0 0 0 0 0 0
1 0 0 1 0 0 0 0 0 0
1 0 0 1 0 0 1 1 1 0
1 1 1 1 0 0 1 0 1 0
0 0 0 0 0 0 1 1 1 0
1 1 1 1 1 0 0 0 0 0
1 0 0 0 1 0 0 0 0 0
1 0 0 0 1 0 0 0 0 0
1 0 0 0 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0F9C340>

**output:**
```
1 1 1 1 0 0 0 0 0 0
1 2 2 1 0 0 0 0 0 0
1 2 2 1 0 0 1 1 1 0
1 1 1 1 0 0 1 7 1 0
0 0 0 0 0 0 1 1 1 0
1 1 1 1 1 0 0 0 0 0
1 7 7 7 1 0 0 0 0 0
1 7 7 7 1 0 0 0 0 0
1 7 7 7 1 0 0 0 0 0
1 1 1 1 1 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0ECF7F0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves transforming a grid of numerical values (representing colors) into another grid of the same dimensions. The input grid primarily consists of 0s (white) and 1s (blue).  The output grid introduces new colors: 2 (red) and 7 (orange). The positions of the 0s (white) remain unchanged. The transformation seems to focus on the 1s (blue). It appears that connected regions of 1s are being identified, and some, but not all are changing color.

**YAML Block - Facts:**


```yaml
observations:
  - type: grid
    description: Input and output are grids of the same dimensions.
  - type: values
    description: Input grid contains 0 (white) and 1 (blue).
  - type: values
    description: Output grid contains 0 (white), 1 (blue), 2 (red), and 7 (orange).
  - type: invariance
    description: The positions of 0s (white) are the same in both input and output.
  - type: transformation
    description: Some blue (1) regions change to red (2), some to orange (7), some stay blue (1)
  - type: object
    description: contiguous regions of color
    properties:
      color:
        values: [blue,red, orange]

```


**Natural Language Program:**

1.  **Identify Objects:** Locate all contiguous regions (objects) of 'blue' (1) pixels in the input grid.  Contiguous means connected horizontally or vertically.
2. **Preserve Background:** Maintain all 'white' (0) pixels in their original positions in the output grid.
3.  **Transform Objects:** Iterate through blue regions.
    *   Change the color of the top-left blue object to red (2).
    *   Change the color of a blue object to orange (7) if it forms at least a 3x1 or 1x3 shape with blue (1) pixels.
    * The large blue object on the right-side of the image does not change.


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
