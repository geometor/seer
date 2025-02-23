# 00d62c1b • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x70FA38657940>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x70FA38657580>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a 2D grid of single-digit integers (0-9), representing colors. The primary element is a cross-shaped object composed of green (3) pixels. The transformation seems to involve identifying specific pixels within this object and changing their color to yellow (4).

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 6x6
      elements: integers (0-9)
      color_map:
        0: white
        3: green
        4: yellow
  - type: object
    properties:
      shape: cross
      color: green
      composition: contiguous pixels of value 3

actions:
  - type: color_change
    properties:
      target: specific pixels within the cross
      initial_color: green
      final_color: yellow
    conditions:
      - target pixels are horizontally and vertically adjacent to a green pixel
      

relationships:
  - type: adjacency
    description: Pixels are considered adjacent horizontally or vertically, not diagonally.
  - type: containment
    description: The cross object is contained within the grid.
```


**Natural Language Program:**

1.  **Identify the Cross:** Locate the cross-shaped object within the input grid. This object is defined as a set of contiguous green (3) pixels forming a cross.
2.  **Locate Interior Pixels:** Examine each cell in the cross.
3. **Transform Interior Pixels:** Find the pixels that are completely surrounded on all four sides (up, down, left, right and not diagnonally) and convert those green (3) pixels into yellow (4) pixels.

In summary, the input cross shape has green color. The center pixels that are horizontally and vertically adjacent to a green pixel are changed to yellow in the output grid.

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
