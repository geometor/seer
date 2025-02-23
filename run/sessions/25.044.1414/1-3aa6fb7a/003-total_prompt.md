# 25.044.1414 • 1-3aa6fb7a • 003 example_2 - NLP

---

**input**
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x7708A5C195A0>
**output**
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x7708A5C19930>

*text:*
**Natural Language Program:**

1. **Identify Corner '8's:** Locate cells in the input grid that contain the value '8' and have exactly two neighboring cells that also contain the value '8'. These '8' cells are considered the corners of potential "L" shapes.

2. **Find '8'-Neighbors:** For each identified corner '8', determine its two neighboring cells that contain '8'.

3. **Calculate Missing Corner Position:**  Using the coordinates of the corner '8' cell and its two '8'-neighbor cells, calculate the coordinates of the 'missing corner' that would complete a 2x2 square. The formula for calculating the missing corner coordinates (row_missing, column_missing) is:
   `row_missing = row_neighbor1 + row_neighbor2 - row_corner`
   `column_missing = column_neighbor1 + column_neighbor2 - column_corner`
   where (row_corner, column_corner) are the coordinates of the corner '8', and (row_neighbor1, column_neighbor1), (row_neighbor2, column_neighbor2) are the coordinates of its two '8'-neighbors.

4. **Check and Fill:** Examine the cell in the input grid at the calculated 'missing corner' coordinates. If this cell contains the value '0', then in the output grid, change the value of this cell to '1'.

5. **Maintain Unchanged Cells:** For all other cells in the grid that are not modified in step 4, their values in the output grid remain the same as they were in the input grid.

This program effectively identifies "L" shapes formed by '8's and fills in the 'missing corner' with a '1' if it was originally a '0'.

*text:*
```python
"""
1. Identify Corner '8's: Locate cells in the input grid that contain the value '8' and have exactly two neighboring cells that also contain the value '8'.
2. Find '8'-Neighbors: For each identified corner '8', determine its two neighboring cells that contain '8'.
3. Calculate Missing Corner Position: Calculate the coordinates of the 'missing corner' to complete a 2x2 square.
4. Check and Fill: If the cell at the 'missing corner' is '0', change it to '1' in the output grid.
5. Maintain Unchanged Cells: Keep other cells unchanged.
"""

def transform(input_grid):
    # initialize output grid as a copy of the input grid
    output_grid = [row[:] for row in input_grid]
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 8:
                neighbor_8s = []
                # Check 4 neighbors (up, down, left, right)
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 8:
                        neighbor_8s.append((nr, nc))

                # Identify corner '8's (those with exactly two '8' neighbors)
                if len(neighbor_8s) == 2:
                    r1, c1 = neighbor_8s[0]
                    r2, c2 = neighbor_8s[1]

                    # Calculate missing corner position
                    missing_r = r1 + r2 - r
                    missing_c = c1 + c2 - c

                    # Check if the missing corner is within grid bounds and is '0'
                    if 0 <= missing_r < rows and 0 <= missing_c < cols and input_grid[missing_r][missing_c] == 0:
                        output_grid[missing_r][missing_c] = 1 # Fill with '1'

    return output_grid


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output_grid = transform(input_grid)

    if output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid)

    print()
    assert output_grid == expected_output_grid, "Transformed output does not match expected output."
```

**input**
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x7708A5C19B10>
**output**
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0<PIL.Image.Image image mode=RGB size=448x448 at 0x7708A5C19240>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
