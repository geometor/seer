"""
The transformation is a simple color substitution rule, where the input colors 3, 1, and 2 are mapped to the output colors 4, 5, and 6, respectively, while the grid structure remains the same.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 1] = 5
    output_grid[input_grid == 2] = 6
    
    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [3, 1, 2],
        [3, 1, 2],
        [3, 1, 2]
    ]

    expected_output_grid = [
        [4, 5, 6],
        [4, 5, 6],
        [4, 5, 6]
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