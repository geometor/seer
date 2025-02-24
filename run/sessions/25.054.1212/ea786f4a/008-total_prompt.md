# ea786f4a • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
2 2 2 2 2
2 2 2 2 2
2 2 0 2 2
2 2 2 2 2
2 2 2 2 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7BFC47503DF0>

**output:**
```
0 2 2 2 0
2 0 2 0 2
2 2 0 2 2
2 0 2 0 2
0 2 2 2 0
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7BFC47500F40>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a 2D grid (matrix) of pixels. Each pixel has a numerical value representing a color. In this specific example, we see two colors: '2' (red) and '0' (white). The input grid appears to be transformed into an output grid of the same dimensions. The transformation seems to involve changing some of the '2' (red) pixels to '0' (white) pixels, and vice-versa, in a specific pattern. The primary object is the grid itself, and the pixels within it are sub-objects that are manipulated.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    type: 2D array
    properties:
      - dimensions: 5x5
      - elements: pixels
      - values: [0, 2]
  - object: pixel
    type: element
    properties:
      - color:
          mapping:
            0: white
            2: red
  - transformation:
      type: color change
      details:
        -  A "frame" of white pixels appear in the output.
        - The center pixel stays the same
        - White pixels are placed, on the first and last columns and rows, such
          that when a "0" appears in the input, it will create a whole line and
          column (cross-like) filled with 0 in the ouput.
```


**Natural Language Program:**

1.  **Initialization:** Start with the output grid being a copy of the input grid.

2.  **Center Preservation:** The pixel in the center of the grid remains unchanged.

3.  **Frame and Cross:** Identify the center pixel (at row 2, column 2, using 0-based indexing).
    - If original center is white, place a white "frame" in output grid.
    - Place a white frame by changing to white the pixels on the perimeter.

4.   **Center Cross**: If a pixel in the original grid is white, ensure that the whole rows and columns containing that pixel become white.
In other words, if input\[i]\[j] == 0, then set output\[i,:] = 0 and output\[:,j] = 0.


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
