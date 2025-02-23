# 00d62c1b • 010 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 0 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7398A1243730>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 4 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7398A12F6890>
Okay, here's my analysis of the example input-output pair, formatted as requested:

**Perception of Elements:**

The task involves a grid of pixels, initially with values of 0 (white) and 3 (green). The transformation seems to involve a localized change: a single pixel changes from green (3) to yellow (4). This change occurs within a cluster of green pixels. Specifically, the pixel that changes appears to be surrounded by other green pixels.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      - width: 10
      - height: 10
      - cells: pixels
        values: [0, 3, 4]
        colors: [white, green, yellow]

  - type: pixel
    properties:
      - color: integer value representing a color

actions:
  - name: change_color
    input: a single green pixel
    conditions:
      - The pixel is surrounded by other green pixels.
    output: changes pixel color to yellow

relationships:
   - adjacency: pixels can be adjacent to each other (horizontally, vertically, or diagonally).

```


**Natural Language Program:**

1.  **Identify** all green (3) pixels within the input grid.
2.  **Select** a *single* green pixel that is completely surrounded on all sides (horizontally and vertically) by other green pixels. It must have all neighbors, at minimum up, down, left and right as green pixels.
3. **Change** the color of the selected pixel to yellow (4).
4.  **Maintain** all other pixel values. Output the modified grid.

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
