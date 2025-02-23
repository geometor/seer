# 1e0a9b12 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7AA3AFE5FA90>

**output:**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7AA3AFE5F6D0>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a 4x4 grid. The input grid contains single-digit integers (0-9), representing different colors. The output grid seems to be a rearrangement of some of the elements from the input grid. The most notable change is that the non-zero elements seem to have moved to the bottom row, maintaining their original order.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    dimensions: 4x4
    elements: integers (0-9)
    element_type: pixel

properties:
  - property: color
    values: represented by integers 0-9
  - property: position
    values: row and column indices

actions:
  - name: move
    description: Non-zero elements are moved.
    precondition: element is non-zero
    postcondition: element is in the bottom row

relationships:
  - type: spatial
    description: Elements maintain their relative horizontal order.
  - type: source-destination
    description: non zero input elements map to bottom row of the output
  
```


**Natural Language Program:**

1.  **Identify** all non-zero elements within the input grid.
2.  **Maintain** the relative horizontal order of the identified non-zero elements.
3.  **Move** all non zero elements to the bottom row of the output.
4.  **Fill** all other grid positions in the output grid by 0.

Essentially, the transformation "collects" all non-zero digits and places them in order in the last row of the output grid, and the rest of the positions with zeros.

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
