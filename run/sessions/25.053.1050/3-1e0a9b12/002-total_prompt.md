# 3-1e0a9b12 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7745ED0D2350>

**output:**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7745EC576920>
Okay, here's my analysis of the example input-output pair:

**Perception of Elements:**

The task involves two 4x4 grids. The input grid contains single-digit integers (0-9) representing different colors. The output grid appears to be a transformation of the input grid. The most noticeable change is the rearrangement of the non-zero colored pixels.

**YAML Block (Facts):**


```yaml
facts:
  - type: grid
    description: 2D array of integers representing colors
    dimensions: 4x4
    elements: integers from 0 to 9
  - object: non-zero pixels
    description: Pixels with values other than 0
    property: color (represented by integer value)
    property: position (row, column)
    action: moved to different positions
  - object: zero pixels
    description: Pixels with value 0 (white)
    property: position (row, column)
    action: remain in place or get replaced
  - relationship: rearrangement
    description: Non-zero pixels are rearranged in the output grid.
    details: the values of non zero pixels are moved to bottom row of output
```


**Natural Language Program:**

1.  **Identify:** Locate all non-zero pixels in the input grid.
2.  **Collect**: make a list of the values of the non-zero pixels
3.  **Clear:** set all input non zero pixels to zero
4.  **Arrange:** Place the collected non-zero values into the last row of the output grid, from left to right, filling any remaining spaces with zeros.
5.  **Preserve Zeros:** If any zeros remain, move from input, transfer those zeros to the same location in output.

In simpler terms, the transformation extracts all the colored (non-zero) pixels from the input, and places them in the last row of the output grid, maintaining their original order. The rest of the cells are made or remain zero.

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
