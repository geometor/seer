# 00d62c1b • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x73A149E5B8E0>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x73A149E5B520>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a grid of numerical values, representing colors. The input grid appears to have a pattern of '3's (green) against a background of '0's (white). The output grid seems to modify some of the '3's to '4's (yellow), specifically those horizontally and vertically adjacent to other '3's. It appears to find the '3's with adjacent '3's.

**YAML Fact Block:**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 6x6
      elements: integers (0-9)
      color_map:
        0: white
        3: green
        4: yellow

  - type: pixel
    properties:
      value: integer
      position: (row, column)
      color: mapped from value

actions:
  - name: identify_adjacent
    description: Find pixels of a specific color that have adjacent pixels of the same color.
    parameters:
      target_color: 3
      adjacency_type: horizontal and vertical

  - name: modify_color
    description: Change the color of a pixel.
    parameters:
      new_color: 4

relationships:
  - type: adjacency
    description: Horizontal or vertical proximity between pixels.
```


**Natural Language Program:**

1.  **Identify Target Pixels:** Examine the input grid and locate all pixels with the value '3' (green).
2.  **Check for Adjacency:** For each identified '3' pixel, check if it has any adjacent pixels (horizontally or vertically, but not diagonally) that also have the value '3'.
3.  **Modify Central Pixels :** If a '3' pixel *has one neighbor*, keep original '3' value.
4.  **Modify Connected Pixels:** If a '3' pixel has more than one horizontal/vertical adjacent pixels with value '3', change its value to '4' (yellow).
5.  **Output:** Create the output grid with the modified pixel values, leaving all other pixels unchanged.

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
