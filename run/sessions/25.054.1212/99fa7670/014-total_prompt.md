# 99fa7670 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0 0
0 8 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 5 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7BFC47F93880>

**output:**
```
0 0 0 0 0 0
0 8 8 8 8 8
0 0 0 0 0 8
0 0 0 0 0 8
0 0 0 5 5 5
0 0 0 0 0 5
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7BFC47FBB6D0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two 6x6 grids. The input grid contains two distinct non-zero colored pixels: an azure (8) pixel and a gray (5) pixel, with the rest being white (0). The output grid shows these colored pixels expanding. The azure pixel expands horizontally to fill the rest of its row. The gray pixel fills the rest of *its* row. Additionally, both of the non-zero colors fill downward. The original locations of non-zero pixels remain the same, they simply grow in two directions.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    description: 6x6 matrix of pixels
    properties:
      - rows: 6
      - columns: 6
      - values: integers representing colors (0-9)

  - object: pixel
    description: individual cell within the grid
    properties:
      - color: integer value (0-9), mapped to a specific color
      - position: (row, column) coordinates

  - object: azure_pixel
    description: pixel with value 8
    properties:
      - initial_position: (1, 1)  # (row, col) in input
      - color: azure

  - object: gray_pixel
    description: pixel with value 5
    properties:
       - initial_position: (4, 3)  # (row, col) in input
       - color: gray

  - action: expand_horizontally
    description: fill the remaining cells in the same row with the pixel's color, originating from the initial position of each non-zero color.
    performed_by:
      - azure_pixel
      - gray_pixel
    constraints:
      - stops at grid boundaries

  - action: fill_down
    description: The non-zero colors expand vertically down from their initial locations.
    performed_by:
        - azure_pixel
        - gray_pixel
    constraints:
      - fills to the bottom of the grid.
```


**Natural Language Program:**

1.  **Identify Non-zero Pixels:** Locate all pixels in the input grid that have a non-zero value (i.e., not white).
2.  **Horizontal Expansion:** For each non-zero pixel, extend its color horizontally across its entire row, replacing any 0 values.
3. **Fill Down:** For each non-zero pixel, starting at their initial location, expand vertically down to the bottom of the grid.

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
