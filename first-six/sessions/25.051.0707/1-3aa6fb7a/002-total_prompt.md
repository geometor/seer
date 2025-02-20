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

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two 2x1 vertical lines
        positions:
          - (1,1), (2,1)  # First line
          - (4,4), (5,4)  # Second line
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two 2x1 vertical lines
        positions:
          - (1,1), (2,1)
          - (4,4), (5,4)
      - color: 1 (blue)
        shape: single cells
        positions:
          - (1,2)
          - (4,4)
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
```

**Natural Language Description of Transformation:**

1.  **Identify Objects:** In the input grid, we have two vertical lines of color 8 (azure), each two cells high. The rest of the grid is filled with color 0 (white).

2.  **Detect Changes:** We can see changes in the output inside each one of the azure lines. In the output grid, the azure lines that were found in the input, are kept intact.

3.  **Describe Action:** Within each azure line, the program searches for the cell located immediately to the right of the top cell of each vertical line. The color of this cell is changed to 1 (blue). If the cell to the right of the bottom cell of each line is also azure, it keeps its original color.

**Natural Language Program**
```
for each vertical azure line in the input:
    find top_cell
    find right_neighbor = cell to the right of the top_cell
    set color of right_neighbor to blue
    
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
