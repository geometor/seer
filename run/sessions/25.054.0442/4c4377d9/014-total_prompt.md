# 4c4377d9 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
9 4 9 4
9 9 4 4
4 4 4 4
```

<PIL.Image.Image image mode=RGB size=256x192 at 0x7AA3AFEF6C20>

**output:**
```
4 4 4 4
9 9 4 4
9 4 9 4
9 4 9 4
9 9 4 4
4 4 4 4
```

<PIL.Image.Image image mode=RGB size=256x384 at 0x7AA3AFB9D750>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. Both grids contain single-digit integers representing colors (in this specific example, 9 (maroon) and 4 (yellow)). The output grid appears to be a vertically mirrored and elongated version of the input grid. The input grid has dimensions 3x4, while the output is 6x4. It duplicates the pattern and flips it vertically

**YAML Fact Block:**


```yaml
facts:
  - subject: input_grid
    description: A 2D array of integers.
    properties:
      rows: 3
      columns: 4
      elements: [9, 4]
    relations:
      - to: output_grid
        type: transformed_to
        details: "vertical mirroring and expansion"

  - subject: output_grid
    description: A 2D array of integers.
    properties:
      rows: 6
      columns: 4
      elements: [9, 4]
    relations:
       - from: input_grid
         type: transformed_from
         details: output is double input height, with vertical reflection

  - subject: transformation
    description: The process of changing input to output.
    properties:
      type: geometric
      actions:
       - name: vertical_reflection
         details: mirror image along horizontal centerline
       - name: vertical_expansion
         details: original grid stacked on top of reflection
```


**Natural Language Program:**

1.  **Duplicate:** Create an exact copy of the input grid.
2.  **Reflect:** Vertically reflect the duplicated copy (flip it upside down).
3. **Stack**: Stack the original copy on top of the vertically reflected, duplicated copy.
4.  **Output:** The resulting combined grid is the output.

In summary, the transformation duplicates the input and stacks the original on top of its reflection.

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
