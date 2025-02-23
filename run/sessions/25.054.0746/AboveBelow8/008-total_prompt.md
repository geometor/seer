# AboveBelow8 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
3 3 3 3 8 8 8 8 8 8 3
3 3 3 3 8 3 3 3 3 3 3
2 2 2 2 8 8 8 8 2 2 2
2 2 2 2 2 2 2 8 2 2 2
7 7 7 7 7 7 7 8 7 7 7
7 7 7 7 7 7 7 8 7 7 7
7 7 7 7 8 8 8 8 7 7 7
9 9 9 8 8 9 9 9 9 9 9
1 1 1 8 1 1 1 1 1 1 1
1 1 1 8 8 1 1 1 1 1 1
1 1 1 1 8 8 8 1 1 1 1
```

<PIL.Image.Image image mode=RGB size=704x704 at 0x7995F901BB20>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 8 8 8 8 0 0 0
0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 8 8 8 8 0 0 0
0 0 0 8 8 0 0 0 0 0 0
0 0 0 8 0 0 0 0 0 0 0
0 0 0 8 8 0 0 0 0 0 0
0 0 0 0 8 8 8 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x704 at 0x7995F8561180>
Okay, here's a breakdown of my observations, documented facts, and a natural language program describing the transformation:

**Perception of Elements:**

The task involves a grid of colored pixels. The primary focus seems to be on isolating and highlighting a specific color (azure, represented by the number 8) within the input grid. All other colors are replaced with white (represented by 0) in the output grid, with all color beside 8 set to 0. The shape formed by the azure pixels appears to be maintained.

**YAML Block (Facts):**


```yaml
facts:
  - object: input_grid
    type: grid
    properties:
      - colors: [3, 2, 7, 9, 1, 8]  # All colors present in the input
      - dimensions: 11x11  # height x width

  - object: output_grid
    type: grid
    properties:
      - colors: [0, 8]  # Colors present in the output
      - dimensions: 11x11

  - action: color_filtering
    description: Isolates a specific color (8) and replaces others with 0.
    input: input_grid
    output: output_grid
    parameters:
        target_color: 8

  - object: target_color
    value: 8

  - relationship:
      type:  color map
      description: 8 is azure, and other colors are not relevant for the output
```


**Natural Language Program:**

1.  **Identify the target color:** The target color for this transformation is azure (represented by the numerical value 8).
2.  **Iterate through the input grid:** Examine each pixel in the input grid.
3.  **Check pixel color:** For each pixel, compare its color value to the target color (8).
4.  **Conditional replacement:**
    *   If the pixel's color is equal to 8 (azure), maintain the pixel's value.
    *   If the pixel's color is not equal to 8, replace the pixel value by 0.
5. **Construct output:** Output is the same dimension as input.

Essentially, the program acts as a color filter, keeping only the azure pixels and setting all other pixels to white.

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
