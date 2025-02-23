# 1cf80156 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0 0 0
0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 2 2 2 0 0 0 0 0 0
0 0 0 2 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x640 at 0x795F858DE230>

**output:**
```
0 2 2 2
0 0 2 0
2 2 2 0
2 0 2 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x795F84345CC0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

*   The input is a large grid (12x10) filled mostly with white pixels (0) and a small "L" shaped object made of red pixels (2).
*   The output is a smaller grid (4x4) that seems to be a condensed representation of the input, focusing on the red pixels. The arrangement of the red pixels in the output matches part of red area in the input.
* The output isolates and rotates a part of input.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: input grid
    dimensions: 12x10
    elements:
      - color: white
        value: 0
        dominant: true
      - color: red
        value: 2
        dominant: false
        shape: L

  - type: grid
    description: output grid
    dimensions: 4x4
    elements:
      - color: white
        value: 0
        dominant: false
      - color: red
        value: 2
        dominant: true
        shape: L_rotated
  - observation: The output grid contains a cropped and rotated section of input grid.
  - observation: The red pixels are the main content.
  - action: Extract object
  - action: rotate
```


**Natural Language Program:**

1.  **Identify:** Find the bounding box of the red colored object within the input grid.
2.  **Crop:** Extract this bounding box, from input.
3. **Rotate:** rotate cropped part clockwise by 90 degrees.
4.  **Output:** Present the rotated and cropped section.

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
