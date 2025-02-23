# 6e02f1e3 • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
3 3 3
3 3 3
3 3 3
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC475017E0>

**output:**
```
5 5 5
0 0 0
0 0 0
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC47503520>
Okay, here's my analysis of the example input-output pair:

**Perception of Elements:**

The task involves two 3x3 grids. The input grid consists entirely of the number 3 (green color). The output grid has the top row replaced with the number 5 (gray color) and the remaining two rows replaced with the number 0 (white color). The grid structure itself (3x3) remains constant.

**YAML Block (Facts):**


```yaml
facts:
  - object: input_grid
    type: grid
    dimensions: 3x3
    elements:
      - value: 3
        color: green
        position: all cells
  - object: output_grid
    type: grid
    dimensions: 3x3
    elements:
      - value: 5
        color: gray
        position: top row
      - value: 0
        color: white
        position: middle and bottom rows
  - action: replace_values
    description: Values in the input grid are replaced based on their row position.
  - relationship: constant_grid_structure
    description: The dimensions of the grid remain 3x3 in both input and output.
```


**Natural Language Program:**

1.  **Identify Rows:** Divide the input grid into three rows: top, middle, and bottom.
2.  **Replace Top Row:** Replace all values in the top row of the input grid with the value 5 (gray).
3.  **Replace Other Rows:** Replace all values in the middle and bottom rows of the input grid with the value 0 (white).
4. **Output** The transformed grid is the final output.

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
