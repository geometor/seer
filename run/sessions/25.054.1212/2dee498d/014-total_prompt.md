# 2dee498d • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
2 1 2 1 2 1
2 3 2 3 2 3
```

<PIL.Image.Image image mode=RGB size=384x128 at 0x7BFC47F939A0>

**output:**
```
2 1
2 3
```

<PIL.Image.Image image mode=RGB size=128x128 at 0x7BFC47F93CA0>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a transformation of a 2D grid of colored pixels. The input grid appears to be a repeating pattern of colored squares, and the output grid seems to be a compressed or summarized version of the input. The colors are represented by single digits (1, 2, and 3), which correspond to blue, red, and green, respectively. The input grid has dimensions 2x6, while the output grid has dimensions 2x2. The key seems to lie in recognizing a repeating sub-pattern within the input.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions: [rows, columns]
      cells:
        type: pixel
        properties:
          color: integer (1-9)
    relationships:
      - type: contains
        target: cell

  - type: pattern
    properties:
      dimensions: [rows, columns]
      elements:
        type: pixel array
        properties:
           color: integer

actions:
  - type: identify_pattern
    input: grid
    output: pattern

  - type: compress_grid
    input: [grid, pattern]
    output: grid
    description: Reduces grid by replacing pattern instances with a single instance.

relationships:
  - type: repeating
    subject: pattern
    object: grid

```


**Natural Language Program:**

1. **Identify Repeating Pattern:** Examine the input grid to find the smallest repeating rectangular sub-grid. In this case, the repeating pattern is a 2x1 grid (a vertical pair of pixels). The pattern is `[2, 1]` on top row and `[2, 3]` on the bottom row.

2. **Compress Grid:** The input is the repeating 2x1 subgrids and output is the first instance of the subgrids. The entire input grid consists of repetitions of this basic 2x1 pattern, extract the first occurance of the repeating pattern.

3. **Output extraction:**  The program outputs a new grid comprised of the representative pattern.

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
