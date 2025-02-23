# AboveBelow3 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0
0 3 3 3 0 0 0 0
0 0 0 0 0 0 0 0
0 4 4 4 0 0 0 0
0 4 4 4 0 0 0 0
0 4 4 4 0 0 0 0
0 0 0 0 0 3 3 3
0 0 3 3 3 0 0 0
```

<PIL.Image.Image image mode=RGB size=512x512 at 0x7995F8FEF670>

**output:**
```
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 3 3 3 0 0 0 0
0 4 4 4 0 0 0 0
0 4 4 4 0 0 0 0
0 4 4 4 0 0 0 0
0 0 0 0 0 3 3 3
0 0 3 3 3 0 0 0
```

<PIL.Image.Image image mode=RGB size=512x512 at 0x7995F8FEFD00>
Okay, here's a breakdown of my observations and proposed transformation rule for the example provided:

**Perception of Elements:**

*   **Input:** An 8x8 grid of pixels, with values representing colors. There are distinct horizontal lines of green (3) and yellow (4) pixels, with the rest being white (0).
*   **Output:** A very similar 8x8 grid. It seems like a portion of the top green line has been removed.
*  The output image show that the top row of 3s are deleted.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 8x8
      colors: [0, 3, 4]
  - type: horizontal_line
    properties:
      color: 3
      positions: [[1,1],[1,2],[1,3], [6,5],[6,6],[6,7],[7,2],[7,3],[7,4]]
  - type: horizontal_line
    properties:
      color: 4
      positions: [[3,1],[3,2],[3,3],[4,1],[4,2],[4,3],[5,1],[5,2],[5,3]]

actions:
  - type: delete
    target: horizontal_line
    properties:
        color: 3
        row: 1

relationships:
    - lines are on the grid
```


**Natural Language Program:**

1.  **Identify** all horizontal lines of pixels with the color green (value 3).
2.  **Delete** the green horizontal lines on the top.

In simpler terms: Locate the top green line and erase it. Maintain everything else unchanged.

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
