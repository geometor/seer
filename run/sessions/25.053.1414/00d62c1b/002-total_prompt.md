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

<PIL.Image.Image image mode=RGB size=384x384 at 0x7D261845BA30>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7D261845B670>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a 2D grid (matrix) of single-digit integers, where each number can be interpreted as a color. The input grid transforms into a modified output grid. The primary change seems to be the introduction of the number '4' (yellow) adjacent to existing '3' (green) pixels. The overall grid dimensions remain constant.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: 2D array of integers (0-9) representing colors.
    properties:
      - dimensions: height and width are equal, and constant across input/output.
      - values: integers in the range 0-9.
  - type: object
    description: contiguous block of pixels of the same color.
    properties:
      - color: integer value representing the color.
      - location: row and column indices in the grid.
  - type: transformation
    description: modification of the grid based on specific rules.
    actions:
      - identify: find all pixels with the value '3'.
      - modify: change the color of pixels that are direct horizontal or vertical neighbors (not diagonal) to '3', by updating the to value '4'.
      - preserve: keeps the original pixels that were '3' as '3'.
    constraints:
      - spatial: only directly adjacent (up, down, left, right) pixels are affected, not diagonals.
```


**Natural Language Program:**

1.  **Identify:** Locate all pixels within the input grid that have a value of '3' (green).
2.  **Iterate:** For each pixel found in step 1, examine its four immediate neighbors (up, down, left, and right). Do not consider diagonal neighbors.
3.  **Modify:** If a neighboring pixel's value is not '3', change it to '4' (yellow).
4. **Preserve:** The original pixel that was found having the value '3' should keep it's same '3' value.
5.  **Output:** Produce the modified grid. All other pixels retain their original values.

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
