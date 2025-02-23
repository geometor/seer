"""
The transformation identifies the topmost pixel of each azure (8) object and paints the pixel to its right blue (1).
"""

import numpy as np

def transform(input_grid):
    # Initialize output as a copy of the input
    output_grid = np.copy(input_grid)
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Iterate to find azure objects
    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 8:
                # Check if it's the topmost pixel of the object
                if r == 0 or input_grid[r-1][c] != 8:
                    # Paint the pixel to the right blue (1)
                    if c + 1 < cols:
                      output_grid[r][c+1] = 1

    return output_grid

if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input)

    if np.array_equal(output, expected_output):
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert np.array_equal(output, expected_output), "Transformed output does not match expected output."