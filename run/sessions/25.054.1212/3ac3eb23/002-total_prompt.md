# 3ac3eb23 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 2 0 0 0 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x384 at 0x7BFC4423DCF0>

**output:**
```
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x384 at 0x7BFC4423C1C0>
Okay, here's a breakdown of my observations and a proposed natural language program for the transformation:

**Perception of Elements:**

*   **Input Grid:** A 2D grid of colored pixels (represented by numbers 0-9). Most of the grid is white (0), with a few red (2) and azure (8) pixels.
*   **Output Grid:** A 2D grid with the same dimensions as the input. It seems to be a modified version of the input grid. The core structure and white pixels are maintained. The previously-red and previously-azure colored pixels generate additional colored pixels.
*  The added pixels are on odd-numbered rows.
* **Colors:** The relevant colors appear to be white (0), red (2), and azure (8).

**YAML Facts:**


```yaml
facts:
  - object: input_grid
    type: 2D array
    properties:
      - dimensions: 6x10 (rows x columns)
      - values: integers (0-9) representing colors
  - object: output_grid
    type: 2D array
    properties:
      - dimensions: 6x10 (rows x columns)
      - values: integers (0-9) representing colors
  - observation: "Red (2) and Azure (8) pixels in the input grid trigger changes in the output grid."
  - observation:  "New pixels appear on every odd numbered row"
  - relationship: "The output grid is a transformation of the input grid, maintaining original white spaces."
  - action: copy
    description: "All background pixels are copied."
  - action: duplicate_with_offset
    description: "Red (2) and azure (8) pixels are duplicated with an vertical offset below"
    parameters:
        rows: 1
        columns: 0
  - constraint: "The change by vertical offset only happens on odd rows"

```


**Natural Language Program:**

1.  **Copy Background:** Copy all white (0) pixels from the input grid to the output grid, preserving their positions.
2.  **Process Key Pixels:** For each non-zero pixel in the input grid:
    *   **Check Row Parity:** If the pixel is located on even row (starting with first row as 0), take no action.
    *  **Duplicate Below**: If the pixel is located on an odd row, duplicate it one row below.

Essentially, the transformation copies the input and adds vertically-offset pixels to the odd rows.

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
