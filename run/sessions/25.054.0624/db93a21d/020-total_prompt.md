# db93a21d • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
0 0 0 0 0 0 0 9 9 9 9 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 9 9 9 9 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 9 9 9 9 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 9 9 9 9 0 0 0 0 0 0 0 0 9 9 9 9 9 9
0 0 9 9 9 9 0 0 0 0 0 0 0 0 9 9 9 9 9 9
0 0 9 9 9 9 0 0 0 0 0 0 0 0 9 9 9 9 9 9
0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 9
0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 9
0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 9 9 9 9 9
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1280x1280 at 0x70FFF0ECF7F0>

**output:**
```
0 0 0 0 0 3 3 9 9 9 9 3 3 0 0 0 0 0 0 0
0 0 0 0 0 3 3 9 9 9 9 3 3 0 0 0 0 0 0 0
0 0 0 0 0 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0
0 0 0 0 0 3 3 3 3 3 3 3 3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 1 1 1 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 1 1 1 3 3 3 3 3 3 3 3 3
3 3 9 9 9 9 3 3 1 1 1 3 3 3 3 3 3 3 3 3
3 3 9 9 9 9 3 3 1 1 1 3 3 3 9 9 9 9 9 9
3 3 9 9 9 9 3 3 1 1 1 3 3 3 9 9 9 9 9 9
3 3 9 9 9 9 3 3 1 1 1 3 3 3 9 9 9 9 9 9
3 3 3 3 3 3 3 3 1 1 1 3 3 3 9 9 9 9 9 9
3 3 3 3 3 3 3 3 1 1 1 3 3 3 9 9 9 9 9 9
0 0 1 1 1 1 0 1 1 1 1 3 3 3 9 9 9 9 9 9
0 0 1 1 1 1 0 1 1 1 1 3 3 3 3 3 3 3 3 3
0 0 1 1 1 1 0 1 1 1 1 3 3 3 3 3 3 3 3 3
0 0 1 1 1 1 0 1 1 1 1 3 3 3 3 3 3 3 3 3
0 0 1 1 1 1 0 1 1 1 1 0 0 0 1 1 1 1 1 1
0 0 1 1 1 1 0 1 1 1 1 0 0 0 1 1 1 1 1 1
```

<PIL.Image.Image image mode=RGB size=1280x1280 at 0x70FFF0143640>
Okay, here's my analysis of the provided input-output example, focusing on perception, object identification, and the transformation rule.

**Perception of Elements:**

The input and output grids consist of pixels with different colors, represented by digits 0-9. The primary colors involved seem to be maroon (9), white (0), green(3), blue(1). The input grid contains two distinct maroon (9) colored rectangular shapes, positioned at the top-left and bottom-right, on a white background. The output grid has changed substantially. The maroon areas maintain similar positioning but have changed colors to blue and green in different areas. The areas surrounding maroon objects also contain green and blue and the maroon shapes have become smaller inside green and blue fillings.

**YAML Block (Facts):**


```yaml
objects:
  - name: TopLeftMaroonShape
    type: rectangle
    color: 9 (maroon)
    initial_position: top-left
    properties:
      - contiguous
      - solid

  - name: BottomRightMaroonShape
    type: rectangle
    color: 9 (maroon)
    initial_position: bottom-right
    properties:
      - contiguous
      - solid

  - name: Background
    type: grid
    color: 0 (white)

actions:
  - name: ColorChange
    target: TopLeftMaroonShape
    from_color: 9 (maroon)
    to_color: varies #changes to blue and green

  - name: ColorChange
    target: BottomRightMaroonShape
    from_color: 9 (maroon)
    to_color: varies #changes to blue and green

  - name: fill_background_adjacent
    target: background pixels surrounding object
    from_color: 0 (white)
    to_color: 3 (green) or 1(blue)

relationships:
  - TopLeftMaroonShape: adjacent to Background
  - BottomRightMaroonShape: adjacent to Background
```


**Natural Language Program:**

1.  **Identify Maroon Rectangles:** Locate the two distinct rectangular shapes of color maroon (9) in the input grid. One is positioned towards the top-left, and the other towards the bottom-right.

2.  **Top-Left Maroon Shape Transformation:**
    *   Change the color of the pixels immediately adjacent and to the right of top left maroon shape to green(3)
    *   Change the color of the pixels immediately adjacent and below the top left maroon shape to blue (1).
    *   Change the top two rows of original maroon shape to green(3).
    *    Change the leftmost two columns of the original maroon shape to green(3).
    *   Change the remaining part of the maroon shape to blue (1)

3.  **Bottom-Right Maroon Shape Transformation:**

    *   Change the color of the pixels immediately adjacent and to the left of the bottom right maroon shape to blue(1)
    *   Change the colors of the pixels immediately adjacent and above the bottom right maroon shape to green(3)
    *    Change the rightmost two columns of the original maroon shape to green(3).
    *    Change the bottom two rows of the original maroon shape to green(3).
    *    Change the remaining part of the maroon shape to blue (1).

4. **Background Transformation:**
    * The majority of the background remains white (0).

In summary, the transformation involves identifying two maroon rectangles, changing parts of each to green and blue and adding adjacent pixels of green and blue around them.

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
