# AboveBelow6 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 4 4 4 4 4 4 4 4 0
0 4 4 4 4 4 4 4 4 0
0 4 4 4 4 4 4 4 4 0
0 2 2 2 2 2 2 2 2 0
0 4 4 4 4 4 4 4 4 0
0 4 4 4 4 4 4 4 4 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x7995F90382E0>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 4 4 4 4 4 4 4 4 0
0 4 4 4 4 4 4 4 4 0
0 4 4 4 4 4 4 4 4 0
0 2 2 2 2 2 2 2 2 0
0 2 2 2 2 2 2 2 2 0
0 2 2 2 2 2 2 2 2 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x512 at 0x7995F85D2170>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors involved seem to be yellow (4), red (2), and white (0). The input grid has a horizontal band of red pixels surrounded by yellow pixels, all bordered by white pixels. The output grid maintains the red band and expands it downwards, replacing some of the yellow pixels.

**YAML Block (Facts):**


```yaml
objects:
  - name: grid
    type: 2D array
    properties:
      - width: 10
      - height: 8
      - cell_values: [0, 2, 4]
  - name: red_band
    type: rectangle
    properties:
      - color: 2
      - initial_position: row 4
      - initial_height: 1
      - final_position: row 4
      - final_height: 3 # height at output
  - name: yellow_region
    type: rectangle
    properties:
       - color: 4
  - name: white_border
    type: rectangle
    properties:
      -color: 0
relationships:
  - type: surrounds
    subject: white_border
    object: yellow_region, red_band
  - type: contains
    subject: yellow_region
    object: red_band
actions:
  - type: expand_downward
    object: red_band
    parameters:
      - rows_added: 2
```


**Natural Language Program:**

1.  **Identify Objects:** Locate the rectangular band of red (2) pixels. Also, note the surrounding yellow (4) and white (0) areas.
2. **Red Band Expansion**: The transformation rule is to expand the red band downwards. Specifically, copy the existing row of the red band twice, placing the copies immediately below the original red band.
3. **Preservation:** All pixels not modified by the expansion remain the same between the input and output. Thus all the white pixels, and the yellow pixels above the red band remain unchanged. The yellow pixels at the bottom are replaced.


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
