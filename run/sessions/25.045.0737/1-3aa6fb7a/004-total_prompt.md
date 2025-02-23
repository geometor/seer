# 25.045.0737 • 1-3aa6fb7a • 004 example_2 - CODE

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

*text:*
```python
"""
The task is to modify the input grid based on the presence of color 8 (azure).
For each cell in the grid, we check if its value is 0 (white).
If it is 0, we then examine its immediate left and right neighbors in the same row.
If either the left neighbor or the right neighbor has a value of 8 (azure), we change the value of the current cell to 1 (blue) in the output grid.
If neither neighbor is 8, or if the original cell value is not 0, we keep the original cell value unchanged in the output grid.
When checking neighbors, we need to handle boundary cases. If a cell is on the left edge, it has no left neighbor; if it's on the right edge, it has no right neighbor. In these cases, we only consider the existing neighbor.
"""

import copy

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)

    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0:
                # Check left neighbor
                left_neighbor_is_8 = False
                if c > 0 and input_grid[r][c-1] == 8:
                    left_neighbor_is_8 = True

                # Check right neighbor
                right_neighbor_is_8 = False
                if c < cols - 1 and input_grid[r][c+1] == 8:
                    right_neighbor_is_8 = True

                if left_neighbor_is_8 or right_neighbor_is_8:
                    output_grid[r][c] = 1

    return output_grid


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

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7711C150DB40>

**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7711C150D360>

*text:*
**Natural Language Program:**

The task is to transform the input grid by examining each cell.
For every cell in the grid, we check its color.
If the cell's color is 0 (white), we then look at its immediate horizontal neighbors: the cell to its left and the cell to its right in the same row.
If either the left neighbor or the right neighbor has a color of 8 (azure), we change the color of the current cell to 1 (blue) in the output grid.
If neither the left nor the right neighbor has a color of 8, or if the original cell's color was not 0, we retain the original color of the cell in the output grid.
When considering neighbors, we must be mindful of grid boundaries. Cells on the left edge have no left neighbor, and cells on the right edge have no right neighbor. In these cases, we only check for the existing neighbor if applicable.
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
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
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
