# d406998b • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 5 0 0 5 0 5 0 0 0 5 0
5 0 0 0 5 0 5 0 0 5 0 0 5
0 5 0 5 0 0 0 0 5 0 5 0 0
```

<PIL.Image.Image image mode=RGB size=832x192 at 0x7BFC44391120>

**output:**
```
0 0 3 0 0 5 0 5 0 0 0 5 0
3 0 0 0 3 0 3 0 0 5 0 0 3
0 5 0 5 0 0 0 0 3 0 3 0 0
```

<PIL.Image.Image image mode=RGB size=832x192 at 0x7BFC443935B0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a transformation of a grid of colored pixels. The primary colors involved are gray (5), white (0), and green (3). The transformation seems to involve a selective replacement of gray (5) pixels with green (3) pixels based on their position, particularly in the first and second columns where they are adjacent to a white(0) pixel.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      dimensions: [3, 13] # 3 rows, 13 columns
      cells: pixels
      colors: [0, 3, 5] # white, green, gray

  - type: pixel
    properties:
      color:
        - white
        - gray
        - green
      position: [row, column]

actions:
  - name: replace_color
    agent: system
    target: pixel
    precondition: "pixel.color == gray AND adjacent to white pixel in first two columns"
    postcondition: "pixel.color == green"

relationships:
  - type: adjacency
    properties:
      - [pixel1, pixel2]: "pixel1 and pixel2 share a side"
```


**Natural Language Program:**

1.  **Identify Target Pixels:** Scan the input grid and identify gray (5) pixels that are in either the first or second column, moving left to right, and are vertically or horizontally adjacent to a white (0) pixel.

2.  **Conditional Replacement:** For each identified gray pixel in step 1, moving left to right, change its color to green (3).

3.  **Preserve Other Pixels:** All other pixels that do not meet the criteria in Step 1, keep their original color.

The core concept is the selective replacement of color, from Gray to Green, on pixels based on a positional rule, i.e. existing in either the first or second column and being adjacent to a white pixel.

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
