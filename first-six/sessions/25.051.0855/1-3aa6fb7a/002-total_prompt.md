# 1-3aa6fb7a • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**Observations:**

*   **Input Grid:**
    *   We see two distinct objects made of color 8 (azure):
        *   One object is a vertical line of length 2 in the second column.
        *   Another object is a horizontal line of length 2 in the fourth row, starting from the fifth column.
    *   The rest of the grid is filled with color 0 (white).

*   **Output Grid:**
    *   The azure objects (color 8) remain in the same positions.
    *   Two new cells with color 1 (blue) are present:
        *   One is adjacent to the top of the vertical azure line.
        *   One is adjacent to the left of the horizontal azure line.

**Natural Language Program:**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid.
2.  **Vertical Line Rule:** For each vertical line object of color 8, place a color 1 (blue) cell directly above the top cell of the object. Do not add color 1 if a colored cell other than color 0 is above.
3.  **Horizontal Line Rule:** For each horizontal line object of color 8, place a color 1 (blue) cell directly to the left of the leftmost cell of the object. Do not add color 1 if a colored cell other than color 0 is to the left.
4.  **Preserve:** Keep the original color 8 objects in their original positions.
5. **Background:** The background (color 0) is preserved in all other cells.

**YAML Summary:**

```yaml
observations:
  input:
    - object: vertical line
      color: 8
      position: (1,1) # (row, col) of top-left cell
      length: 2
    - object: horizontal line
      color: 8
      position: (3,4)
      length: 2
    - background:
      color: 0
  output:
    - object: vertical line
      color: 8
      position: (1,1)
      length: 2
    - object: horizontal line
      color: 8
      position: (3,4)
      length: 2
    - object: single cell
      color: 1
      position: (1,2)
    - object: single cell
        color: 1
        position: (4,3)
    - background:
      color: 0

transformation_rules:
  - description: |
      Identify all objects composed of color 8.
      Place a cell of color 1 directly above the top of each vertical line object of color 8,
        unless there is not color 0 above the azure object.
      Place a cell of color 1 directly to the left of the leftmost cell of each horizontal line object of color 8,
      unless there is not color 0 to the left.
      Preserve all existing objects of color 8.
```

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
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
