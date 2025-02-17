# 6-0520fde7 • 002 • example_1 - CODE

---

**input**
```
1 0 0 5 0 1 0
0 1 0 5 1 1 1
1 0 0 5 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x192 at 0x7017B1F7FDF0>

**output**
```
0 0 0
0 2 0
0 0 0
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7017B29FBE20>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Summary of Observations**

```yaml
input_grid:
  size: (3, 7)
  objects:
    blue_objects:
      count: 5
      positions: [(0, 0), (0, 5), (1, 1), (1, 5), (1,6), (2, 0)]
    gray_objects:
      count: 3
      positions:  [(0, 3), (1, 3), (2, 3)]
    white_objects:
        count: 13
        positions: all the others

output_grid:
  size: (3, 3)
  objects:
    red_objects:
        count: 1
        positions: [(1,1)]
    white_objects:
      count: 8
      positions: all the others
```

**Natural Language Program: Description of the Transformation Rule**

1.  **Identify the Center:** The output grid is a 3x3 square. Find the center cell of the input grid. In this case the center of the input is at position (1,3).

2.  **Extract Central Object:** Observe the color number in that center cell. The color number there is 5 (grey).

3.  **Count Blue Objects Adjacent to Center:** Count the number of blue (1) objects adjacent to the center gray object (5) at (1, 3) in the input grid. Adjacent includes cells touching by sides, cells touching by corners.

4.  **Place Count Value in Center of output:** Create a 3x3 grid filled with white (0) objects, and place a single object of color "red" (2) in the center of the output grid, IF the number of adjacent blue object is an odd number. If the number is even replace the center by a black (0) object.

**Elaboration and Justification of the Rule**

*   The core concept is to determine the central element of the input, and set to 2 (red) the central element of the output, according the number of blue cells around the central cell.
*   All the other cells are background, and will be set to white (0).


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
