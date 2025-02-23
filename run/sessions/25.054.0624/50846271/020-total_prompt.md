# 50846271 • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
0 5 0 0 0 0 5 0 0 0 0 5
5 0 5 0 0 0 0 0 5 0 0 5
5 0 5 0 0 5 5 0 2 0 5 0
5 5 0 0 5 0 5 0 2 5 0 5
5 0 0 5 5 5 2 5 2 2 2 0
5 5 5 0 5 5 0 5 2 0 0 5
5 5 5 0 5 0 0 5 5 0 0 0
5 0 0 0 0 5 0 0 0 0 0 0
0 5 5 0 5 0 0 0 0 5 0 0
5 0 0 0 5 5 5 5 5 0 0 0
5 0 0 0 0 5 0 0 5 5 5 5
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x70FFF01B1F60>

**output:**
```
0 5 0 0 0 0 5 0 0 0 0 5
5 0 5 0 0 0 0 0 5 0 0 5
5 0 5 0 0 5 5 0 2 0 5 0
5 5 0 0 5 0 5 0 2 5 0 5
5 0 0 5 5 5 2 8 2 2 2 0
5 5 5 0 5 5 0 5 2 0 0 5
5 5 5 0 5 0 0 5 8 0 0 0
5 0 0 0 0 5 0 0 0 0 0 0
0 5 5 0 5 0 0 0 0 5 0 0
5 0 0 0 5 5 5 5 5 0 0 0
5 0 0 0 0 5 0 0 5 5 5 5
```

<PIL.Image.Image image mode=RGB size=768x704 at 0x70FFF01B0C40>
Okay, here's my analysis of the example input-output pair, formatted as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The primary colors observed are gray (5), white (0), red (2), and azure (8).  The input and output grids are identical except for two changes related to the red "cross" shape. The change appears very localized. There are two single azure pixels in the output that was not in the input.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions: [11, 12] # Height x Width
      colors: [0, 2, 5, 8] # white, red, gray, azure

  - type: shape
    properties:
      color: 2 # Red
      form: cross
    location:
      row_center: 4
      col_center: 8

  - type: pixel
    properties:
      color: 8  #azure
    location:
        row: 4
        col: 7

  - type: pixel
    properties:
        color: 8
    location:
      row: 6
      col: 8
```


**Natural Language Program:**

1.  **Identify a "cross" shape:** Locate a contiguous region of red (2) pixels forming a cross shape. The cross is defined by a central red pixel, with four red pixels directly adjacent to it (above, below, left, and right).

2.  **Locate insertion points relative to cross:**
    *   **Point 1:** locate the position immediately to the left of the central red pixel of the cross
    *   **Point 2:** locate the postion immediately below the central red pixel of the cross.

3.  **perform insertion** insert an azure (8) pixel at each of the insertion points.

4.  **Copy all other pixels:** All pixels from the input that are not part of the modification defined above, are directly copied to the output.

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
