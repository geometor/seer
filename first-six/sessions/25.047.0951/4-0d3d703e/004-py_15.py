"""
The transformation is a simple color substitution rule, where the input colors 2, 3, and 8 are mapped to the output colors 6, 4, and 9, respectively, while the grid structure remains the same.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    output_grid[input_grid == 2] = 6
    output_grid[input_grid == 3] = 4
    output_grid[input_grid == 8] = 9
    
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