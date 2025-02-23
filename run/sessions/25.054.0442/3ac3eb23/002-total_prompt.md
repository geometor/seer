# 3ac3eb23 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 2 0 0 0 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x384 at 0x7AA3AFB9DC30>

**output:**
```
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x384 at 0x7AA3AFB9FD60>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. Both grids contain single-digit integers (0-9), representing different colors. The input grid appears to have a sparse arrangement of non-zero values (2 and 8, corresponding to red and azure), while the output grid seems to be a modified version of the input grid, with a pattern involving the repetition of the non-zero values. The dimensions of the grids are the same.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: input grid
    dimensions: 6x10
    elements:
      - value: 0
        color: white
        count: 58
      - value: 2
        color: red
        count: 1
      - value: 8
        color: azure
        count: 1

  - type: grid
    description: output grid
    dimensions: 6x10
    elements:
      - value: 0
        color: white
        count: 44
      - value: 2
        color: red
        count: 7
      - value: 8
        color: azure
        count: 7

  - type: transformation
    description: input to output
    rule: >-
      Non-zero values in the input grid are replicated in a specific pattern
      in the output grid.  The pattern seems to alternate vertically down
      the column where the original is located.
```


**Natural Language Program:**

1.  **Identify Non-Zero Pixels:** Locate all pixels in the input grid that have a non-zero value.
2.  **Vertical Alternating Replication:** For each non-zero pixel in the input grid:

    *   Copy the value of that input pixel to the output pixel with the same coordinates.
    *   Moving to the next row down, replicate the non-zero pixel from the first row, alternating the non-zero value and zero.
    *    Continue down all rows, creating a mirrored vertical alternating pattern of the non-zero value and zero values below each original pixel value.

Essentially, the transformation replicates each non-zero pixel's value downwards, alternating the non-zero color with a zero value, creating a repeating pattern.

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
