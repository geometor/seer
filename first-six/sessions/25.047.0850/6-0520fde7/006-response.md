# 6-0520fde7 • 006 Response

---

*text:*

```python
"""
Transformation Rule:

1.  **Identify the central gray object:** In the input grid, there's a vertical line of gray (color code 5) cells.  This acts as our reference.

2.  **Locate Blue Objects:** Note the positions of blue cells (color code 1) in the input.

3.  **Determine Relative Position and Pattern (Row-wise):** For *each* row, compare the number of blue cells to the left and right of the gray line.

4.  **Formulate Output:** Create a 3x3 output grid, initially all white (color code 0).

5.  **Calculate and Update the Output:**
    *   If in a given *row* of the input, there are more blue cells to the *left* of the gray line, the cell in the *first* column of the corresponding row in the output grid is colored red (color code 2).
    *   If there are more blue cells to the *right* of the gray line, the cell in the *last* column of that row in the output is colored red.
    *   If the counts are *equal*, the cell remains white (no change).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the column index of the gray line (color code 5)
    gray_col = -1
    for j in range(cols):
        if np.all(input_grid[:, j] == 5):
            gray_col = j
            break

    if gray_col == -1:  # No gray line found, return all zeros
        return output_grid

    # Count blue cells (color code 1) to the left and right of the gray line for each row
    for r in range(rows):
        left_blue_count = 0
        right_blue_count = 0

        for c in range(cols):
            if input_grid[r, c] == 1:
                if c < gray_col:
                    left_blue_count += 1
                elif c > gray_col:
                    right_blue_count += 1

        if left_blue_count > right_blue_count:
            output_grid[r, 0] = 2  # Left column
        elif right_blue_count > left_blue_count:
            output_grid[r, 2] = 2  # Right Column
        #Equal, no change

    return output_grid.tolist()

if __name__ == '__main__':
    input_grid = [
        [0, 0, 1, 5, 0, 0, 0],
        [1, 1, 0, 5, 1, 0, 1],
        [0, 1, 1, 5, 1, 0, 1]
    ]

    expected_output_grid = [
        [0, 0, 0],
        [2, 0, 0],
        [0, 0, 2]
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
