"""
Here, again the central grey object is an agent. It leaves a red mark at its position, contracts, and then disappears. But in this case, there's an added offset.

1.  **Identify the Agent:** Find the gray (color code 5) object that forms a vertical line in the center of the input grid.

2.  **Locate Agent's Position:** Determine the row and column indices covered by that object.

3.  **Record center position:**. Note the cells covered by the object.

4.  **Change color and add offset:** Change the value of the gray positions to red (color code 2). But apply an offset of -2 to the column.

5. **Contract and disappear:** Eliminate all input cells except the ones forming the vertical grey object, with the applied offset. Fill the rest with white (color code 0).

6.  **Output:** A 3x3 output grid whose cells are white, except the cells corresponding to the previous position of the agent, which become red.
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Find the column indices of the gray objects (color code 5)
    # gray_cols = np.where(input_array[0] == 5)[0] # not needed

    # Determine the center column of the input
    center_col_input = cols // 2

    # Find positions
    # center_row = rows // 2 # Not needed
    # center_col = 1 # since we expect 3x3 output # not needed

    # Initialize the output grid with all white (0) and size 3x3
    output_grid = np.zeros((3, 3), dtype=int)

    # set center position as red
    # output_grid[center_row, center_col] = 2 # Not correct

    # Iterate and check
    for r in range(rows):
        if input_array[r,center_col_input] == 5:
            output_grid[r, r-rows+1] = 2  # r-2

    return output_grid.tolist()  # Convert back to a list for the assertion


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