# 25.045.0737 • 1-3aa6fb7a • 002 example_1 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7711C150D5D0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7711C150D960>

*text:*
**Natural Language Program:**

The task is to modify the input grid based on the presence of color 8 (azure).
For each cell in the grid, we check if its value is 0 (white).
If it is 0, we then examine its immediate left and right neighbors in the same row.
If either the left neighbor or the right neighbor has a value of 8 (azure), we change the value of the current cell to 1 (blue) in the output grid.
If neither neighbor is 8, or if the original cell value is not 0, we keep the original cell value unchanged in the output grid.
When checking neighbors, we need to handle boundary cases. If a cell is on the left edge, it has no left neighbor; if it's on the right edge, it has no right neighbor. In these cases, we only consider the existing neighbor.

**YAML Block:**

```yaml
task_context: Grid transformation
transformation_rule: Change 0 to 1 if horizontally adjacent to 8
objects:
  - type: cell
    properties:
      color: integer (0-9)
predicates:
  - is_zero: cell.color == 0
  - is_eight: cell.color == 8
  - is_horizontally_adjacent_to_eight: cell is horizontally adjacent to a cell with color 8
actions:
  - change_color_to_one: set cell.color = 1
transformation_steps:
  - For each cell in the input grid:
    - Check if the cell's color is 0.
    - If yes, check its left and right neighbors.
    - If the left neighbor's color is 8 OR the right neighbor's color is 8, change the current cell's color to 1 in the output grid.
    - Otherwise, keep the cell's color as 0 in the output grid.
  - If the cell's color is not 0, keep it unchanged in the output grid.
```
**Instructions**

- Generate a complete Python module to be run in your code_execution to
  represent the natural language program 
- Follow the template below
- If your code fails to achieve a match - analyze the expected and generated
  outputs and try to run the code again 

**Transform Template:**

```python
"""
{ natural language description of the transformation rule }
"""

{ allowed imports that support the transform }

def transform(input):
    # initialize output

    # change output pixels 

    return output


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."

```
