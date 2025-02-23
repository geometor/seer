# 2-0ca9ddb6 • 006 • example_3 - CODE

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

<PIL.Image.Image image mode=RGB size=576x576 at 0x7C32619439A0>

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

<PIL.Image.Image image mode=RGB size=576x576 at 0x7C3261943730>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, initially with a few colored pixels (red, blue, magenta) scattered within a background of white pixels (represented by the value 0). The transformation seems to involve adding new colored pixels (yellow, orange) around the existing ones, particularly in a cross or plus-sign (+) shape. The original colors seem to remain. There's likely a relationship between existing colors, the background, and the new colors added.

**YAML Fact Documentation:**


```yaml
facts:
  - type: grid
    description: Input and output are 2D grids of pixels.
    elements:
      - value: 0
        color: white
        role: background
      - value: 1
        color: blue
        role: original_pixel
      - value: 2
        color: red
        role: original_pixel
      - value: 6
        color: magenta
        role: original_pixel
      - value: 4
        color: yellow
        role: new_pixel
      - value: 7
        color: orange
        role: new_pixel
  - type: object
    description: Colored pixels can be considered as individual objects.
  - type: action
    description: New pixels are added around existing ones.
  - type: relationship
    description: The new pixels form a '+' shape around the original pixels where possible, extending one pixel in each cardinal direction.
    details: If a new pixel location would be occupied by existing pixels, then that location is skipped.
  - type: constraint
    description: new pixels added will fit within the grid
    details: If adding the full + shape would make new pixels fall outside of the input grid, it only fills up to the boundary.
```


**Natural Language Program:**

1.  **Identify Original Pixels:** Scan the input grid and identify all non-white (non-zero) pixels. These are the "original pixels."
2.  **Create Output Grid:** Initialize an output grid identical to the input grid.
3.  **Iterate Through Original Pixels:** For each original pixel in the input grid:
    *   **Check Neighbors:** Examine the four neighboring positions (up, down, left, right) around the original pixel in the output grid.
    *   **Add New Pixels** Add the appropriate pixel one above, one below, one left and one right of the original pixel.
        * If the original pixel is blue(1), add orange(7) pixels.
        * if the original pixel is red (2), add yellow(4) pixels.
        * if the original pixel is magenta (6), no new pixels.
4.  **Boundary Check:** If a neighboring position is outside the grid boundaries, skip adding a pixel in that direction.
5.  **Existing Pixel Check:** If a neighboring postion is not white(0) then skip adding a pixel in that direction.
6. Return the updated output grid.

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
