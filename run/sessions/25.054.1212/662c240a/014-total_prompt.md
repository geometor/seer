# 662c240a • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
2 2 2
2 2 3
2 3 3
5 7 7
7 5 5
7 5 5
8 8 1
1 8 1
1 8 1
```

<PIL.Image.Image image mode=RGB size=192x576 at 0x7BFC47F93700>

**output:**
```
8 8 1
1 8 1
1 8 1
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC47F93970>
Okay, here's a breakdown of my observations and proposed transformation rule for the provided example:

**Perception of Elements:**

The task involves a grid of colored pixels. The transformation seems to be a selection or filtering process, where only a specific portion of the input grid is retained in the output. The output grid appears to be the bottom-most, uniquely colored segment of the input.

**YAML Block (Facts):**


```yaml
objects:
  - grid:
      type: 2D array
      elements: colored pixels (integers 0-9)
      properties:
        - height
        - width

observations:
  - input_grid_height: 9
  - input_grid_width: 3
  - output_grid_height: 3
  - output_grid_width: 3
  - output_grid: bottom section of the input grid
  - unique_colors_area: The output section contains colors that do not appear in the upper area of the input.

actions:
    - selection: identify a region based on a property (uniqueness).

relationships:
  - spatial: output is a sub-region of the input (bottom).
  - color_based: the selected region's color composition is a unique set.
```


**Natural Language Program:**

1.  **Identify the bottom-most section of the input grid.** This section is defined as contiguous rows, up to the point where the next upper row contains different colors.
2.  **Output this section.** The output grid has the same dimensions as the bottom area.

In simpler terms, extract the last "unique colored block" of rows from the bottom.

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
