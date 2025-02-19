# 3bd67248 • 002 • example_1 - CODE

---

**input**
```
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
6 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=960x960 at 0x79CABAB79CF0>

**output**
```
6 0 0 0 0 0 0 0 0 0 0 0 0 0 2
6 0 0 0 0 0 0 0 0 0 0 0 0 2 0
6 0 0 0 0 0 0 0 0 0 0 0 2 0 0
6 0 0 0 0 0 0 0 0 0 0 2 0 0 0
6 0 0 0 0 0 0 0 0 0 2 0 0 0 0
6 0 0 0 0 0 0 0 0 2 0 0 0 0 0
6 0 0 0 0 0 0 0 2 0 0 0 0 0 0
6 0 0 0 0 0 0 2 0 0 0 0 0 0 0
6 0 0 0 0 0 2 0 0 0 0 0 0 0 0
6 0 0 0 0 2 0 0 0 0 0 0 0 0 0
6 0 0 0 2 0 0 0 0 0 0 0 0 0 0
6 0 0 2 0 0 0 0 0 0 0 0 0 0 0
6 0 2 0 0 0 0 0 0 0 0 0 0 0 0
6 2 0 0 0 0 0 0 0 0 0 0 0 0 0
6 4 4 4 4 4 4 4 4 4 4 4 4 4 4
```

<PIL.Image.Image image mode=RGB size=960x960 at 0x79CABB63AA10>
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    objects:
      - color: 6
        shape: vertical_line
        position: (0, all) # First column, all rows
        count: 15
      - color: 0
        shape: rectangle
        position: (1-14, 0-14) # All rows except the first, all columns
        count: 210  
  output_grid:
    objects:
      - color: 6
        shape: vertical_line
        position: (0, all)
        count: 15
      - color: 2
        shape: diagonal_line
        position: (0-14, 14-0) # From bottom-left to top-right
        count: 15
      - color: 4
        shape: horizontal line
        position: (14, 0-14)
        count: 15
      - color: 0
        shape: fill
        position: (0-14, 0-14)
```

**Natural Language Program:**

1.  **Identify the magenta line:** In the input grid, there is a vertical line of magenta (color 6) pixels along the leftmost edge.

2.  **Create a diagonal of red pixels:** Create a diagonal line from the bottom left corner (coordinates (14,0) and going upwards to the top right corner (coordinates (0,14) of color red (color code 2).

3.  **Create a yellow line:** The last row keeps color 0, except the last row is changed to yellow (color 4).

4.  **Everything else:** Preserve the white cells (color 0).

**Explanation of the Rule**
The input is composed by a column of 6 and the rest is 0.
The output is formed by:
- a diagonal line of 2 from bottom left to top right
- last row is made of 4
- the first column is made of 6
- the rest is 0.


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
