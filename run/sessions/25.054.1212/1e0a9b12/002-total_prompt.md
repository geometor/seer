# 1e0a9b12 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7BFC475A3400>

**output:**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7BFC475A3340>
Okay, here's my analysis of the provided example:

**Perception of Elements:**

The task involves a 4x4 grid of pixels, each with a numerical value representing a color. The transformation seems to rearrange these pixels based on their original positions and values.  Non-zero pixels appear to be the primary focus of the transformation. The zero-value pixels (white) seem to act like a background or empty space.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    dimensions: 4x4
    elements: pixels
    properties:
      - name: value
        type: integer
        range: 0-9
      - name: color
        type: categorical
        mapping: {0: white, 1: blue, 2: red, 3: green, 4: yellow, 5: gray, 6: magenta, 7: orange, 8: azure, 9: maroon}
      - name: position
        type: coordinate
        format: (row, column)

actions:
  - name: move_pixel
    description: Changes the position of a pixel within the grid.
    parameters:
      - name: source
        type: coordinate
      - name: destination
        type: coordinate

relationships:
  - type: spatial
    description: Non-zero pixels are moved to the bottom rows, preserving their relative order from left to right and top to bottom in the input.

```


**Natural Language Program:**

1.  **Identify non-zero pixels:** Find all pixels in the input grid with values other than 0.
2.  **Preserve Order:** Maintain the original order of these non-zero pixels as they appear from left-to-right, top-to-bottom in the input.
3.  **Move to Bottom:** Move the identified non-zero pixels to the bottom-most available rows of the output grid. Fill the rows from left to right.
4. **Fill Remaining:** All other cells in output grid, not occupied are filled with 0.

In summary, the rule extracts all non-zero pixels, preserves original order, and places them at the bottom of the grid.

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
