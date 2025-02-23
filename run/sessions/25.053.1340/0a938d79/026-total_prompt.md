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

<PIL.Image.Image image mode=RGB size=512x1536 at 0x7398A1083700>

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

<PIL.Image.Image image mode=RGB size=512x1536 at 0x7398A0F416C0>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves 2D grids containing numerical values representing colors. The primary elements are individual cells (pixels) within the grids, characterized by their color (represented by a digit) and position (row and column indices). The input grid appears to be transformed into the output grid based on some rule involving the replication and positioning of specific colored rows. Specifically, rows with non-zero single pixels are replaced with multiple, solid colored, rows.

**YAML Block (Facts):**


```yaml
objects:
  - name: grid
    type: 2D array
    properties:
      - rows: list of rows
      - columns: list of columns
      - cells: individual elements within the grid, each with a color value

  - name: cell
    type: pixel
    properties:
      - color: integer (0-9)
      - row_index: integer
      - column_index: integer

actions:
  - name: identify_colored_rows
    description: Find rows containing exactly one non-zero pixel.
  - name: replicate_color
    description: Create new rows filled entirely with the identified color.
  - name: insert_rows
    description: insert replicated color rows into the output.

relationships:
  - type: spatial
    description: Cells are arranged in a grid structure, with row and column relationships.
  - type: transformation
    description: The input grid is transformed into the output grid by replicating rows containing specific color.
```


**Natural Language Program:**

1.  **Identify Key Rows:** Scan the input grid row by row. Identify rows that contain *exactly one* non-zero pixel. Note the color of that pixel and the row index.

2.  **Replicate and Insert:** For each identified row:
    *   Create multiple copies of a new row, where *all* pixels in the new row are of the color found in the original, key, row.
    *   The number of replicated rows should match the height of the original image.
    *  Insert the new replicated rows in blocks maintaining the order they were found in the original input.

3. **Assemble output:** The result of inserting the replicated rows is the final output grid.

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
