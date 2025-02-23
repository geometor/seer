# 2-0ca9ddb6 • 018 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7745ED0D2200>

**output:**
```
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 7 0 0 0 0 0
0 0 7 1 7 0 0 0 0
0 0 0 7 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7745EB1CB1F0>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The input grid seems to have a few distinct colored pixels (red, blue, magenta) scattered within a background of white pixels (represented by 0). The output grid introduces new colors (yellow, orange) and expands on the placement of some existing input colors, specifically around the blue pixel.

**YAML Block - Facts:**


```yaml
objects:
  - name: grid
    type: 2D array
    properties:
      - width: 9
      - height: 9
      - cells: pixels with color values (0-9)

  - name: pixel
    type: individual cell
    properties:
      - color: integer (0-9)
      - position: (row, column)

  - name: blue_pixel
    inherit: pixel
    properties:
      - color: 1

  - name: red_pixel
      inherit: pixel
      properties:
        - color: 2

  - name: magenta_pixel
    inherit: pixel
    properties:
      - color: 6
      
actions:
  - name: add_yellow
    description: Place yellow pixels (4) above and to the left of the blue. And above and to the left of the red pixel.
    
  - name: add_orange
    description: Create an L shaped pattern with orange (7) color around the blue.

relationships:
   - type: adjacency
     description: the relative positioning of colored pixels is crucial.

```


**Natural Language Program:**

1.  **Identify Key Pixels:** Locate the blue pixel (color 1), the red pixel (color 2) and the magenta pixel (color 6) within the input grid.

2. **Add Yellow Around Blue and Red**: Place a yellow pixel above and one to the left of the blue pixel. Place a yellow pixel above and one to the left of the red pixel.

3.  **Add Orange Around Blue:** Place orange pixels (color 7) to form an "L" pattern centered on the blue pixel, as follow: one to its left, one below, one to its right and one below that one.

4.  **Preserve original non-zero pixels:** All other pixels from the input grid, except zero, should remain in the same position and retain their original color in the output grid. Zero value pixels remain the same unless transformed.

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
