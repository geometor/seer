"""
The transformation rule can be described as follows:

1.  **Identify the Object:** Locate the contiguous region of color '5' in the input grid.

2.  **Bounding Box (Implicit):**  As before, a bounding box can be conceptually imagined around the "5" shaped object, though it's not explicitly used in the color-changing logic.

3. **Color Substitution within the bounding box:** The transformation recolors portions of the object of '5'.

4.  **Recolor Rule**:
    *   Consider the coordinates where the color is 5.
    *   If those coordinates have a row index of 1 or 2, then it must be considered whether the column index is 3 or less. If it's less or equal to 3, then it is recolored to 8. If it's more than 3, then the cell is recolored to 2.
    *   If the row index is greater or equal to 3:
        * If the column position is 3, and the color is 5, then change it to 2.
        * if the column position is greater than 3, and the color is 5, then change it to 8.

**Step-by-step explanation (symbolic):**

1.  Find the connected component of color 5.
2.  Iterate through all the color 5 cells of the identified object.
3.  If the cell at (row, col) has color 5:
    *   If `row` is 1 or 2:
        *   If `col` <= 3, change the color to 8.
        *   If `col` > 3, change the color to 2.
    *   If `row` >=3:
        *   If `col`==3, change color to 2.
        *   If `col` > 3, change color to 8.

4.  The background (color 0) remains unchanged.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    rows, cols = input_grid.shape

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 5:
                if r in (1, 2):
                    if c <= 3:
                        output_grid[r,c] = 8
                    else:
                        output_grid[r,c] = 2
                elif r >= 3:
                    if c == 3:
                        output_grid[r, c] = 2
                    elif c > 3:
                        output_grid[r, c] = 8


    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 5, 5, 5, 5, 5, 0, 0, 0],
        [0, 5, 5, 5, 5, 5, 5, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
        [0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 8, 2, 8, 8, 2, 0, 0, 0],
        [0, 8, 8, 2, 8, 8, 2, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 2, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 2, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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