# 25.045.0658 • 1-3aa6fb7a • 002 example_1 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x722092A11540>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x722092A118D0>

*text:*
**Natural Language Program:**

The transformation rule is as follows:
For every cell in the input grid, we check its current color.
If the cell is white (color 0), we then examine its four immediate neighbors (up, down, left, right).
If at least one of these neighboring cells is azure (color 8), we change the color of the current cell to blue (color 1) in the output grid.
If none of the neighboring cells are azure (color 8), the cell remains white (color 0) in the output grid.
If the cell is already azure (color 8), it remains azure (color 8) in the output grid, and is not modified.
Cells of any other color are also not modified. In this specific example, only colors 0 and 8 are present in the input, and colors 0, 1, and 8 in the output.

**YAML Block:**

```yaml
task_context: "Grid transformation based on neighbor color"
transformation_rule: "For each white cell, if any adjacent cell is azure, change the cell to blue."
objects:
  - type: "cell"
    properties:
      color: ["white", "azure", "blue"]
      position: "grid coordinates"
  - type: "neighbor"
    relation: "adjacent to"
actions:
  - action_type: "check_neighbor_color"
    target_object: "cell"
    neighbor_type: "adjacent"
    condition_color: "azure"
  - action_type: "change_color"
    target_object: "cell"
    new_color: "blue"
    condition: "adjacent azure neighbor exists and cell is white"
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
