# AboveBelow1 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 6 6 6 0 0 0 6 6 6 6 0 6 6
0 0 0 6 6 6 0 0 0 6 6 6 6 0 6 6
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
0 0 6 6 6 0 0 0 0 0 6 6 6 6 0 0
0 0 6 6 6 0 0 0 0 0 6 6 6 6 0 0
0 0 0 0 0 0 0 0 0 0 6 6 6 6 0 0
0 0 0 0 0 0 0 0 0 0 6 6 6 6 0 0
0 0 6 6 0 0 6 6 0 0 6 6 6 6 0 0
0 0 6 6 0 0 6 6 0 0 0 0 0 0 0 0
0 0 6 6 0 0 6 6 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1024x640 at 0x7995F901BB20>

**output:**
```
0 0 0 6 6 6 0 0 0 6 6 6 6 0 6 6
0 0 0 6 6 6 0 0 0 6 6 6 6 0 6 6
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1024x640 at 0x7995F901BF70>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors observed are white (0), magenta (6), and green (3). The input grid appears to contain distinct regions or shapes formed by these colors. The output grid seems to be a modified version of the input, with some areas "erased" or set to white (0). The most noticeable change is the removal of most of the magenta (6) pixels, particularly in the lower part of the grid. The green (3) horizontal line remains untouched.

**YAML Fact Block:**


```yaml
facts:
  - observation: |
      The input grid is a 10x16 matrix of pixels.
  - observation: |
      The output grid is the same size as the input grid (10x16).
  - objects:
      - name: magenta_region_1
        type: pixel_region
        color: magenta (6)
        location: top_right
        properties:
          - contiguous: true
      - name: magenta_region_2
        type: pixel_region
        color: magenta (6)
        location: top_left
        properties:
            - contiguous: true
      - name: magenta_region_3
        type: pixel_region
        color: magenta(6)
        location: middle_right
        properties:
            contiguous: true
      - name: magenta_region_4
        type: pixel_region
        color: magenta(6)
        location: bottom_left
        properties:
            contiguous: true
      - name: green_line
        type: pixel_region
        color: green (3)
        location: row_3
        properties:
          - contiguous: true
          - shape: horizontal_line
  - actions:
      - name: erase_magenta
        target: magenta_regions
        condition: "location != top_right and location != top_left"
        result: set_pixels_to_white(0)
  - relationships:
      - type: spatial
        description: "The magenta regions are distributed across the grid, green region is a horizontal line in the top section"
```


**Natural Language Program:**

1.  **Identify Regions:** Locate all contiguous regions of magenta (6) pixels and the single contiguous region of green (3) pixels.
2.  **Preserve Top Magenta:**  Keep any magenta pixels located in the top three rows of grid.
3. **Erase Other Magenta:** Change the color of all other magenta (6) pixels to white (0).
4.  **Preserve Green:** Do not modify the green (3) pixels.

In simpler terms, the transformation erases all the magenta areas except for the ones in the top three rows, while leaving the green line intact.

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
