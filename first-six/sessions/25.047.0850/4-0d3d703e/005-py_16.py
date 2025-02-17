"""
The transformation rule is a conditional color substitution:
- Gray (5) becomes Blue (1)
- Azure (8) becomes Maroon (9)
- Magenta (6) becomes Red (2)
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input
    output_grid = np.array(input_grid, copy=True)
    rows, cols = output_grid.shape

    # Iterate and apply the conditional transformation
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 5:
                output_grid[i, j] = 1
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9
            elif output_grid[i, j] == 6:
                output_grid[i, j] = 2

    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [5, 8, 6],
        [5, 8, 6],
        [5, 8, 6]
    ]

    expected_output_grid = [
        [1, 9, 2],
        [1, 9, 2],
        [1, 9, 2]
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