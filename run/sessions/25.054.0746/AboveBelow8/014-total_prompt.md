# AboveBelow8 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 3 8 8 8 3 3 3 3 0
0 3 3 3 8 3 3 3 3 0
0 3 8 8 8 3 3 3 3 0
0 3 8 3 3 3 3 3 3 0
0 3 8 3 3 3 3 3 3 0
0 1 8 8 1 1 1 1 1 0
0 1 1 8 1 1 1 1 1 0
0 1 1 8 8 8 8 1 1 0
0 1 1 1 1 1 8 1 1 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x704 at 0x7995F85FB370>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 8 8 0 0 0 0 0 0
0 0 0 8 0 0 0 0 0 0
0 0 0 8 8 8 8 0 0 0
0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x704 at 0x7995F8FEEC50>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors observed are white (0), green (3), azure (8), and blue (1). The output grid seems to be a simplified version of the input, retaining only the azure (8) pixels and setting all others to white (0).  The shapes and relative positions of the azure regions appear to be preserved, but the surrounding context (the green and blue regions) are removed.

**YAML Fact Block:**


```yaml
facts:
  - observation: "Input grid contains pixels of colors 0, 1, 3, and 8."
  - observation: "Output grid contains pixels of colors 0 and 8 only."
  - object: "Azure (8) regions"
    properties:
      - "Shape is preserved in the output."
      - "Position relative to other azure regions is preserved."
  - object: "Non-azure regions (colors 1, 3)"
    properties:
      - "Transformed to white (0) in the output."
  - action: "Color replacement"
    details: "All non-azure pixels are changed to white."
  - relationship: "Azure pixels maintain their original positions."
```


**Natural Language Program:**

1.  **Identify** all pixels in the input grid that have the color azure (value 8).
2.  **Create** a new grid of the same dimensions as the input, initially filled entirely with white pixels (value 0).
3.  **Copy** the azure (8) pixels from the input grid to the corresponding positions in the output grid.
4.  **Leave** all other pixels in the output grid as white (0).

In simpler terms, the transformation filters out all colors except azure, keeping the azure pixels in their original positions and replacing everything else with white.

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
