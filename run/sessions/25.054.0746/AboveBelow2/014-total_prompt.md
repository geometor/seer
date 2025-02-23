# AboveBelow2 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 8 8 8 0
0 0 0 8 8 8 0
0 0 0 8 8 8 0
0 0 0 0 0 0 0
0 0 7 7 7 0 0
0 0 7 7 7 0 0
0 0 7 7 7 0 0
0 0 0 0 0 0 0
7 7 7 7 0 8 8
7 7 7 7 0 8 8
0 0 0 0 0 0 0
0 0 0 0 3 3 3
0 0 0 0 3 3 3
0 0 0 0 3 3 3
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x960 at 0x7995F90382E0>

**output:**
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 3 3 3
0 0 0 0 3 3 3
0 0 0 0 3 3 3
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x960 at 0x7995F85D1840>
Okay, here's my analysis of the example input-output pair, broken down into perceptions, a YAML fact block, and a natural language program.

**Perception of Elements:**

The primary element is a grid of colored pixels.  The input grid contains several distinct colored regions (azure, orange, green, and white/background). The output grid seems to retain only the green region, with all other pixels becoming white (value 0). The position and shape of the green region appears unchanged.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: Input and output are 2D grids of pixels.
  - observation: input_colors
    values: [0, 8, 7, 3]  # white, azure, orange, green
    description: The input grid contains pixels of these colors.
  - observation: output_colors
    values: [0, 3] # white, green
    description: The output grid contains pixels of these colors.
  - object: green_region
    color: 3  # green
    attribute: shape
      value: rectangle
    attribute: position
      value: unchanged #relative to input
    description: A rectangular region of green pixels.
  - object: other_regions
    colors: [8, 7, 0]
    attribute: transformation
       value: all pixels to 0
    description: All regions of colors are replaced with white.

  - action: filtering
    description:  Pixels are retained or changed based on their color.
  - rule: retain_color
    color: 3 # Green
    description:  Pixels with the value 3 are retained.
  - rule: remove_color
    colors: [0,7,8] #white, orange and azure
    description: Pixels with colors other than 3 become 0.

```


**Natural Language Program:**

1.  **Identify** all pixels in the input grid.
2.  **Filter** the pixels based on their color:
    *   If a pixel's color is green (value 3), retain its value in the output grid at the same position.
    *   If a pixel's color is not green (i.e., white, azure, or orange), change its value to white (0) in the output grid at the same position.
3.  The output grid is the result of this filtering process.

In essence, the transformation is a color-based filter that preserves only green pixels and sets all other pixels to white.

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
