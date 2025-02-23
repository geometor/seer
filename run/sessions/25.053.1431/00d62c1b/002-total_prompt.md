# 00d62c1b • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x70DA4E04BAC0>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x70DA4E04B700>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a 2D grid (matrix) of single-digit integers, representing colors. The input grid transforms into the output grid. The primary colors involved appear to be white (0), green (3), and yellow (4). The transformation seems to involve a localized change, specifically affecting the green pixels and their immediate neighbors. It appears to be a form of cellular automata or a local neighborhood operation.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: 2D array of integers representing colors
    dimensions: 6x6
  - object: pixel
    properties:
      color:
        type: integer
        values: [0, 3, 4]
      position:
        type: coordinate
        description: (row, column)
  - action: color_change
    description: Change the color of certain green (3) pixels.
    trigger:
      condition: adjacency
      description: Green pixels adjacent to other green pixels
    result:
      color: yellow(4)
  - relationship: adjacency
    description: Orthogonal neighboring pixels (up, down, left, right).
    properties:
      type:
       values: [horizontal, vertical]

```


**Natural Language Program:**

1.  **Identify** all pixels with the color green (value 3) in the input grid.
2.  **Check** for the green pixels: is the green pixel adjacent to other green pixels by at least two of their orthogonal neighbor, horizontally or vertically?
3. **Change** the identified adjacent green pixels in step 2 to the color yellow (value 4)
4.  **Leave** all other pixels unchanged. The result is the transformed output.

Essentially it is a change of green to yellow, triggered by how many green neighbours that it has.

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
