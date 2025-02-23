# 6e02f1e3 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
2 2 2
3 2 3
3 3 3
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC475479D0>

**output:**
```
5 0 0
0 5 0
0 0 5
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC47547AC0>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a transformation of a 3x3 grid of single-digit integers (representing colors) to another 3x3 grid of single-digit integers. The input grid contains values 2 and 3 (red and green). The output grid contains values 5 and 0 (gray and white).  The key observation is the diagonal pattern of 5s in the output, and 0s elsewhere. The input has a diagonal of 2s, another of 3s.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    description: Input grid is a 3x3 matrix.
    values: [2, 3]
  - type: grid
    description: Output grid is a 3x3 matrix.
    values: [0, 5]
  - object: diagonal
    description: The main diagonal (top-left to bottom-right) is a prominent feature.
    input_value: 2 #red
    output_value: 5  #grey
  - object: anti-diagonal
    description: The anti-diagonal (top-right to bottom-left) is another prominent feature.
    input_value: 3 #green
    output_value: 5  #grey
  - property: off-diagonal
    description: all other cells that are not on the main diagonal or anti-diagonal
    input_value: varies
    output_value: 0 #white
  - operation: replacement
    description: Values on diagonals become 5 and all others become 0
```


**Natural Language Program:**

1.  **Identify Diagonals:** Locate the main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left) of the input grid.
2.  **Main Diagonal Transformation:** Replace all values along the main diagonal with the value 5 (gray).
3. **Anti-Diagonal Transformation:** Replace all values on the anti-diagonal with the value 5 (gray).
4.  **Off-Diagonal Transformation:** Replace all other values (not on either diagonal) with the value 0 (white).


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
