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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74F516190F70>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74F5161907F0>

*text:*
**Natural Language Program:**

1. **Identify Objects:** Detect all connected regions of color 8 (azure) in the input grid. These regions are considered as distinct objects.
2. **Sort Objects:** Order the identified objects from left to right based on their horizontal position. The horizontal position of an object is determined by the minimum column index among all cells belonging to that object.
3. **Leftmost Object Action:** For the object that is leftmost in the sorted order:
    - Find its topmost cell. The topmost cell is the cell with the minimum row index among all cells of this object.
    - Locate the cell immediately to the right of this topmost cell. If this cell is within the grid boundaries, change its color to 1 (blue).
4. **Rightmost Object Action:** For the object that is rightmost in the sorted order:
    - Find its bottommost cell. The bottommost cell is the cell with the maximum row index among all cells of this object.
    - Locate the cell immediately to the left of this bottommost cell. If this cell is within the grid boundaries, change its color to 1 (blue).
5. **Output:** The grid obtained after applying these changes is the output grid.

**YAML Block:**

```yaml
task_context: "ARC-AGI grid puzzle transformation"
transformation_rule: "Identify connected components of color 8, sort them horizontally, and modify cells adjacent to the leftmost and rightmost components."
objects:
  - type: "connected region"
    color: 8 # azure
predicates:
  - "connected": "cells of the same color are adjacent (horizontally or vertically)"
  - "leftmost": "object with the minimum starting column index"
  - "rightmost": "object with the maximum starting column index"
  - "topmost": "cell with the minimum row index within an object"
  - "bottommost": "cell with the maximum row index within an object"
actions:
  - "identify": "detect connected regions of color 8"
  - "sort": "order objects based on their leftmost column"
  - "change_color": "modify cell color to 1 (blue)"
  - "locate_adjacent_cell": "find cell immediately to the right or left of a given cell"
steps:
  - "Identify all connected components of color 8."
  - "Sort these components based on their minimum column index (left to right)."
  - "For the leftmost component, find its topmost cell and change the color of the cell immediately to its right to 1."
  - "For the rightmost component, find its bottommost cell and change the color of the cell immediately to its left to 1."
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
