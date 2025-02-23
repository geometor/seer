# AboveBelow10 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 0 0 0 0 0 3 0 0 0
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 3 0 0 0 0 0
0 0 0 0 0 3 0 0 0 0 0 0
0 0 0 0 3 0 0 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 0 0 0 0 0
0 3 0 0 0 0 0 0 0 0 0 0
3 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x7995F90382E0>

**output:**
```
0 0 0 0 0 0 0 0 3 3 3 3
0 0 0 0 0 0 0 3 3 3 3 3
0 0 0 0 0 0 3 3 3 3 3 3
0 0 0 0 0 3 3 3 3 3 3 3
0 0 0 0 3 3 3 3 3 3 3 3
0 0 0 3 3 3 3 3 3 3 3 3
0 0 3 3 3 3 3 3 3 3 3 3
0 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3 3
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x7995F901BF70>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid (likely 2D array) of numerical values, where `0` represents white and `3` represents green. The transformation seems to involve expanding the green pixels (`3`) downwards and to the right. The expansion appears to fill the entire remaining area of the grid, bounded by its original diagonal line.

**YAML Fact Documentation:**


```yaml
facts:
  - object: grid
    type: 2D array
    elements:
      - value: 0
        color: white
      - value: 3
        color: green
  - observation: Green pixels form a diagonal line from top-right to bottom-left.
  - transformation: Green pixels expand.
  - expansion_direction: Downwards and to the right.
  - expansion_limit:  Original diagonal forms a boundary, and the expansion continues to the grid edges.
```


**Natural Language Program:**

1.  **Identify:** Locate all green pixels (value `3`) in the input grid.
2.  **Propagate:** For each green pixel, change all pixels below it and all the pixels to its right, including itself, to green (value `3`). The green pixels will expand to the lower and right boundaries of the grid.

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
