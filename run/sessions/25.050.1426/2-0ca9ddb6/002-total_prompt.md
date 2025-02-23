# 2-0ca9ddb6 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

**Natural Language Program: Transformation Rule**

1. **Initialization:** Create a new output grid that is initially identical to the input grid.
2. **Iterate through Input Grid:** Examine each cell in the input grid, row by row, and column by column.
3. **Identify Red Pixels:** If a cell in the input grid contains the color red (color code 2):
    - Consider its horizontal and diagonal neighbors: top-left, top-right, left, right, bottom-left, and bottom-right.
    - For each neighbor position, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor cell in the input grid is white, change the color of the same neighbor cell in the *output* grid to yellow (color code 4).
4. **Identify Blue Pixels:** If a cell in the input grid contains the color blue (color code 1):
    - Consider all eight neighbors: top, bottom, left, right, top-left, top-right, bottom-left, and bottom-right.
    - For each neighbor position, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor cell in the input grid is white, change the color of the same neighbor cell in the *output* grid to orange (color code 7).
5. **Maintain Original Pixels:** The original red and blue pixels in the input grid remain unchanged in the output grid. All other pixels that are not neighbors of red or blue pixels (or whose neighbors in input were not white) also remain unchanged from the input to the output grid.
6. **Output:** The resulting output grid after processing all red and blue pixels in the input grid is the final transformed grid.

**YAML Block: Object Observation and Documentation**

```yaml
task_context: "Grid transformation based on color proximity."
objects:
  - type: "pixel"
    color: "red"
    color_code: 2
    behavior: "Generates yellow border in horizontal and diagonal directions on empty spaces."
  - type: "pixel"
    color: "blue"
    color_code: 1
    behavior: "Generates orange border in all 8 directions on empty spaces."
predicates:
  - "is_red": "Checks if a pixel is red (color code 2)."
  - "is_blue": "Checks if a pixel is blue (color code 1)."
  - "is_white": "Checks if a pixel is white (color code 0)."
  - "is_horizontal_diagonal_neighbor": "Checks if a position is a horizontal or diagonal neighbor."
  - "is_all_neighbor": "Checks if a position is any of the 8 neighbors."
actions:
  - "create_yellow_border": "Sets horizontal and diagonal neighbors to yellow if input neighbor is white."
  - "create_orange_border": "Sets all neighbors to orange if input neighbor is white."
transformation_rule: "For each red pixel, create a yellow border in horizontal and diagonal directions on white input neighbors. For each blue pixel, create an orange border in all directions on white input neighbors."
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
