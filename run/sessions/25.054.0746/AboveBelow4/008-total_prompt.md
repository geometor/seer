# AboveBelow4 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 3 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0
6 6 6 6 6 6 6 6 6 6 6 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x576 at 0x7995F9038A00>

**output:**
```
0 0 6 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 6 3 3 0 0
6 6 6 6 6 6 6 6 6 6 6 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 3 3 3 3 3 6
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=768x576 at 0x7995F85FB1C0>
Okay, here's my analysis of the provided example, focusing on perception, object identification, and the transformation rule.

**Perception of Elements:**

The task involves two grids (input and output) of the same dimensions (12x9). The grids contain numerical values representing colors. The primary colors observed are:

*   0 (white)
*   3 (green)
*   6 (magenta)

The transformation seems to involve a subtle change, primarily focused on inserting the color 6 (magenta) adjacent to existing color 3 (green) regions.

**YAML Block (Facts):**


```yaml
objects:
  - id: grid_input
    type: grid
    dimensions: [12, 9]
    elements: [0, 3, 6]

  - id: grid_output
    type: grid
    dimensions: [12, 9]
    elements: [0, 3, 6]

  - id: green_regions
    type: object_group
    color: 3
    grid: grid_input

  - id: magenta_regions
      type: object_group
      color: 6
      grid: grid_input

relations:
  - type: same_dimensions
    objects: [grid_input, grid_output]

  - type: adjacency
    description: "Magenta (6) is inserted next to green (3) in the output grid."
    objects: [green_regions]
```


**Natural Language Program:**

1.  **Identify:** Locate all regions of color 3 (green) in the input grid.
2.  **Insert:** For each green region, examine its immediate horizontal neighbors (left and right). If a neighbor is not already green (3) or magenta(6), and the neighbor is within the grid bounds, place 6 to left or right of the existing green.
3. If color 3 is at the edge, add 6 to only to available side.
4. The central magenta region remains unchanged.

In essence, the transformation adds a magenta (6) pixel adjacent to existing horizontal green regions.


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
