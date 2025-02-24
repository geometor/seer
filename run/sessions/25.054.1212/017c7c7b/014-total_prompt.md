# 017c7c7b • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 1 0
1 1 0
0 1 0
0 1 0
1 1 0
0 1 0
```

<PIL.Image.Image image mode=RGB size=192x384 at 0x7BFC4890A0E0>

**output:**
```
0 2 0
2 2 0
0 2 0
0 2 0
2 2 0
0 2 0
0 2 0
2 2 0
0 2 0
```

<PIL.Image.Image image mode=RGB size=192x576 at 0x7BFC48909EA0>
Okay, here's my analysis of the example input-output pair:

**Perception of Elements:**

The task involves a grid of pixels, each with a single digit representing a color. The input grid appears to be transformed into an output grid of the same dimensions, with some of the colors changed. The key difference seems to be the replacement of '1' (blue) pixels with '2' (red) pixels. The '0' (white) pixels remain unchanged. The output grid is two rows taller than the input.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions:
        input: [6, 3]
        output: [9, 3]
      pixels:
        - value: 0
          color: white
        - value: 1
          color: blue
        - value: 2
          color: red

actions:
  - type: replacement
    description: Replace blue pixels with red pixels.
  - type: addition
    description: add rows of the established pattern

relationships:
  - type: spatial
    description: Pixels are arranged in a 2D grid.
  - type: transformation
    description: Input grid is transformed into the output grid by changing colors and adding rows.
```


**Natural Language Program:**

1.  **Identify:** Locate all pixels in the input grid with the value '1' (blue).
2.  **Replace:** Change the value of these identified pixels to '2' (red).
3. **Extend**: add three rows to the bottom, copying the row above in each case.
4.  **Preserve:** All other pixels (value '0', white) remain unchanged.

Essentially, the transformation rule is to replace all blue pixels with red pixels and add three rows.

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
