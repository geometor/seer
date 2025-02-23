# 25.044.1353 • 1-3aa6fb7a • 003 example_2 - NLP

---

```
example_1_input = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

example_1_output = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
```

input
<PIL.Image.Image image mode=RGB size=448x448 at 0x70C76BA11DE0>
output
<PIL.Image.Image image mode=RGB size=448x448 at 0x70C76BA12170>

*text:*
**Natural Language Program:**

1. **Identify the objects:** The objects are cells in a 7x7 grid. Each cell has a numerical value (0, 1, or 8).
2. **Identify the predicate:** We are interested in cells that have a value of 0 and their neighbors.
3. **Describe the transformation:** For every cell in the input grid:
    - Check if the cell's value is 0.
    - If it is 0, examine its immediate neighbors (up, down, left, right) in the *input* grid.
    - If any of these neighbors has a value of 8, then change the value of the current cell in the *output* grid to 1.
    - If the cell's value is not 0, or if none of its neighbors are 8, keep the cell's original value in the *output* grid.

**In simpler terms:**

For each empty cell (value 0) in the input grid, if any of its adjacent cells (up, down, left, or right) in the input grid is an '8', then fill this empty cell with '1' in the output grid. Otherwise, leave the cell as it is. Cells with values other than 0 are unchanged in the output.

*text:*
```python
"""
For each empty cell (value 0) in the input grid, if any of its adjacent cells (up, down, left, or right) in the input grid is an '8', then fill this empty cell with '1' in the output grid. Otherwise, leave the cell as it is. Cells with values other than 0 are unchanged in the output.
"""

def transform(input_grid):
    # Get the dimensions of the input grid
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    # Initialize the output grid as a copy of the input grid
    output_grid = [row[:] for row in input_grid]

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0:
                # Check neighbors for value 8
                neighbors = [
                    (r - 1, c),  # Up
                    (r + 1, c),  # Down
                    (r, c - 1),  # Left
                    (r, c + 1)   # Right
                ]
                found_neighbor_8 = False
                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols and input_grid[nr][nc] == 8:
                        found_neighbor_8 = True
                        break
                if found_neighbor_8:
                    output_grid[r][c] = 1

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

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
```

```
example_2_input = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

example_2_output = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]
```

input
<PIL.Image.Image image mode=RGB size=448x448 at 0x70C76BA11FC0>
output
<PIL.Image.Image image mode=RGB size=448x448 at 0x70C76BA12230>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
