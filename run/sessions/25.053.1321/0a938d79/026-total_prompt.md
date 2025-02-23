# 0a938d79 • 026 • example_4 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=512x1536 at 0x7415308F9270>

**output:**
```
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4
```

<PIL.Image.Image image mode=RGB size=512x1536 at 0x741530570910>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves 2D grids where each cell contains a single digit representing a color. The primary elements are:

*   **Single-color rows:** Rows containing only one color (besides white/0).
*   **Color Propagation:**  The non-white color in a single-color row appears to be replicated.
*   **Pattern Repetition:** The replicated color forms a repeated pattern of rows.

**YAML Fact Block:**


```yaml
facts:
  - observation: |
      Input grids contain rows with a single non-zero (non-white) color, potentially mixed with zeros.
  - observation: |
      Output grids contain rows of the same colors observed in single color rows of input.
  - observation: |
    The colors are replicated and creating a pattern
  - relationship: |
      The single non-zero color rows in the input correspond to patterned color blocks in the output.
  - action: The single color is extended into a row.
  - action: The single color row is copied multiple times.
```


**Natural Language Program:**

1.  **Identify Significant Rows:** Scan the input grid to find rows that contain exactly one non-zero (non-white) color value, and the rest are zeros.
2.  **Expand Rows:** For each significant row found, expand the single non-zero color to fill the entire row.
3. **Create Pattern**: Copy rows from top to bottom, replicating the row below the single color row twice, and repeating the pattern to the bottom of the grid.


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
