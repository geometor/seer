"""
The transformation rule is a simple color substitution: each color value is incremented by one.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.array(input_grid)

    # Apply the transformation: increment each color value
    output_grid = output_grid + 1

    return output_grid.tolist() # Convert back to list of lists


if __name__ == '__main__':

    input_grid = [
        [3, 1, 2],
        [3, 1, 2],
        [3, 1, 2]
    ]

    expected_output_grid = [
        [4, 2, 3],
        [4, 2, 3],
        [4, 2, 3]
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