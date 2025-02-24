# 3618c87e • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0
0 0 0 0 0
0 1 0 0 1
0 5 0 0 5
5 5 5 5 5
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7BFC47544640>

**output:**
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 5 0 0 5
5 1 5 5 1
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7BFC47545240>
Okay, here's my analysis of the provided input-output example, focusing on perception, factual documentation, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves a transformation of a 2D grid of single-digit integers (representing colors). The most obvious changes are:

1.  **Color Swapping:**  Blue (1) and gray (5) pixels appear to swap positions, but not all instances, and based on location.
2.  **Row-Specific Changes:** The transformation seems specific to certain rows. The top three rows are unchanged.
3. **Symmetry**: There is a mirrored swap in the last two rows.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      rows: 5
      columns: 5
      cells:
        - value: 0 (white)
        - value: 1 (blue)
        - value: 5 (gray)

  - type: pixel
    properties:
      color:
        - white
        - blue
        - gray
      position: (row, column)

actions:
  - type: swap
    properties:
      affected_colors: [blue, gray]
      affected_rows: [4, 5] # 0 indexed
      affected_columns: conditional, mirrored

relationships:
  - type: positional
    description: "Pixels are arranged in a 2D grid."
  - type: conditional_swap
    description: "blue and grey swap based on row index and symmetry."

```


**Natural Language Program:**

1.  **Ignore Top Rows:** The first three rows (0, 1, and 2, using 0-based indexing) of the input grid are copied directly to the output grid without modification.

2.  **Conditional Swap (Row 3):** In the fourth row (index 3), gray (5) pixels remain unchanged.

3.  **Conditional Swap and Mirror (Row 4):**
    *   Gray pixels in row 4 become blue pixels in the output
    *   Blue pixels in row 3 become grey in row 4 in the output.

In summary, the rule in the last two rows swaps blue and grey, maintaining symmetry from input to output. The remaining cells do not change.

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
