# 25.045.0717 • 1-3aa6fb7a • 002 example_1 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x77A55E30D570>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x77A55E30D900>

*text:*
**Natural Language Program:**

The task is to identify and modify cells within connected regions of color 8 (azure).
1. **Identify Connected Regions:** Find all contiguous regions of color 8 in the input grid. Two cells are considered connected if they are adjacent horizontally or vertically and have the same color.
2. **Order the Regions:**  For each connected region, find its "top-leftmost" cell. The top-leftmost cell is defined as the cell with the smallest row index, and among those with the same smallest row index, the smallest column index. Order the regions based on their top-leftmost cells, first by row index and then by column index in ascending order. Let's call the regions Region 1 and Region 2 based on this order.
3. **Modify Region 1:** In Region 1, locate its top-leftmost cell and change its color to 1 (blue).
4. **Modify Region 2:** In Region 2, locate its bottom-rightmost cell. The bottom-rightmost cell is defined as the cell with the largest row index, and among those with the same largest row index, the largest column index. Change the color of this bottom-rightmost cell to 1 (blue).

**YAML Block:**

```yaml
task_context: "Grid transformation"
transformation_rule: "Modify cells in connected regions of color 8. For the first region (ordered by top-leftmost cell), change its top-leftmost cell to color 1. For the second region, change its bottom-rightmost cell to color 1."
objects:
  - type: "connected region"
    color: 8
    properties:
      - "top-leftmost cell"
      - "bottom-rightmost cell"
actions:
  - "identify connected regions of color 8"
  - "order regions based on top-leftmost cell position"
  - "change color of top-leftmost cell of the first region to 1"
  - "change color of bottom-rightmost cell of the second region to 1"
predicates:
  - "connected"
  - "same color"
  - "top-leftmost"
  - "bottom-rightmost"
  - "first region"
  - "second region"
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
