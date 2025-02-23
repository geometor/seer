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

<PIL.Image.Image image mode=RGB size=640x640 at 0x74153085B970>

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

<PIL.Image.Image image mode=RGB size=640x640 at 0x74153085B850>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a 2D grid (matrix) of single-digit integers, where each integer represents a color. The input grid appears to contain a shape formed by the digit '3' (green) on a background of '0' (white). The output grid is almost identical to the input, except for a single '3' being changed to a '4' (yellow). This suggests a highly localized, possibly rule-based or coordinate-based, modification. The core operation seems to be identifying a specific '3' and changing its value.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    type: 2D array
    elements: integers (0-9)
    interpretation: color values
  - object: shape
    value: 3
    color: green
    description: contiguous block of 3s
  - object: background
    value: 0
    color: white
  - action: change_value
    location: specific coordinate
    old_value: 3
    new_value: 4
  - observation:
    description: Only one instance of '3' is changed to '4'.
```


**Natural Language Program:**

1.  **Identify the Shape:** Locate the contiguous region of pixels with the value '3' (green) within the input grid.
2.  **Locate Target Pixel:** Within the identified shape, find the pixel at a specific location. Based purely on this *single example*, it seems like the 4 is one up from bottom of the object and centered, but with a single point it is difficult to determine what feature marks it as a coordinate.
3. **Perform the change:** Change the value of the located '3' pixel to '4' (yellow).
4.  **Preserve the Rest:** All other pixels in the grid remain unchanged.

It should be noted, with a single example it is very difficult to pinpoint how the changed pixel is selected. More examples will make it easier to determine the rule.

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
