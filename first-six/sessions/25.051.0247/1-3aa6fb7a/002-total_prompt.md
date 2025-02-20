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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
observations:
  input_objects:
    - color: 8 (azure)
      shape: two separate 2x1 vertical rectangles
      position: 
        - One rectangle at (row 1, col 1) and (row 2, col 1)
        - One rectangle at (row 3, col 4) and (row 4, col 4)
    - color: 0 (white)
      shape: background
      position: fills the entire grid

  output_objects:
    - color: 8 (azure)
      shape: two separate 2x1 vertical rectangles
      position: Same as in the input
        - One rectangle at (row 1, col 1) and (row 2, col 1)
        - One rectangle at (row 3, col 4) and (row 4, col 4)
    - color: 1 (blue)
      shape: two single cells.
      position:
        - One cell at (row 1, col 2) directly to the right of the first azure rectangle
        - One cell at (row 4, col 5) directly to the left of the second azure rectangle
    - color: 0 (white)
      shape: background
      position: fills the entire grid

```

**Natural Language Description of Transformation Rule:**

1.  **Identify Objects:** In the input grid, we observe two distinct azure (color 8) objects. Each object is a 2x1 vertical rectangle. The remaining cells are white (color 0), forming the background.

2.  **Preserve Azure Objects:** The two azure rectangles remain unchanged in their position and shape in the output grid.

3. **Place Blue next to objects:** 
    For the azure object on the left side of the grid, a new single blue cell (color 1) is generated adjacent to the object right border, in the middle of the object y axis.
    For the azure object on the right side, a new single blue cell (color 1) is generated adjacent to the object left border, in the middle of the object y axis.

4. **Background remains:** The rest of the background color is unchanged.

**Step-by-step transformation:**

1.  Copy the two azure rectangles from the input to the output grid.
2.  Locate the azure rectangle on the left. Add a blue cell to its immediate right in the middle of the object height.
3.  Locate the azure rectangle on the right. Add a blue cell to its immediate left in the middle of the object height.
4.  The white background remains the same.

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
