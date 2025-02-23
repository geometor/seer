# AboveBelow7 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 4 4 4 4 4 4 4 4 0 0 0
0 0 0 0 3 3 3 3 3 3 3 3 0 0 0
0 0 0 0 3 0 0 0 0 0 0 3 0 0 0
0 0 0 0 3 0 0 0 0 0 0 3 0 0 0
0 0 0 0 3 0 0 0 0 0 0 3 0 0 0
0 0 0 0 3 3 3 3 3 3 3 3 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x640 at 0x7995F85D2560>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 3 3 3 3 3 3 3 0 0 0
0 0 0 0 3 0 0 0 0 0 0 3 0 0 0
0 0 0 0 3 0 0 0 0 0 0 3 0 0 0
0 0 0 0 3 0 0 0 0 0 0 3 0 0 0
0 0 0 0 3 3 3 3 3 3 3 3 0 0 0
0 0 0 0 4 4 4 4 4 4 4 4 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x640 at 0x7995F901BF40>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors observed are white (0), yellow (4), and green (3). The input grid contains a rectangular block of yellow pixels at the top and a U-shaped structure of green pixels below it. The output grid swaps the positions of the yellow rectangle and the green structure, maintaining their original shapes. The white background (0) remains unchanged.

**YAML Block (Facts):**


```yaml
objects:
  - id: yellow_rectangle
    type: rectangle
    color: yellow (4)
    initial_position: top
    final_position: bottom
    shape_properties:
      width: 8 pixels
      height: 1 pixel

  - id: green_structure
    type: U-shape
    color: green (3)
    initial_position: middle/bottom
    final_position: middle/top
    shape_properties:
      width: 8 pixels
      height: 5 pixels (overall)

  - id: background
    type: grid_background
    color: white (0)
    initial_position: all
    final_position: all

actions:
  - type: swap_positions
    objects: [yellow_rectangle, green_structure]
    description: "The yellow rectangle and the green U-shape exchange their vertical positions."

relationships:
  - type: spatial
    relation: above/below
    objects: [yellow_rectangle, green_structure]
    description: "Initially, the yellow rectangle is above the green structure. Finally, the green is on top and the yellow at the bottom."
```


**Natural Language Program:**

1.  Identify a rectangular block of yellow (4) pixels.
2.  Identify a U-shaped structure of green (3) pixels.
3.  Swap the vertical positions of the yellow rectangle and the green U-shape within the grid. The shapes should be preserved.
4.  Keep all white background (0) pixels unchanged.

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
