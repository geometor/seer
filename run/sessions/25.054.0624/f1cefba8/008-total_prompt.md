# f1cefba8 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 4 1 1 1 1 1 1 1 0 0 0
0 0 1 1 4 4 4 4 4 4 4 4 1 1 0 0 0
0 0 1 1 4 4 4 4 4 4 4 4 4 1 0 0 0
0 0 1 1 4 4 4 4 4 4 4 4 1 1 0 0 0
0 0 1 1 4 4 4 4 4 4 4 4 1 1 0 0 0
0 0 1 1 1 1 1 1 4 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1088x960 at 0x70FFF010EC80>

**output:**
```
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 1 1 4 4 1 4 1 4 4 4 1 1 0 0 0
4 4 1 1 1 1 1 1 1 1 1 1 1 1 4 4 4
0 0 1 1 4 4 1 4 1 4 4 4 1 1 0 0 0
0 0 1 1 4 4 1 4 1 4 4 4 1 1 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 4 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1088x960 at 0x70FFF010E2C0>
Okay, let's analyze this input-output example.

**Perception of Elements:**

*   **Input:** A 17x15 grid.  Predominantly filled with 0 (white). Contains a central "object" composed of connected 1 (blue) and 4 (yellow) pixels. The yellow pixels are fully enclosed by the blue pixels.
*   **Output:** A 17x15 grid, same dimensions as the input. The central object is mostly preserved, except where modifications are apparent, the yellow parts are changed in color. There is a 3 pixels vertical line of color yellow and the number 4 added on the either sides of the central blue shape, where the borders are white.

**YAML Block (Facts):**


```yaml
facts:
  - object: main_shape
    properties:
      colors: [blue, yellow]
      description: A connected shape in the center of the grid. The yellow part is inside of the blue part.
      input_position: Rows 5-12, Columns 3-14
      output_position: Rows 5-12, Columns 3-14

  - object: background
    properties:
       color: white
       description: Fills the areas outside the main shape.

  - action: color_change
    description: Some yellow pixels in the input grid are still yellow in the output grid.
    details: the pixels remained as yellow form two vertical lines

  - object: added_elements
    properties:
      color: yellow
      description: vertical lines
      position: x = 3, y = 8; x = 7, y = 8; x=11, y = 8
    
  - object: border_elements
    properties:
      color: yellow
      description: the number four to represent yellow
      positions: left and right sides of the main_shape, where the background is white.

```


**Natural Language Program:**

1.  **Identify the central shape:** Locate the connected region of blue (1) and yellow (4) pixels in the input grid.
2.  **Preserve Blue:** Keep the entire shape of 1s in the output grid, in their respective place
3.  **Partial color Change:** Find the vertical symmetric middle, find the pixels on rows x=7 and x= 9, keep them to yellow.
4. **Vertical Lines**: Create yellow lines on x=3, x=7 and x= 11, and the length is the same
5.  **Add Border Elements:** On the horizontal borders, fill with yellow the white columns.


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
