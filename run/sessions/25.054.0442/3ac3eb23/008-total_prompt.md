# 3ac3eb23 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 4 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x384 at 0x7AA3AFEF69E0>

**output:**
```
0 4 0 0 0 0 0
4 0 4 0 0 0 0
0 4 0 0 0 0 0
4 0 4 0 0 0 0
0 4 0 0 0 0 0
4 0 4 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x384 at 0x7AA3AFE5F6D0>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves 2D grids (matrices) where each cell contains a single digit integer, representing a color. The input grid contains mostly `0` (white) with a single `4` (yellow). The output grid is an alteration of the input grid where the initial yellow pixel seems to have "activated" a pattern, a vertical oscillation of yellow pixels in alternating columns.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      - dimensions: 2D array (rows x columns)
      - cells: contain integer values (0-9) representing colors
      - color_map:
          0: white
          4: yellow

  - type: pixel
    properties:
      - color: integer value
      - location: (row, column) coordinates within the grid

actions:
  - name: activate_pattern
    description: A single yellow pixel triggers a pattern change.
    details: >
        The yellow pixel appears to initiate an alternating pattern. 
        The pattern involves copying of the yellow pixel vertically in the column to the left and the column containing the original yellow pixel.

relationships:
  - type: spatial
    description: Pixels are arranged in a 2D grid.
    details:  Adjacency (up, down, left, right) is key to the transformation pattern.

```


**Natural Language Program:**

1.  **Locate the Trigger:** Find the single yellow (4) pixel in the input grid.
2.  **Vertical Oscillation:** In the original trigger's column and a column directly to its left, duplicate that pixel value vertically.
3. **Alternation** Yellow pixels now fill alternating rows in these columns.

In essence, the transformation identifies a specific 'trigger' pixel and uses its location to generate a simple, vertically alternating pattern of the same color in its containing and an adjacent column.

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
