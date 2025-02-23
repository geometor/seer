# 57aa92db • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 8 8 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1152x960 at 0x70FFF010E230>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 3 3 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 3 0 0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 8 8 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 4 4 4 4 2 2 0 0 0 0 0 0 0 0 0 0
0 0 4 4 4 4 2 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1152x960 at 0x70FFF010F0A0>
Okay, here's my analysis of the provided example, focusing on perception, structured observations, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves 2D grids containing colored pixels. The colors represent digits 0-9.  The primary colors observed are white (0), green (3), red (2), azure (8), yellow (4). The input and output grids have the same dimensions. There appear to be distinct colored objects, possibly defined by contiguous blocks of the same color. Some objects expand, others stay the same, and some new components may get added.

**YAML Block (Facts):**


```yaml
facts:
  - type: grid
    description: Input and output are 2D grids of digits/colors.
    dimensions: identical for input and output
  - type: object
    attribute: color
    values: [white, green, red, azure, yellow]
    description: Contiguous blocks of the same color.
  - type: transformation
    description: Objects can change in size and extent.
    details:
      - type: expansion
        color: green
        direction: up and to the left
      - type: maintain
        color: azure, red
      - type: extend_and_fill
        color: yellow
        direction: Down and to the left, incorporating adjacent red squares, expanding overall size and merging.

```


**Natural Language Program:**

1.  **Identify Objects:** Locate all contiguous blocks of non-white pixels in the input grid. These are our initial objects.

2.  **Green Object Expansion:** The green object expands. If it exists, increase its size by one pixel in all orthogonal directions (up, down, left, right).

3. **Yellow Object Expansion:** If exists, the yellow object will check if red squares are diagonal from it. If so, extend them to down and to the left, filling the area between them.

4.  **Preserve Other Objects:**  All other non-green, non-yellow objects (in this case, the azure and red objects) retain their original shape and position in the output grid.

5.  **Background:** All other pixels (white/0) remain unchanged.

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
