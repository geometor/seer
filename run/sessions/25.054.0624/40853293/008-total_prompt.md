# 40853293 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 3 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 7 0 0 7 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 8 0 0 0 0 8 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x1280 at 0x70FFF010F4F0>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 3 4 3 3 3 3 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 7 4 7 7 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 8 8 8 8 9 8 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 9 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x1280 at 0x70FFF010F580>
Okay, here's my analysis of the provided example, focusing on perception, facts, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves 2D grids containing colored pixels. The primary element is the existence of single, isolated colored pixels in the input grid. These isolated pixels seem to trigger the creation of vertical and horizontal lines of the same color in the output grid. The lines extend from the original pixel's position. The lines appear to be one pixel wide. The output retains the colors of input singletons, but fills in adjacent pixels.

**YAML Block (Facts):**


```yaml
facts:
  - object: isolated_pixel
    description: A pixel with a color different from all its immediate neighbors (up, down, left, right).
    properties:
      - color: Integer value (0-9) representing the pixel's color.
      - position: (row, column) coordinates in the grid.
  - action: extend_line
    description: Creates a line of the same color as the isolated pixel.
    properties:
      - direction: vertical and horizontal from the isolated pixel.
      - length: Extends to fill pixels with the same color as original or blank spaces (0).
  - grid:
      description: 2D array of colored pixels
      properties:
          - dimensions: height x width
```


**Natural Language Program:**

1. **Identify Isolated Pixels:** Scan the input grid and identify all "isolated pixels." An isolated pixel is defined as a pixel whose color is different from all four of its immediate neighbors (up, down, left, and right).
2.  **For Each Isolated Pixel**:
    -   Record the pixel's original `color` and `position`.
    -   **Horizontal Extension:** 
       -    Fill empty positions to the left and to the right of the original position with same color.
    -   **Vertical Extension:**
        -  Fill empty positions on top and to the bottom of the original position with the same color.
3.  **Output:** The resulting grid, with extended lines from each of the isolated pixels, is the final output.

Essentially, each isolated pixel in the input acts as a "seed" from which lines of the same color grow in both horizontal and vertical directions, until they encounter a different color. All original pixels are kept.

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
