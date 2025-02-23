"""
The central vertical line of grey pixels acts as an agent. It transforms its
own pixels to red, then the output grid contracts to only include those pixels,
and finally fills remaining cells with white. Specifically:

1.  **Identify Agent:** Locate the vertical line of grey (color 5) pixels in
    the center column of the input grid.
2.  **Locate Agent Positions:** Get the row indices of *all* pixels belonging
    to the agent (the vertical grey line).
3. **Create Output:** Initialize a 3x3 grid filled with white (0).
4.  **Transform Agent Pixels:** For each row where the agent was present in
    the input, set the corresponding pixel in the output grid to red (2).
    *Crucially*, the column index in the output grid is *always* 1 (the middle
    column), except for input agent rows equal to the middle row
    (input_rows//2), in which case two red pixels are created at (row, 1) and
    (row, 2).
5.  **Output:** The final 3x3 grid.
"""

import numpy as np

def transform(input_grid):
    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    center_col_input = cols // 2
    output_grid = np.zeros((3, 3), dtype=int)

    for r in range(rows):
        if input_array[r, center_col_input] == 5:
            if r == rows // 2:
                output_grid[r, 1] = 2
                output_grid[r, 2] = 2
            else:
                output_grid[r, 1] = 2

    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [1, 1, 0, 5, 0, 1, 0],
        [0, 0, 1, 5, 1, 1, 1],
        [1, 1, 0, 5, 0, 1, 0]
    ]

    expected_output_grid = [
        [0, 2, 0],
        [0, 0, 2],
        [0, 2, 0]
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