# bbc9ae5d • 026 • example_5 • investigate_coder

---

## Example 5

**input:**
```
7 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x64 at 0x7BFC47585480>

**output:**
```
7 0 0 0 0 0
7 7 0 0 0 0
7 7 7 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x192 at 0x7BFC47501090>
Okay, here's my analysis of the provided example:

**Perception of Elements:**

The task involves a transformation of a 1x6 grid (input) to a 3x6 grid (output). The input grid contains a single orange (7) pixel in the first cell and the rest are white (0). The output grid expands the single orange pixel into a 3x3 block of orange pixels in the top-left corner, while maintaining the original dimensions of other (0 - white) pixel locations.

**YAML Block (Facts):**


```yaml
facts:
  - object: input_grid
    type: grid
    dimensions: 1x6
    elements:
      - color: orange (7)
        position: [0,0]
      - color: white (0)
        position: [0,1:5] # shorthand for positions [0,1], [0,2]...[0,5]

  - object: output_grid
    type: grid
    dimensions: 3x6
    elements:
      - color: orange (7)
        position: [[0,0], [1,0], [2,0], [0,1], [1,1], [2,1], [0,2], [1,2], [2,2] ]
      - color: white (0)
        position: [[0,3],[0,4],[0,5], [1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]

  - action: expansion
    description: The orange pixel at [0,0] in the input is expanded.
    input_position: [0,0]
    output_positions: [[0,0], [1,0], [2,0],[0,1], [1,1], [2,1],[0,2], [1,2], [2,2]]

  - relationship:  size_change
    description: input grid height is 1, output grid height is 3.  Other pixel positions do not change

```


**Natural Language Program:**

1.  **Identify** the orange (7) pixel in the input grid.
2.  **Expand** the orange area. Create a 3x3 block of orange pixels in output grid, with position of original orange pixel as the top left cell.
3.   **Copy** all white (0) pixel positions
4.  **Construct** the output grid, maintaining the original horizontal length, but with 3 times the original height.


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
