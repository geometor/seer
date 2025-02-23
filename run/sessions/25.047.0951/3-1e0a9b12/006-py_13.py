"""
1.  **Identify Non-Zero Objects:** Locate all the colored cells (non-zero values) in the input grid.
2.  **Move Objects to the Bottom:** Move all the identified non-zero objects down to the last rows of the output grid.
3. **Preserve Horizontal Order**: When moving objects maintain their original horizontal order. The objects will stack on top of each other starting from the last row.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    non_zero_elements = []

    # Collect non-zero elements with their column indices
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] != 0:
                non_zero_elements.append((j, input_grid[i, j]))  # (column, value)

    # Sort by column index
    non_zero_elements.sort()

    # Fill the output grid from the bottom up
    row = output_grid.shape[0] - 1
    col_index = 0
    for col, value in non_zero_elements:
        while output_grid[row, col] != 0 and row > 0 :
          row -= 1
        output_grid[row, col] = value
          

    return output_grid


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 1, 0],
        [0, 3, 0, 0, 0],
        [0, 3, 0, 1, 2],
        [6, 0, 0, 0, 0],
        [0, 3, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0],
        [0, 3, 0, 1, 0],
        [6, 3, 0, 1, 2]
    ]

    output_grid = transform(input_grid)

    if (output_grid == np.array(expected_output_grid)).all():
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:\n", np.array(expected_output_grid))
        print("Transformed Output:\n", output_grid)

    print()
    assert (output_grid == np.array(expected_output_grid)).all(), "Transformed output does not match expected output."