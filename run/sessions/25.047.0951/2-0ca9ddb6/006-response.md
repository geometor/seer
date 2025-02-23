# 2-0ca9ddb6 • 006 • Response

---

*text:*

```python
"""
The transformation rule involves identifying single-cell objects and drawing a 3x3 colored frame around each of them, but only if the cell is empty (color 0). The color of the frame depends on the color of the single-cell object.
- If the single-cell object is red (color 2), the frame is yellow (color 4).
- If the single-cell object is blue (color 1), the frame is orange (color 7).
- If the single-cell object has any color other than 1 or 2, there is no framing.
The original single-cell objects are preserved, and all other cells remain unchanged (color 0) unless they are overwritten by a frame.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] != 0:
                is_single_cell = True
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        if (x, y) != (i, j) and input_grid[x, y] != 0:
                            is_single_cell = False
                            break
                    if not is_single_cell:
                        break

                if is_single_cell:
                    if input_grid[i, j] == 2:
                        frame_color = 4
                    elif input_grid[i, j] == 1:
                        frame_color = 7
                    else:
                        continue

                    for x in range(max(0, i - 1), min(rows, i + 2)):
                        for y in range(max(0, j - 1), min(cols, j + 2)):
                            if (x, y) != (i, j) and output_grid[x,y] == 0:
                                output_grid[x, y] = frame_color
    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 7, 1, 7, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0]
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
