# 1e32b0e9 • 014 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 3 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 3 0 3 0 1 0 3 0 0 0 1 0 0 0 3 0
0 0 3 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 3 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 3 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 3 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1088x1088 at 0x795F843E7250>

**output:**
```
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 3 0 0 1 0 0 1 0 0 1 0 0 1 0 0
0 3 0 3 0 1 0 3 0 1 0 1 0 1 0 3 0
0 0 3 0 0 1 0 0 1 0 0 1 0 0 1 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 3 0 0 1 0 0 1 0 0 1 0 0 1 0 0
0 3 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 3 0
0 0 1 0 0 1 0 0 1 0 0 1 0 0 3 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1088x1088 at 0x795F843E6530>
Okay, here's a breakdown of my observations and proposed transformation rule for the provided example:

**Perception of Elements:**

*   **Grid Structure:** The input and output are grids of identical dimensions (17x17).
*   **Colors:**  Predominant colors are white (0), blue (1), and green (3).
*   **Horizontal Lines:** There are solid blue lines that span the grid horizontally.
*   **Vertical Lines of 1s:** There are broken or partial columns, made by blue (1) cells.
*   **Green (3) Placement:** Green cells appear to exist in the input, and interact with the vertical blue lines in some way.

**YAML Fact Block:**


```yaml
facts:
  - object: horizontal_lines
    type: line
    color: blue
    description: Continuous horizontal lines spanning the width of the grid.
    properties:
      - constant: true
  - object: vertical_lines
    type: line
    color: blue
    description: Discontinuous vertical lines made of blue cells.
     properties:
      - constant: false
  - object: green_cells
    type: cell
    color: green
    description: Isolated green cells.
    properties:
      - constant: false
  - observation: |
      Vertical blue lines are extended downwards and up, one cell at a time, where ever a green does NOT appear to be adjacent.
  - observation: |
      If a green is adjacent, do not place a blue.

```


**Natural Language Program:**

1.  **Identify Constant Elements:** The horizontal blue lines remain unchanged between the input and output. Preserve them.

2.  **Vertical Line Extension:** For each column, identify existing blue (1) cells that are part of a vertical line.

3. **Green Cell as a Blocker:**
      Locate green cells (value 3)
4.  **Extend Blue, Avoid Green:**
    *   Extend the existing blue vertical lines downwards and upwards, one cell at a time, adding a blue cell to the line.
    *   Do **not** extend the blue line into any cell adjacent to a green cell, *either vertically or horizontally*.

In essence, the transformation rule takes the existing vertical blue lines and extends them, but the green cells act as "blockers," preventing the blue lines from expanding into adjacent cells.

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
