# 1caeab9d • 014 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 0 0
0 1 0 2 0 0 0 0 0 0
0 1 0 0 0 0 4 0 0 0
0 0 0 0 0 0 4 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x320 at 0x795F858DE320>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 1 0 2 0 0 4 0 0 0
0 1 0 2 0 0 4 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x320 at 0x795F843E4430>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves two grids of colored pixels. The input grid contains several distinct colored objects (blue, red, and yellow) against a background of white pixels (represented by the value 0). The output grid seems to be a modified version of the input grid. The key difference appears to be a vertical stacking or merging of objects of the same color that are vertically adjacent, and the removal of the top row and right-shifting of items in the case where objects in a row are eliminated..

**YAML Fact Block:**


```yaml
facts:
  - observation: "Input and output grids have the same dimensions (5x10)."
  - objects:
      - type: "pixel"
        properties:
          color: ["blue", "red", "yellow", "white"]
          value: [1, 2, 4, 0]
  - relationships:
      - type: "vertical_adjacency"
        condition: "Pixels of the same color are directly above/below each other."
  - actions:
    - type: "merge if same, move down one if not"
    - parameters: vertically combine
      details: "If two vertically adjacent pixels share the same color, they stay. If in any row all objects are eliminated, the row should shift right one."
    - type: "remove_top_row"
      details: "The topmost row in the output grid is always all white."
```


**Natural Language Program:**

1.  **Identify Objects:** Scan the input grid and identify contiguous blocks of pixels with the same color. Consider each of these blocks as a single object.
2.  **Check for Vertical Adjacency and Merge, or move down:** Iterate through the grid, focusing on vertically adjacent pixel pairs.
    *   If two vertically adjacent pixels have the same color, they stay.
    *   If at least one object in a row is not eliminated, the row should be moved down
3.  **Remove Top Row:** After processing vertical adjacency, remove the top-most row of the grid.
4. Ensure empty positions are the background color (0).


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
