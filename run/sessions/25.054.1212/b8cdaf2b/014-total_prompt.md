# b8cdaf2b • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 6 6 6 0
6 1 1 1 6
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7BFC44391B10>

**output:**
```
0 0 0 0 0
0 0 0 0 0
1 0 0 0 1
0 6 6 6 0
6 1 1 1 6
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7BFC48A63190>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two 5x5 grids. The input grid contains pixels of colors white (0), magenta (6), and blue (1). The output grid shares the same bottom two rows with the input, a row of 1 and 0, where the '1' represents the locations of the previous white section.

**YAML Fact Block:**


```yaml
facts:
  - observation: |
      The input and output grids are both 5x5.
  - observation: |
      The bottom two rows of the input and output grids are identical.
  - observation: |
    The top two rows of the output grid are entirely white (0).
  - observation: |
    The third row from top has only white and changed to blue in corner, indicating location of blue.
  - objects:
      - name: grid
        type: 2D array
        dimensions: 5x5
        elements: integers (0-9 representing colors)
  - actions:
    - description: |
        Replace all '0' in 3x3 region in the top with '1', in corner locations.
```


**Natural Language Program:**

1.  **Copy** the bottom two rows of the input grid directly to the output grid.
2.  **Fill** the top two rows of the output grid with white pixels (0).
3.  **Fill** the third row up with `0`.
4.  **Locate** where `0` is in the original top three rows.
5.  **Change** the value of cell at this position in the third row to `1`.

Essentially, the transformation preserves the bottom two rows and represents in third row the location of white in the top three rows.

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
