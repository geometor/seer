# AboveBelow9 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 0 7 7 7 7 7 7 0 0 0 0 0
0 0 7 7 7 0 0 0 0 0 0 0 0 0 0
0 0 7 0 0 0 0 0 0 0 0 0 0 0 0
0 0 7 0 0 0 0 0 0 0 0 0 0 0 0
0 0 7 7 7 7 0 0 0 0 0 0 0 0 0
0 0 0 0 0 7 0 0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
0 0 0 7 7 7 0 0 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 0 0 0 0 0 0 0
0 0 0 7 7 7 7 7 7 7 0 0 0 0 0
0 0 0 0 0 0 0 0 0 7 0 0 0 0 0
0 0 0 0 0 0 7 7 7 7 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x832 at 0x7995F8563CD0>

**output:**
```
0 0 0 0 7 7 7 7 7 7 0 0 0 0 0
0 0 7 7 7 0 0 0 0 0 0 0 0 0 0
0 0 7 0 0 0 0 0 0 0 0 0 0 0 0
0 0 7 0 0 0 0 0 0 0 0 0 0 0 0
0 0 7 7 7 7 0 0 0 0 0 0 0 0 0
0 0 0 0 0 7 0 0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x832 at 0x7995F8FEF670>
Okay, here's my analysis of the provided example, focusing on perception, object identification, and the transformation rule.

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors observed are orange (7), yellow (4), and white (0). The input grid contains distinct shapes formed by orange and yellow pixels, while the output grid seems to simplify or eliminate some of these shapes. The most notable change is the complete removal of the orange (7) shapes below the yellow (4) line.

**YAML Block (Facts):**


```yaml
objects:
  - id: orange_shape_1
    color: orange (7)
    type: irregular shape
    position: top half of the grid
    properties:
      - extends_horizontally
      - has_vertical_components
  - id: orange_shape_2
    color: orange (7)
    type: irregular shape
    position: bottom half of the grid, below yellow line
    properties:
        - extends_horizontally
        - has_vertical_components
  - id: yellow_line
    color: yellow (4)
    type: horizontal line
    position: middle of the grid
    properties:
      - continuous
      - spans_entire_width

actions:
  - type: removal
    target: orange_shape_2
    condition: "object is below yellow_line"

relationships:
  - yellow_line: "acts as a boundary or filter"
  - orange_shape_1: "unaffected by the transformation"
  - orange_shape_2: "removed based on position relative to yellow_line"

```


**Natural Language Program:**

1.  **Identify Objects:** Locate all contiguous blocks of orange (7) pixels and the single horizontal line of yellow (4) pixels.
2.  **Conditional Removal:** Remove all orange shapes that are located *below* the yellow line.
3.  **Preserve:** Keep the yellow line and any orange shapes located *above* the yellow line unchanged.
4.  **Output:** The resulting grid contains only the yellow line and the orange shapes that were originally above it.

In simpler terms: The transformation removes all orange shapes that appear below the horizontal yellow line, leaving everything else unchanged.

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
