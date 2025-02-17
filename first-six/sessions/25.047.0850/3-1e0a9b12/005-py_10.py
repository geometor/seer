"""
The non-white cells in the input grid are moved vertically down, maintaining their original column.
The non-background objects of the same column stack at the bottom of the output, preserving the input vertical order.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # change output pixels
    for col in range(input_grid.shape[1]):
        non_zero_elements = input_grid[input_grid[:, col] != 0, col]
        if non_zero_elements.size > 0:
            for i, element in enumerate(reversed(non_zero_elements)):
               output_grid[-(i+1),col] = element

    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
      [0, 0, 0, 1, 0],
      [0, 3, 0, 0, 0],
      [0, 3, 0, 1, 2],
      [6, 0, 0, 0, 0],
      [0, 3, 0, 0, 0]
    ]

    expected_output_grid =  [
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 3, 0, 0, 0],
      [0, 3, 0, 1, 0],
      [6, 3, 0, 1, 2]
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