# 54d82841 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0 0 0
0 8 8 8 0 0 0
0 8 0 8 6 6 6
0 0 0 0 6 0 6
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x320 at 0x7BFC47F93880>

**output:**
```
0 0 0 0 0 0 0
0 8 8 8 0 0 0
0 8 0 8 6 6 6
0 0 0 0 6 0 6
0 0 4 0 0 4 0
```

<PIL.Image.Image image mode=RGB size=448x320 at 0x7BFC47503670>
Okay, here's my analysis of the provided example, focusing on perception, structured observations, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves a grid of numerical values, representing colors. There are distinct regions of color within the grid. The transformation seems to involve adding a new row at the bottom, which has some relation to the existing grid.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      rows: 5
      columns: 7
      cells: integers (0-9, representing colors)
    relationships:
      - adjacent_cells (share a side or corner)
      
  - type: region
    properties:
     color: a single integer
     shape: contiguous block of cells
     
actions:
- type: copy
  description: maintain layout and value of pixels

- type: create
  description: add a new row at bottom

- type: set_value
   description: change an existing cell's value in a location to a new value

```


**Natural Language Program:**

1.  **Copy:** The entire input grid is copied to the output grid.
2.  **Create:** A new row is added at the bottom of the output grid.
3. **Inspect previous row.** For each cell in the newly created row (starting from the left):
4.  **Conditional Value:**
    *   If the cell above it, two rows up in the original row 3, is not 0, and it is the first cell in the output with this condition, then the new cell value is set to 4.
    *   If the cell, two rows up in original row 3 is not 0, and a previous cell in the output in the new row is 4, skip to the next one, unti a new cell with color not 0 is reached, set this to 4.
    *  If the cell above and two rows up is 0, then the new cell's value is set to 0.

Essentially, the last row examines two rows above it. It puts '4' under the first of each grouping two rows above and puts '0' if the cell two rows above is '0'.

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
