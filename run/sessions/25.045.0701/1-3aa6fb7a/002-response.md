# 25.045.0701 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
The task involves transforming a grid by identifying regions of color 8 (azure) and modifying cells adjacent to the first and last encountered 8s in reading order.
Specifically, find the first and last cells with color 8 in reading order (top to bottom, left to right).
If the cell to the right of the first cell is within the grid and has color 0, change its color to 1.
If the cell to the left of the last cell is within the grid and has color 0, change its color to 1.
"""

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = [row[:] for row in input_grid] # Create a copy to avoid modifying the input directly

    cells_of_8 = []
    for r in range(rows):
        for c in range(cols):
            if output_grid[r][c] == 8:
                cells_of_8.append((r, c))

    if not cells_of_8:
        return output_grid # No cells of color 8, return original grid

    first_cell_8 = cells_of_8[0]
    last_cell_8 = cells_of_8[-1]

    first_r, first_c = first_cell_8
    last_r, last_c = last_cell_8

    # Check right of first cell
    right_c_first = first_c + 1
    if 0 <= right_c_first < cols and output_grid[first_r][right_c_first] == 0:
        output_grid[first_r][right_c_first] = 1

    # Check left of last cell
    left_c_last = last_c - 1
    if 0 <= left_c_last < cols and output_grid[last_r][left_c_last] == 0:
        output_grid[last_r][left_c_last] = 1

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
