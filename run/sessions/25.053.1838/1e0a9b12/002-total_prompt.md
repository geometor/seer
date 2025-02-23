# 1e0a9b12 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x795F858DE320>

**output:**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x795F858DE380>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two 4x4 grids.  The input grid contains single-digit integers (0-9), representing different colors.  The output grid also contains single-digit integers, with some cells seemingly moved or combined. The most salient observation is that the non-zero values from the input are repositioned in the output. Specifically, all the non-zero values move to the last row.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: input grid
    dimensions: 4x4
    elements: integers (0-9)
  - type: grid
    description: output grid
    dimensions: 4x4
    elements: integers (0-9)
  - observation: object_movement
    description: Non-zero elements in the input grid are repositioned.
  - observation: spatial_relation
    description: Non-zero values from input are moved to the bottom row in the output.
  - observation: order_preservation
    description: relative order of non-zero elements appear to be sorted from left to right
```


**Natural Language Program:**

1.  **Identify**: Locate all non-zero pixels within the input grid.
2.  **Collect**: Gather these non-zero pixels, preserving their original values.
3.  **Sort**: Sort the collected pixels based on original column, then original row, in ascending order.
4.  **Place**: Position the sorted pixels along the bottom row of the output grid, filling cells from left to right.
5.  **Fill**: All other cells in output grid default to value of 0.

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
