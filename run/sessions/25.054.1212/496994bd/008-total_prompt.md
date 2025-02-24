# 496994bd • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
2 2 2 2 2
8 8 8 8 8
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=320x640 at 0x7BFC44365E40>

**output:**
```
2 2 2 2 2
8 8 8 8 8
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
8 8 8 8 8
2 2 2 2 2
```

<PIL.Image.Image image mode=RGB size=320x640 at 0x7BFC443EE290>
Okay, here's my analysis of the provided example, focusing on perception, structured documentation, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors involved are red (2), azure (8), and white (0). The input and output grids have the same dimensions (10x5). The transformation seems to involve some form of mirroring or reflection, specifically affecting the azure (8) and red (2) rows, while leaving the white (0) rows unchanged.

**YAML Fact Block:**


```yaml
objects:
  - type: grid
    dimensions: 10x5
    elements: pixels
    properties:
      - color:
        values: [0, 2, 8]  # white, red, azure
        mapping:
          0: white
          2: red
          8: azure

  - type: row
    properties:
      - color:
        values: [0,2,8]

actions:
    - name: reflection # could be mirroring or translation
    - agent: rows (certain color only)
    - target: vertical axis (appears to reflect about center)

relationships:
  - type: spatial
    description: rows stacked vertically

  - type: transformation
    desciption: input rows of 8 and 2 are transformed to output rows of 8 and 2, reordered.
```


**Natural Language Program:**

1.  **Identify Key Rows:** Locate the rows containing only the color azure (8) and the rows containing only the color red (2) within the input grid.
2.  **Ignore other rows:** The rows containing only white (0) do not change their vertical position.
3.  **Reverse Order** Reverse the vertical order of the azure (8) and red (2) rows. Place the azure (8) at the original red(2) row position, and the red (2) at the original azure (8) location.
4.  **Output.** Combine the unchanged white(0) rows with the transformed azure(8) and red(2) rows at their new locations. The result is the output.

In essence, the transformation swaps the positions of the "red" and "azure" rows, while leaving the "white" rows untouched, effectively performing a kind of selective vertical reflection around the center of the grid.

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
