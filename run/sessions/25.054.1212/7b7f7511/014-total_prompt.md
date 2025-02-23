# 7b7f7511 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
2 3
3 2
4 4
2 3
3 2
4 4
```

<PIL.Image.Image image mode=RGB size=128x384 at 0x7BFC47578520>

**output:**
```
2 3
3 2
4 4
```

<PIL.Image.Image image mode=RGB size=128x192 at 0x7BFC4757A3E0>
Okay, here's my analysis of the provided example, focusing on perception, structured observations, and a natural language program describing the transformation.

**Perception of Elements:**

*   **Input:** A rectangular grid of colored pixels. The colors correspond to the digits 2 (red), 3 (green), and 4 (yellow). The input grid is 6 rows by 2 columns.
*   **Output:** A rectangular grid of colored pixels, also with colors 2, 3, and 4. The output grid is 3 rows by 2 columns.
*   **Relationship:** The output appears to be a vertically cropped version of the input. Specifically, the top half of the input grid.

**YAML Block (Facts):**


```yaml
objects:
  - name: input_grid
    type: grid
    properties:
      rows: 6
      columns: 2
      colors: [2, 3, 4]
  - name: output_grid
    type: grid
    properties:
      rows: 3
      columns: 2
      colors: [2, 3, 4]

actions:
  - name: crop
    agent: system
    input: input_grid
    parameters:
        row_start: 0
        row_end: 3 # input_grid.rows / 2
        col_start: 0
        col_end: 2

relationships:
   - subject: output_grid
     relation: is_cropped_version_of
     object: input_grid
     properties:
        crop_region: top_half
```


**Natural Language Program:**

The program takes the input grid and crops it to produce the output grid. The output grid consists of the top half of the input grid. Specifically, we take all columns, and the rows from the start index (0) up to, but not including, the row at the middle of the height of the input (input rows / 2).

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
