# 496994bd • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
2 2 2
2 2 2
3 3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
```

<PIL.Image.Image image mode=RGB size=192x640 at 0x7BFC44365E40>

**output:**
```
2 2 2
2 2 2
3 3 3
0 0 0
0 0 0
0 0 0
0 0 0
3 3 3
2 2 2
2 2 2
```

<PIL.Image.Image image mode=RGB size=192x640 at 0x7BFC443E3940>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The colors are represented by single-digit integers (0-9). The input grid appears to be transformed into a modified output grid. The primary colors involved seem to be red (2), green (3), and white (0). The input grid has a section of white (0), a section of green (3) and section of red(2). The output is adding at the bottom the mirror of the top two rows.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      - dimensions: 10x3 (input), 10x3 (output)
      - elements: pixels
      - colors: [0, 2, 3]  # white, red, green
    relationships:
        - input_grid: original state
        - output_grid: modified state

actions:
    - type: append rows
    - properties:
      - source : first 3 rows
      - order: inverse or mirrored

```


**Natural Language Program:**

1.  **Identify**: Get the input grid which represents the initial state.
2.  **Observe**: The first two rows are copied.
3. **Invert**: The copied part is inverted.
4. **Append**: The original and inverted sections are combined
    vertically.
5. **Return:** new grid

In summary, The transformation takes the top three rows of the input and mirrors/inverts it, placing the added section it to the bottom of the grid.

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
