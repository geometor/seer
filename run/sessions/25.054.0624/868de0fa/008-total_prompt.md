# 868de0fa • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
1 1 1 0 1 1 1 1 1 1
1 0 1 0 1 0 0 0 0 1
1 1 1 0 1 0 0 0 0 1
0 0 0 0 1 0 0 0 0 1
0 0 0 0 1 0 0 0 0 1
0 0 0 0 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0F9C340>

**output:**
```
1 1 1 0 1 1 1 1 1 1
1 7 1 0 1 2 2 2 2 1
1 1 1 0 1 2 2 2 2 1
0 0 0 0 1 2 2 2 2 1
0 0 0 0 1 2 2 2 2 1
0 0 0 0 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FFF0ECF7F0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, with each pixel having a single integer value representing a color. The input grid appears to be primarily composed of white (0) and blue (1) pixels, while the output grid introduces red (2) and orange (7) pixels, seemingly based on the arrangement of the blue pixels in the input. The overall grid dimensions remain constant between input and output.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 10x10
      elements: pixels
  - type: pixel
    properties:
      color: integer (0-9)
      position: (row, column)

actions:
  - name: recolor_contiguous_block
    parameters:
      input_color: 1 (blue)
      output_color: 2 (red)
      minimum_size: 3
  - name: recolor_single_pixel
    parameters:
     input_color: 1
     output_color: 7
     location: (1,1)

relationships:
  - type: adjacency
    description: Pixels can be adjacent horizontally, vertically, or diagonally.
  - type: containment
    description: A group of adjacent pixels of the same color forms a contiguous block or object.
```


**Natural Language Program:**

1.  **Identify Contiguous Blue Blocks:** Scan the input grid to identify contiguous blocks of blue (1) pixels. A contiguous block is defined as a group of one or more blue pixels connected horizontally, vertically and/or diagonally.

2.  **Recolor Large Blue Blocks:** If a contiguous blue block consists of 3 or more blue pixels, change those pixel's colors to red (2).

3. **Recolor a Specific Pixel** If the blue pixel has the location (1,1), change its color to orange(7).

4.  **Preserve Other Pixels:** All other pixels retain their original colors. Specifically, isolated blue pixels (those not part of a larger contiguous block) and white pixels remain unchanged.

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
