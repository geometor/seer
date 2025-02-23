# b527c5c6 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 3 3 3 3 3 3 3 3 3 3 3 3 3 2 3 3 3 3 0
0 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1280x1280 at 0x70FFF4B4B0D0>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 3 2 3 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 3 2 3 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 3 2 3 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 3 2 3 0 0 0 0
0 3 3 3 3 3 3 3 3 3 3 3 3 3 2 3 3 3 3 0
0 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 3 3 2 2 2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 3 3 3 3 3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 3 3 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1280x1280 at 0x70FFF4B4BD90>
Okay, here's my analysis of the provided input-output example pair, formatted as requested:

**Perception of Elements:**

The task involves two 20x20 grids. The input grid contains two primary shapes: a horizontal rectangle of green (3) pixels with a single red (2) pixel near the right end, and a vertical rectangle of green (3) pixels, also with a single red (2) pixel, near the bottom. The rest of the input grid is filled with white (0) pixels. The output grid seems to highlight certain pixels in and around these rectangles. The large horizontal green rectangle and the vertical green rectangle get their red pixels duplicated, specifically the input red pixel is maintained, and it is copied to the left of the original on the upper horizontal bar, and upwards on the vertical one. The red pixel in the horizontal rectangle appears copied across the entire lower section of the rectangle.

**YAML Block (Facts):**


```yaml
facts:
  - object: horizontal_rectangle
    type: rectangle
    color: green (3)
    property: contains_red_pixel (2)
    position: top_half
  - object: vertical_rectangle
    type: rectangle
    color: green (3)
    property: contains_red_pixel (2)
    position: bottom_left
  - object: background
    color: white (0)
  - action: copy_red_pixel
    object: horizontal_rectangle
    direction: left, and down
  - action: copy_red_pixel
    object: vertical_rectangle
    direction: up
  - relationship: horizontal_rectangle_intersects_vertical_rectangle
```


**Natural Language Program:**

1.  **Identify Rectangles:** Locate all green (3) rectangles within the input grid.
2.  **Locate Red Pixels:** Within each identified green rectangle, find the single red (2) pixel.
3.  **Horizontal Rectangle Transformation**: For the upper horizontal green rectangle copy its red pixel to all of the empty space of the rectangle to the left, keeping its original position, and copy it to the bottom part from end to end of the rectangle..
4.  **Vertical Rectangle Transformation**: For the vertical green rectangle copy its red pixel. The copy is created above the input red pixel, keeping its original position.


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
