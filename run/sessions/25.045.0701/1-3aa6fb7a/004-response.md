# 25.045.0701 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
Iterate through cells with color 8 in reading order. For the 1st color 8 cell, change the color of the cell below it to 1 if it is 0. For the 4th color 8 cell, change the color of the cell to its right to 1 if it is 0. For the 7th color 8 cell, change the color of the cell to its left to 1 if it is 0.
"""

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = [row[:] for row in input_grid] # Create a copy to avoid modifying the input directly

    azure_cell_counter = 0
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 8:
                azure_cell_counter += 1
                if azure_cell_counter == 1:
                    # 1st azure cell: check cell below
                    below_r = r + 1
                    if 0 <= below_r < rows and output_grid[below_r][c] == 0:
                        output_grid[below_r][c] = 1
                elif azure_cell_counter == 4:
                    # 4th azure cell: check cell to the right
                    right_c = c + 1
                    if 0 <= right_c < cols and output_grid[r][right_c] == 0:
                        output_grid[r][right_c] = 1
                elif azure_cell_counter == 7:
                    # 7th azure cell: check cell to the left
                    left_c = c - 1
                    if 0 <= left_c < cols and output_grid[r][left_c] == 0:
                        output_grid[r][left_c] = 1

    return output_grid


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
