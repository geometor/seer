# 25.045.0701 • 1-3aa6fb7a • 002 example_1 - CODE

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76C90CE15510>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76C90CE158A0>

*text:*
```yaml
task_context: "The task involves transforming a grid by identifying regions of color 8 (azure) and modifying cells adjacent to the first and last encountered 8s in reading order."
objects:
  - type: "grid"
    description: "A 2D array of integers representing colors."
  - type: "region"
    color: 8
    description: "Contiguous blocks of cells with color 8."
  - type: "cell"
    properties:
      color: "integer from 0 to 9"
      position: "(row, column) index"
predicates:
  - "is_color_8(cell)" : "Checks if a cell has color 8."
  - "is_color_0(cell)" : "Checks if a cell has color 0."
  - "is_adjacent_right(cell1, cell2)" : "Checks if cell2 is immediately to the right of cell1."
  - "is_adjacent_left(cell1, cell2)" : "Checks if cell2 is immediately to the left of cell1."
  - "is_first_in_reading_order(cell, region_of_8s)" : "Checks if the cell is the first cell with color 8 in reading order within a region."
  - "is_last_in_reading_order(cell, region_of_8s)" : "Checks if the cell is the last cell with color 8 in reading order within a region."
actions:
  - "find_cells_of_color(grid, color)" : "Identifies all cells in the grid with a given color."
  - "get_connected_regions(cells)" : "Groups connected cells into regions."
  - "get_first_cell_in_reading_order(region)" : "Returns the cell from a region that is first in reading order."
  - "get_last_cell_in_reading_order(region)" : "Returns the cell from a region that is last in reading order."
  - "get_cell_to_right(cell)" : "Returns the cell immediately to the right of a given cell."
  - "get_cell_to_left(cell)" : "Returns the cell immediately to the left of a given cell."
  - "change_cell_color(grid, cell, color)" : "Changes the color of a cell in the grid."
transformation_rule: "Identify all cells with color 8. Find the cell with color 8 that is first in reading order (top to bottom, left to right). If the cell immediately to its right is within the grid and has color 0, change its color to 1. Similarly, find the cell with color 8 that is last in reading order. If the cell immediately to its left is within the grid and has color 0, change its color to 1."
```

**Natural Language Program:**

1.  Locate all cells in the input grid that are colored azure (color 8).
2.  Determine the cell among these azure cells that appears first when reading the grid from top to bottom, and left to right within each row. Let's call this the 'first azure cell'.
3.  Examine the cell immediately to the right of the 'first azure cell'. If this cell is within the grid boundaries and is white (color 0), then change its color to blue (color 1).
4.  Determine the cell among the azure cells that appears last in the same reading order (top to bottom, left to right). Let's call this the 'last azure cell'.
5.  Examine the cell immediately to the left of the 'last azure cell'. If this cell is within the grid boundaries and is white (color 0), then change its color to blue (color 1).
6.  The grid resulting from these changes is the final output.
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
