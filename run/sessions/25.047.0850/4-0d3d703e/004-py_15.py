"""
The transformation rule is a conditional color substitution:
- Red (2) becomes Magenta (6)
- Green (3) becomes Yellow (4)
- Azure (8) becomes Maroon (9)
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input
    output_grid = np.array(input_grid, copy=True)  # Create a deep copy
    rows, cols = output_grid.shape

    # Iterate through each cell and apply the conditional transformation
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 2:
                output_grid[i, j] = 6
            elif output_grid[i, j] == 3:
                output_grid[i, j] = 4
            elif output_grid[i, j] == 8:
                output_grid[i, j] = 9

    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [2, 3, 8],
        [2, 3, 8],
        [2, 3, 8]
    ]

    expected_output_grid = [
        [6, 4, 9],
        [6, 4, 9],
        [6, 4, 9]
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