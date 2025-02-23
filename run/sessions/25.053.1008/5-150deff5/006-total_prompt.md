# 5-150deff5 • 006 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 0 0 0
0 0 0 0 5 5 0 0 0
0 0 0 5 0 0 0 0 0
0 0 0 5 5 5 0 0 0
0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x512 at 0x762C40175B10>

**output:**
```
0 0 0 0 0 0 0 0 0
0 2 2 2 8 8 0 0 0
0 0 0 0 8 8 0 0 0
0 0 0 2 0 0 0 0 0
0 0 0 2 8 8 0 0 0
0 0 0 2 8 8 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x512 at 0x762C40175BD0>
Okay, here's my analysis of the provided example:

**Perception:**

The input and output are grids of the same dimensions. The input grid contains a shape made of grey (5) pixels. The output grid seems to redraw this shape using two different colors: red (2) and azure (8). The grey shape is divided into two parts. The leftmost part, a single line, is colored red, and the rest is colored azure.

**YAML Block (Facts):**


```yaml
objects:
  - name: InputGrid
    type: grid
    properties:
      - dimensions: 8x9
      - values: [0, 5]
  - name: OutputGrid
    type: grid
    properties:
      - dimensions: 8x9
      - values: [0, 2, 8]
  - name: GreyShape
    type: shape
    properties:
      - color: grey (5)
      - composition: contiguous grey pixels
  - name: RedShape
    type: shape
    properties:
      - color: red (2)
      - composition: contiguous red pixels
    location:
      - leftmost part of GreyShape
  - name: AzureShape
    type: shape
    properties:
      - color: azure (8)
      - composition: contiguous azure pixels
      location:
       - right part of GreyShape

actions:
 - description: Divide GreyShape vertically
 - description: Recolor the leftmost part Red
 - description: Recolor the rest of GreyShape Azure

relationships:
  - InputGrid contains GreyShape
  - OutputGrid contains RedShape and AzureShape
  - RedShape and AzureShape constitute a recoloring of GreyShape
```


**Natural Language Program:**

1.  Identify the contiguous shape composed of grey (5) pixels in the input grid.
2.  Divide this shape vertically. The leftmost segment is one column of the height of GreyShape.
3.  Redraw each segment on output grid.
4.  Change the color of leftmost segment to red (2).
5.  Change the color of rest of segment to azure (8).
6.  Leave all other pixels in the output grid as black (0).

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
