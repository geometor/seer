# 0a938d79 • 018 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x1408 at 0x70FA386F12D0>

**output:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
```

<PIL.Image.Image image mode=RGB size=576x1408 at 0x70FA3435F130>
Okay, here's my analysis of the provided example, broken down into perceptions, a YAML fact block, and a natural language program.

**Perceptions:**

*   The input and output are grids of digits, representing colors.
*   The input grid contains two distinct colored pixels: a red (2) pixel and a green (3) pixel, with the rest being white (0).
*   The output grid replicates the colored pixels horizontally to fill the entire row they originally occupied. This replication occurs in both directions from the original pixel.
*   The pattern of replication repeats below the original position of the single colored pixel.
*  The filled rows alternates below the origin row location

**YAML Fact Block:**


```yaml
facts:
  - object: red_pixel
    properties:
      color: red (2)
      initial_position: [5, 0] # [row, col]
      action: replicate_horizontally
  - object: green_pixel
    properties:
      color: green (3)
      initial_position: [7, 8]
      action: replicate_horizontally
  - object: background
    properties:
      color: white (0)
      action: replaced_by_replication
  - relation: replication
    type: horizontal
    details: "Each colored pixel extends its color across its entire row."
  - relation: pattern
    type: alternating
    details: "The rows are replicated in an alternating pattern below the origin"
```


**Natural Language Program:**

1.  **Identify Colored Pixels:** Locate all non-white (non-zero) pixels in the input grid.
2.  **Horizontal Replication:** For each colored pixel:
    *   Replace all white pixels in the same row with the color of the identified pixel.
3. **Pattern Replication:**
   *  Starting with each original colored pixel row.
   *  alternating below, fill the rows with the same color as the original pixel row.


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
