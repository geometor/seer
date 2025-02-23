# ff805c23 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 3 3 3 3 0 0 2 2 2 0 0 0 0 2 2 2 0 1 1 1 1 1 0
3 3 3 3 3 0 2 2 0 2 2 0 0 2 2 0 2 2 1 1 1 1 1 3
3 3 3 0 0 3 2 0 0 2 0 0 0 0 2 0 0 2 1 1 1 1 1 3
3 3 0 3 3 3 2 2 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 3
3 3 0 3 3 3 0 2 0 2 2 2 2 2 2 0 2 0 1 1 1 1 1 3
0 0 3 3 3 3 0 0 0 2 2 2 2 2 2 0 0 0 3 3 3 3 0 0
0 2 2 2 0 0 2 0 0 2 2 2 2 2 2 0 0 2 0 0 2 2 2 0
2 2 0 2 2 0 0 2 2 0 2 2 2 2 0 2 2 0 0 2 2 0 2 2
2 0 0 2 0 0 0 2 2 0 0 2 2 0 0 2 2 0 0 0 2 0 0 2
2 2 2 2 2 2 2 0 0 2 2 2 2 2 2 0 0 2 2 2 2 2 2 2
0 2 0 2 2 2 2 2 0 2 0 2 2 0 2 0 2 2 2 2 2 0 2 0
0 0 0 2 2 2 2 2 2 2 2 0 0 2 2 2 2 2 2 2 2 0 0 0
0 0 0 2 2 2 2 2 2 2 2 0 0 2 2 2 2 2 2 2 2 0 0 0
0 2 0 2 2 2 2 2 0 2 0 2 2 0 2 0 2 2 2 2 2 0 2 0
2 2 2 2 2 2 2 0 0 2 2 2 2 2 2 0 0 2 2 2 2 2 2 2
2 0 0 2 0 0 0 2 2 0 0 2 2 0 0 2 2 0 0 0 2 0 0 2
2 2 0 2 2 0 0 2 2 0 2 2 2 2 0 2 2 0 0 2 2 0 2 2
0 2 2 2 0 0 2 0 0 2 2 2 2 2 2 0 0 2 0 0 2 2 2 0
0 0 3 3 3 3 0 0 0 2 2 2 2 2 2 0 0 0 3 3 3 3 0 0
3 3 0 3 3 3 0 2 0 2 2 2 2 2 2 0 2 0 3 3 3 0 3 3
3 3 0 3 3 3 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 0 3 3
3 3 3 0 0 3 2 0 0 2 0 0 0 0 2 0 0 2 3 0 0 3 3 3
3 3 3 3 3 0 2 2 0 2 2 0 0 2 2 0 2 2 0 3 3 3 3 3
0 3 3 3 3 0 0 2 2 2 0 0 0 0 2 2 2 0 0 3 3 3 3 0
```

<PIL.Image.Image image mode=RGB size=1536x1536 at 0x70FFF01B0700>

**output:**
```
0 3 3 3 3
0 3 3 3 3
3 0 0 3 3
3 3 3 0 3
3 3 3 0 3
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x70FFF01B3130>
Okay, here's my analysis of the example input-output pair, including my perception of the elements, a YAML block documenting facts, and a natural language program describing the transformation.

**Perception of Elements:**

The input is a large, complex grid composed of multiple colors (represented by digits 0-9). The output is a significantly smaller grid, seemingly derived from the upper-left corner of the input grid, specifically using only green (3) and white(0) values. The input contains red(2), blue(1), and the output doesn't. The output grid appears to be a sub-grid of the input grid.

**YAML Block (Facts):**


```yaml
objects:
  - name: input_grid
    type: 2D array
    dimensions: [24, 26]
    elements: [0, 1, 2, 3] # Values represent colors
    properties:
      - contains_subgrids: True

  - name: output_grid
    type: 2D array
    dimensions: [5, 5]
    elements: [0, 3] # Values represent colors
    properties:
      - is_subgrid: True
      - location: top-left corner of input_grid

relationships:
  - type: subgrid_of
    subject: output_grid
    object: input_grid

actions:
  - type: extraction
    description: Extract a sub-grid from the input_grid.
    parameters:
      - start_row: 0
      - end_row: 4
      - start_col: 0
      - end_col: 4
  - type: filter
    description: filtering colors to only show 0 and 3
```


**Natural Language Program:**

1.  **Identify the Input:**  The input is a 24x26 grid of colored pixels.
2.  **Locate Sub-grid:** Identify the 5x5 sub-grid located at the top-left corner of the input grid, starting at row 0, column 0 and extending to row 4, column 4.
3. **Extract the subgrid**: extract that area.
4.  **Filter Colors:** Remove all colors that are not white(0) or green(3). The output will be this new grid.

In essence, the transformation extracts a 5x5 sub-grid from the top-left corner of the input grid, and keeps pixels of color white and green, which becomes the output.

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
