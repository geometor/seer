# db93a21d • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 9 9 0 0
0 0 0 0 0 0 9 9 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 9 9 0 0 0 0 0 0 0
0 9 9 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0ECF7F0>

**output:**
```
0 0 0 0 0 3 9 9 3 0
0 0 0 0 0 3 9 9 3 0
0 0 0 0 0 3 3 3 3 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 1 0 0
3 3 3 3 0 0 1 1 0 0
3 9 9 3 0 0 1 1 0 0
3 9 9 3 0 0 1 1 0 0
3 3 3 3 0 0 1 1 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0F776A0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves transforming a grid of colored pixels (represented by digits 0-9) into another grid of the same dimensions. The input grid primarily contains white (0) and maroon (9) pixels, while the output grid introduces green (3) and blue (1) pixels in addition to the original colors. There appears to be a relationship between the placement of maroon pixels in the input and the placement of other colors in the output. Specifically, it seems like maroon regions are being "outlined" or "bordered" by green, and a new blue object is appearing seemingly where no objects were before.

**YAML Fact Block:**


```yaml
facts:
  - subject: input_grid
    description: 10x10 grid of pixels
    properties:
      - color_values: [0, 9]
      - color_names: [white, maroon]
    objects:
      - object_id: maroon_regions
        description: Contiguous blocks of maroon (9) pixels
        properties:
          - shape: variable
          - location: variable

  - subject: output_grid
    description: 10x10 grid of pixels
    properties:
      - color_values: [0, 1, 3, 9]
      - color_names: [white, blue, green, maroon]
    objects:
      - object_id: green_outline
        description: Green (3) pixels surrounding maroon regions
        properties:
          - shape: outline of maroon_regions
          - location: adjacent to maroon_regions
      - object_id: blue_rectangle
        description: a rectangle filled by blue pixels
        properties:
            - shape: rectangle
            - location: seemingly filling whitespace

  - transformation:
    description: Input grid is transformed to output grid.
    rules:
      - rule_1:  Maroon (9) regions in the input are preserved in the output.
      - rule_2:  Green (3) pixels form an outline around the maroon regions.
      - rule_3: A new object of Blue (1) pixels form in area previously defined by white pixels.
```


**Natural Language Program:**

1.  **Preserve Maroon:** Copy all maroon (9) pixels from the input grid to the same positions in the output grid.

2.  **Outline in Green:** For each maroon pixel in the input grid, examine its immediate neighbors (up, down, left, right). If a neighbor is white (0) in the input grid, change that pixel in the output grid to green (3).

3.  **Create blue object:** Starting from the bottom right of the image, identify a rectangular area not occupied by any colored pixels and replace the white pixels with blue (1) pixels.


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
