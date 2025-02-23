# a85d4709 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 5
0 0 5
0 0 5
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x737FBF03EFE0>

**output:**
```
3 3 3
3 3 3
3 3 3
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x737FBE5FDE40>
Okay, here's my analysis of the provided example:

**Perception of Elements:**

The task involves a transformation of a grid of numerical values. The input grid contains the values 0 and 5, while the output grid contains only the value 3. The dimensions of the grid (3x3) remain constant during the transformation. The key change seems to be a uniform replacement of all input values with the value 3.

**YAML Block (Facts):**


```yaml
facts:
  - observation: Input grid is a 3x3 matrix.
  - observation: Output grid is a 3x3 matrix.
  - observation: Input grid contains values 0 and 5.
  - observation: Output grid contains only the value 3.
  - relationship: All values in the input grid are replaced by 3 in the output grid.
  - object: input_grid
    properties:
      dimensions: 3x3
      values: [0, 5]
  - object: output_grid
    properties:
      dimensions: 3x3
      values: [3]
  - action: replace_all
    input: input_grid.values
    output: output_grid.values
    parameters: {old_value: input_grid, new_value: 3}
```


**Natural Language Program:**

1.  **Input:** Receive a 3x3 grid (input_grid).
2.  **Transformation:** Replace every value in the input grid with the value 3.
3. **Output**: the transformed grid.

In essence, the program describes a simple global substitution: All values of every cell are turned to the number 3.

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
