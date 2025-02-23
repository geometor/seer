# 6-0520fde7 • 002 • example_1 - CODE

---

**input**
```
1 0 0 5 0 1 0
0 1 0 5 1 1 1
1 0 0 5 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0
0 2 0
0 0 0
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input to the output grid.

**Observations:**

*   **Input Grid:**
    *   We have a 3x7 grid.
    *   Colors present: 0 (white), 1 (blue), and 5 (gray).
    *   There are distinct vertical lines formed by the blue (1) and gray (5) colors.
*   **Output Grid:**
    *   We have a 3x3 grid.
    *    Colors: only color 2
    *   There is a single red pixel (2) in the center.

**YAML Block:**

```yaml
input_grid:
  size: 3x7
  colors:
    0: white
    1: blue
    5: gray
  objects:
    - type: vertical_line
      color: 1
      positions: [(0,0), (1,1), (0,5), (1,5), (1,6)]
    - type: vertical_line
      color: 5
      positions: [(0,3), (1,3), (2,3)]

output_grid:
  size: 3x3
  colors:
     2: red  
  objects:
     - type: single_pixel
       color: 2
       position: (1,1)
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** In the input grid, locate all vertical lines of color 1 (blue) and color 5 (gray).
2.  **Extract the color from the center of the grid:** If the color in the center of the grid is 5, it becomes 2 in output grid. Otherwise, it is 0.
3.  **Generate Output Grid:** Create a new 3x3 which is filled with color 0, with a centered pixel of color 2.

**In essence,** the transformation focuses on the central vertical line. The output is always a 3x3 grid filled with 0, but the central color extracted (color 2).

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
