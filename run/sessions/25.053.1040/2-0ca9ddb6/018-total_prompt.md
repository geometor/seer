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

<PIL.Image.Image image mode=RGB size=576x576 at 0x751433B1F400>

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

<PIL.Image.Image image mode=RGB size=576x576 at 0x751433B1F070>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a grid of pixels, initially with some colored pixels (red, blue, magenta) scattered within a background of white pixels (represented by the number 0). The transformation seems to involve adding new colored pixels (yellow, orange) adjacent to the existing ones, creating a sort of "halo" or "expansion" effect. The shape and size of the original colored pixels are maintained, and the expansion seems to be limited to immediate neighbors (up, down, left, and right, but not diagonal).

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    description: 2D array of pixels
    properties:
      - height: 9
      - width: 9
      - cells: integer values (0-9) representing colors

  - type: pixel
    description: Individual cell in the grid
    properties:
      - color: integer value (0-9)
      - position: (row, column) coordinates

  - type: colored_object
    description: A contiguous block of one or more non-white pixels.
    properties:
      - color: the color of the contiguous object

actions:
  - name: expand
    description: Add new pixels of specified colors adjacent to existing colored pixels.
    parameters:
      - original_color: The color of the object being expanded
      - new_color: The color of the new adjacent pixel

relationships:
  - adjacency: Pixels are considered adjacent if they share a side (up, down, left, or right).
  - expansion: original colored pixels connect to added color, forming new extended objects

```


**Natural Language Program:**

1.  **Identify original objects**: Find all contiguous non-white pixels in the input grid. These are the original colored objects.
2.  **Determine expansion colors**:
    *   If an original object is red (2), add adjacent pixels colored yellow (4).
    *   If an original object is blue (1), add adjacent pixels colored orange (7).
    *   If an original object is magenta (6) add adjacent pixels, but they will have yellow and orange nearby, so they will not be extended
3.  **Expand objects**: For each original colored object:
    *   For each pixel in the original object, check its four immediate neighbors (up, down, left, right).
    *   If a neighbor is white (0), change it to the designated expansion color based on the original pixel's color. Do *not* extend diagonally.
4. output the final grid


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
