# 868de0fa • 026 • example_5 • investigate_coder

---

## Example 5

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x960 at 0x70FFF0F743A0>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0
0 1 7 7 7 7 7 1 0 0 0 0 0 0 0
0 1 7 7 7 7 7 1 0 0 0 0 0 0 0
0 1 7 7 7 7 7 1 0 0 0 0 0 0 0
0 1 7 7 7 7 7 1 0 0 0 0 0 0 0
0 1 7 7 7 7 7 1 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 1 2 2 2 2 1 0 0 0
0 0 0 0 0 0 1 2 2 2 2 1 0 0 0
0 0 0 0 0 0 1 2 2 2 2 1 0 0 0
0 0 0 0 0 0 1 2 2 2 2 1 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x960 at 0x70FFF4B4B190>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves two 15x15 grids. The input grid contains two distinct objects, both composed of blue (1) and white (0) pixels. The first object appears in the top half, and the second in the bottom half of the grid. The objects are rectangular outlines filled with white, except for the outer edges which are blue. The output grid maintains the structure of the blue outlines, while the insides get different solid color fillings. The top outline is filled orange(7), the bottom filled with red(2)

**YAML Block - Facts:**


```yaml
objects:
  - id: shape1
    type: rectangle
    outline_color: blue (1)
    fill_color_input: white (0)
    fill_color_output: orange (7)
    position: top_half
    outline_thickness: 1

  - id: shape2
    type: rectangle
    outline_color: blue (1)
    fill_color_input: white (0)
    fill_color_output: red (2)
    position: bottom_half
    outline_thickness: 1

transformations:
  - object: shape1
    action: fill_inside
    parameter: orange (7)

  - object: shape2
    action: fill_inside
    parameter: red (2)

relationships:
  - type: positional
    object1: shape1
    object2: shape2
    relation: shape1 is above shape2

```


**Natural Language Program:**

1.  **Identify Rectangles:** Locate all rectangular shapes within the input grid. Rectangles are defined by a continuous blue (1) outline, one pixel thick, enclosing an area of white (0) pixels.

2.  **Determine Position:** Classify the identified rectangles based on their vertical position within the grid. Rectangles in the top half are considered "top," while those in the bottom half are considered "bottom."

3. **Fill Top Rectangle:** For any rectangle in the "top" half, change all pixels within its blue outline to orange (7).

4.  **Fill Bottom Rectangle:** For any rectangle in the "bottom" half, change all the pixels within its blue outline to red (2).

5. **Preserve outline**: Keep the outline blue (1)

6.  **Output:** Present the modified grid as the output.

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
