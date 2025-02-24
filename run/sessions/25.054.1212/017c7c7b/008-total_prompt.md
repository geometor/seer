# 017c7c7b • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
```

<PIL.Image.Image image mode=RGB size=192x384 at 0x7BFC48909C30>

**output:**
```
0 2 0
2 0 2
0 2 0
2 0 2
0 2 0
2 0 2
0 2 0
2 0 2
0 2 0
```

<PIL.Image.Image image mode=RGB size=192x576 at 0x7BFC4890A0E0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a transformation of a grid of colored pixels. The input grid consists of alternating white (0) and blue (1) pixels in a checkerboard pattern. The output grid seems to replace the blue pixels with red (2) pixels, while keeping the white pixels unchanged. The output grid also has different dimensions and the pattern repeats one extra time vertically.

**YAML Fact Block:**


```yaml
facts:
  - object: input_grid
    type: grid
    properties:
      - colors: [white, blue]
      - pattern: checkerboard
      - dimensions: [6, 3]
  - object: output_grid
    type: grid
    properties:
      - colors: [white, red]
      - pattern: checkerboard
      - dimensions: [9, 3]
  - action: color_substitution
    input: blue
    output: red
  - action: repeat_pattern
    axis: vertical
    times: input rows / output rows

```


**Natural Language Program:**

1.  **Identify** the checkerboard pattern in the input grid, noting the alternating white (0) and blue (1) pixels.
2.  **Substitute** all blue (1) pixels with red (2) pixels.
3  **Repeat** the original vertical pattern extra time (input grid is length 6 and output grid is length 9 so it is repeated 9/6 = 1.5 times - or one extra half of it's length).
4.  **Maintain** the white (0) pixels unchanged.
5. **Output**: New grid


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
