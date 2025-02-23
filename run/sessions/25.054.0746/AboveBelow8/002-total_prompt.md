# AboveBelow8 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 3 8 8 3 3 3 3 3 3 3 3 0
0 3 3 8 3 3 3 3 3 3 3 3 0
0 6 6 8 6 6 6 6 6 6 6 6 0
0 6 6 8 6 6 6 6 6 6 6 6 0
0 7 7 8 8 8 7 7 7 7 7 7 0
0 7 7 7 7 8 7 7 7 7 7 7 0
0 4 4 4 4 8 8 4 4 4 4 4 0
0 4 4 4 4 4 8 8 8 8 4 4 0
```

<PIL.Image.Image image mode=RGB size=832x704 at 0x7995F901BB20>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 8 0 0 0 0 0 0 0 0 0
0 0 0 8 0 0 0 0 0 0 0 0 0
0 0 0 8 8 8 0 0 0 0 0 0 0
0 0 0 0 0 8 0 0 0 0 0 0 0
0 0 0 0 0 8 8 0 0 0 0 0 0
0 0 0 0 0 0 8 8 8 8 0 0 0
```

<PIL.Image.Image image mode=RGB size=832x704 at 0x7995F901BF40>
Okay, here's my analysis of the example input-output pair:

**Perception of Elements:**

The input is a grid of colored pixels. There are distinct horizontal bands of color. A single vertical column of azure (8) pixels appears to be the key element being isolated in the output. All other colors are replaced with grey (0).

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      width: 13
      height: 11
      colors: [0, 3, 6, 7, 4, 8]
  - type: horizontal_bands
    properties:
      colors: [3, 6, 7, 4] # Green, Magenta, Orange, Yellow
      pattern: contiguous blocks of the same color
  - type: vertical_column
    properties:
       color: 8  # Azure
       position: x = 3 (starting from 0)
       exists_in: input
       isolated_in: output
```


**Natural Language Program:**

1.  **Identify the vertical azure (8) column**: Locate the single, contiguous vertical column where all pixels are azure (value 8). In this case starts a x = 3
2.  **Preserve the azure column**: Maintain the azure pixels in their original positions in the output grid.
3.  **Clear other pixels**: Change all pixels that are *not* part of the identified azure column to grey (value 0).

In essence, the transformation isolates a specific pre-existing azure column within the input, setting all other areas to gray.

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
