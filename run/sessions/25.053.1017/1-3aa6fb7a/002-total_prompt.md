# 1-3aa6fb7a • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x75C2E5C1AE60>

**output:**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x75C2E5C1B640>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves a 2D grid of pixels, where each pixel has a numerical value representing a color. The primary color observed is '8' (azure), forming distinct shapes against a background of '0' (white). The transformation seems to involve a subtle change in the color of a single, specific pixel within the azure shapes.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: 2D array of pixels
    elements:
      - value: 0
        color: white
        role: background
      - value: 8
        color: azure
        role: object
      - value: 1
        color: blue
        role: marker
  - objects:
    description: Contiguous blocks of azure (8) pixels
    properties:
      - shape: irregular
      - size: variable
  - transformation:
    description: change in color
    action: A single azure (8) pixel within an object is changed to blue (1).
    location:
      description: The changed pixel seems to be interior, not on the edge. It's always on the second row or second to last row of the shape
```


**Natural Language Program:**

1.  **Identify Objects:** Locate all contiguous blocks of azure (8) pixels within the grid. These form the primary objects.
2.  **Select Target Pixel:** Within all of the objects, find the pixel that is on either the second row, or second-to-last row from the top or bottom of a shape and is azure.
3.  **Modify Pixel:** Change the color value of the selected pixel from azure (8) to blue (1).
4.  **Output:** The output grid is identical to the input grid except for the single modified pixel.

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
