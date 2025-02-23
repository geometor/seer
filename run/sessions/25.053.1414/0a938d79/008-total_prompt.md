# 0a938d79 • 008 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1472x448 at 0x7D261845B9D0>

**output:**
```
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 3 0 0 1 0 0 3 0 0 1 0 0 3 0 0
```

<PIL.Image.Image image mode=RGB size=1472x448 at 0x7D26184F12A0>
Okay, here's my analysis of the example input-output pair, presented as a report:

**Perception of Elements:**

The task involves a transformation of a 2D grid of single-digit integers (representing colors) to another 2D grid of the same dimensions. The input grid seems to contain mostly 0s (white), with a few instances of 1 (blue) and 3 (green). The output grid has the same dimensions, but the single instances of '1' and '3' in the input seem to have been replicated to create a repeating pattern of alternating '1' and '3' values across the entire row and maintains the initial column placement.

**YAML Fact Documentation:**


```yaml
facts:
  - observation: "Input and output grids have the same dimensions."
  - object: grid
    properties:
      - dimensions: 2D array (rows x columns)
      - cells: "contain single-digit integers (0-9)"
      - color_map: "0: white, 1: blue, 3: green"
  - object: cell
    properties:
      - value: integer (0-9)
      - color: "determined by color_map"
      - position: (row, column)
  - action: replication
    description: "Values 1 and 3 are replicated horizontally."
    details: "The replication alternates between 1 and 3 across the entire row, starting with the original position of the digit."
  - relationship: "positional_transformation"
    description: "Non-zero values in the input grid trigger a horizontal replication in the output grid at the same row."
```


**Natural Language Program:**

1.  **Identify Dimensions:** Determine the number of rows and columns of the input grid. The output grid will have the same dimensions.
2.  **Initialize Output:** Create an output grid filled with 0s (white), matching the input grid's dimensions.
3.  **Iterate Rows:** For each row in the input grid:
    *   **Iterate Columns:** For each cell (pixel) in the current row:
        *    Check Value: Examine current input cell value.
        *    **Replication Rule:**
             *   If the input cell's value is 1 (blue):
                 *   Starting at current column, fill the output row, alternating between 1 and 3 until the end of the row.
             *   If the input cell's value is 3 (green):
                 *   Starting at current column, fill the output row, alternating between 3 and 1 until the end of the row.
             * If the input is 0, leave corresponding output cell as 0

In essence the program scans each row of the input. When it finds a 1 or a 3, it replaces the rest of the row with an alternating sequence of 1s and 3s (or 3s and 1s), starting with the value that was found. The column position of the initial digit is preserved.

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
