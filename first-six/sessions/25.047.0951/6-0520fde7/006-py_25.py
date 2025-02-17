"""
The central vertical line of grey pixels acts as an agent. It transforms some
of its pixels to red in a new 3x3 grid, then the output grid contracts, and
finally remaining cells are filled with white. The specific transformation
depends on the row index of the agent's pixels:

1.  **Identify Agent:** Locate the vertical line of grey (color 5) pixels in
    the center column of the input grid.
2.  **Locate Agent Positions:** Get the row indices of *all* pixels belonging
    to the agent.
3.  **Create Output:** Initialize a 3x3 grid filled with white (0).
4.  **Transform Agent Pixels:** For each row `r` where the agent was present
    in the input:
    *   If `r` is the middle row of the *input* grid (`r == rows // 2`), set
        the output pixel at `(r, 2)` to red (2).
    *   Otherwise, set the output pixel at `(r, r - rows + 1)` to red (2).
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
                output_grid[r, 2] = 2
            else:
                output_grid[r, r - rows + 1] = 2

    return output_grid.tolist()


if __name__ == '__main__':
    # Test Case 1
    input_grid1 = [
        [1, 0, 0, 5, 0, 1, 0],
        [0, 1, 0, 5, 1, 1, 1],
        [1, 0, 0, 5, 0, 0, 0]
    ]

    expected_output_grid1 = [
        [0, 0, 0],
        [0, 2, 0],
        [0, 0, 0]
    ]
    output_grid1 = transform(input_grid1)
    print(f"Test Case 1: {'SUCCESS' if output_grid1 == expected_output_grid1 else 'FAILED'}")
    assert output_grid1 == expected_output_grid1

    # Test Case 2
    input_grid2 = [
        [1, 1, 0, 5, 0, 1, 0],
        [0, 0, 1, 5, 1, 1, 1],
        [1, 1, 0, 5, 0, 1, 0]
    ]
    expected_output_grid2 = [
        [0, 2, 0],
        [0, 0, 2],
        [0, 2, 0]
    ]
    output_grid2 = transform(input_grid2)
    print(f"Test Case 2: {'SUCCESS' if output_grid2 == expected_output_grid2 else 'FAILED'}")
    assert output_grid2 == expected_output_grid2
    

    # Test Case 3
    input_grid3 = [
      [0, 0, 1, 5, 0, 0, 0],
      [1, 1, 0, 5, 1, 0, 1],
      [0, 1, 1, 5, 1, 0, 1]
    ]

    expected_output_grid3 = [
      [0, 0, 0],
      [2, 0, 0],
      [0, 0, 2]
    ]
    output_grid3 = transform(input_grid3)
    print(f"Test Case 3: {'SUCCESS' if output_grid3 == expected_output_grid3 else 'FAILED'}")
    assert output_grid3 == expected_output_grid3