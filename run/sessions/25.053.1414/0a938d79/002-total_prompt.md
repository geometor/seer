# 0a938d79 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1600x640 at 0x7D261845B670>

**output:**
```
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
0 0 0 0 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0 2 0 8 0
```

<PIL.Image.Image image mode=RGB size=1600x640 at 0x7D261845B9D0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves transforming a grid of colored pixels (represented by numbers 0-9) into a new grid of colored pixels. The input grid appears to have a sparse distribution of colors (mostly white, with a few red and azure pixels), while the output grid has a much denser, repeating pattern of red and azure pixels, seemingly derived from the locations of the original non-white pixels. The dimensions of the grid remain the same (height and width).

**YAML Fact Documentation:**


```yaml
facts:
  - observation: |
      The input grid contains a few pixels of color red (2) and azure (8) on a background of white (0).
  - observation: |
      The output grid has the same dimensions as the input grid.
  - observation: |
      The output grid is filled with a repeating pattern of red (2) and azure (8) pixels.
  - relationship: |
      The pattern in the output grid seems to be derived from the positions of the non-white pixels in the input grid.
  - pattern: |
      The output pattern consists of alternating columns of red and azure, starting from the original column where a color first appears in the input.
  - action:
      Expand non-white pixels into columns in input grid.
  - action:
      Continue the non-white color in the output grid, alternating in
      every new column with the previously expanded non-white color.
```


**Natural Language Program:**

1.  **Identify Source Pixels:** Scan the input grid and identify all pixels that are not white (0). Record the color and (x, y) coordinates of each of these "source pixels".
2.  **Columnar Expansion:** For each source pixel found:
    *   Create a full column in the output grid at the x-coordinate (column) of the source pixel.
    *   Fill this column with the color of the source pixel.
3.  **Alternating Fill:** For each remaining column in the output, alternate the color of each source colors, left to right. For example, fill the column immediately to the right of first column with a different source color. If a source pixel is present, create a column with that color; otherwise, use the alternate color.
4. **Maintain Grid size**: The input and output grids have the same dimensions.

In simpler terms: The original colored pixels act as "seeds". Each seed grows into a vertical column of its color. The spaces between these columns are filled with alternating columns of each of the seed colors.

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
