# 25.045.1125 • 1-3aa6fb7a • 002 example_1 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F8F07109D80>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7F8F0710A200>

*text:*
**Natural Language Program:**

1. **Identify Objects:** Find all connected regions of color 8 (azure) in the input grid. We consider these regions as distinct objects.
2. **Locate Topmost Cell:** For each region of color 8, determine the cell with the smallest row index. If there are multiple cells with the same smallest row index, choose the one with the smallest column index among them. This cell is the "topmost" cell of the region.
3. **Locate Bottommost Cell:** For each region of color 8, determine the cell with the largest row index. If there are multiple cells with the same largest row index, choose the one with the smallest column index among them. This cell is the "bottommost" cell of the region.
4. **Transform Topmost Neighbor:** For each region, examine the cell immediately to the right of its "topmost" cell. If this neighboring cell is within the grid boundaries and has color 0 (white), change its color to 1 (blue).
5. **Transform Bottommost Neighbor:** For each region, examine the cell immediately to the left of its "bottommost" cell. If this neighboring cell is within the grid boundaries and has color 0 (white), change its color to 1 (blue).
6. **Output:** The grid modified after applying steps 4 and 5 for all regions of color 8 is the final output grid.

This program describes how to identify contiguous regions of color 8 as objects and then modify specific neighboring cells based on the topmost and bottommost cells within each object.
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
