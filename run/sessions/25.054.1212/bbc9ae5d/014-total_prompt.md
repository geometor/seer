# bbc9ae5d • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
5 5 5 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x64 at 0x7BFC47501090>

**output:**
```
5 5 5 0 0 0 0 0 0 0
5 5 5 5 0 0 0 0 0 0
5 5 5 5 5 0 0 0 0 0
5 5 5 5 5 5 0 0 0 0
5 5 5 5 5 5 5 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x320 at 0x7BFC475A32B0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves a transformation of a 2D grid of single-digit integers (representing colors). The input is a single row, and the output is a rectangular grid. The non-zero values in the input seem to expand vertically and to the right, forming a growing sequence of squares. The zero values remain unchanged.

**YAML Fact Block:**


```yaml
facts:
  - object: input_grid
    type: 2D array
    dimensions: 1 x 10 (initial)
    elements: integers (0-9)
  - object: output_grid
    type: 2D array
    dimensions: 5 x 10 (final)
    elements: integers (0-9)
  - observation: non_zero_expansion
    description: Non-zero values expand into squares.
    details: Each subsequent row adds one more instance of the non-zero element to the right.
  - observation: zero_preservation
    description: Zero values remain unchanged in the output grid.
  - relationship: input_output_correspondence
    description: Each element in the input row corresponds to a column or a set of columns in the output.
```


**Natural Language Program:**

1. **Initialization:** Start with the input grid (a single row).
2. **Iterate** through each element in the input row.
3. **Non-zero Expansion:** If the element is non-zero:
    - Create a 'square' of that element in the output.
    - The height of output square equal to number of non-zero values to the left including current value.
4. **Zero Preservation:** If the element is zero, copy it directly to the corresponding column in all rows of the output grid.
5. **Output:** The resulting 2D array is the output grid.

In simple terms, it's like each non-zero number "grows" into squares, with each subsequent row of out having an expanded square to the right by one. The zeros stay as they are.

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
