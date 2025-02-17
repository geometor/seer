"""
The transformation rule is a color substitution based on the following mapping:
- Red (2) becomes Magenta (6)
- Green (3) becomes Yellow (4)
- Azure (8) becomes Maroon (9)
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.array(input_grid)

    # Apply the modulo transformation
    output_grid = (output_grid + 4) % 10


    return output_grid.tolist() # Convert back to list of lists


if __name__ == '__main__':

    input_grid = [
        [2, 3, 8],
        [2, 3, 8],
        [2, 3, 8]
    ]

    expected_output_grid = [
        [6, 7, 2],
        [6, 7, 2],
        [6, 7, 2]
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