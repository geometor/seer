"""
Locate all instances of the digit '8' in the input grid.
Inspect each '8'. If an '8' is *not* on an edge (top, bottom, left, or right border), replace it with the digit '1'.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Replace '8' with '1' if it's not on the border.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    output_array = np.copy(input_array)

    for r in range(rows):
        for c in range(cols):
            if input_array[r, c] == 8:
                # Check if it's on the border
                if r > 0 and r < rows - 1 and c > 0 and c < cols - 1:
                    output_array[r, c] = 1

    return output_array.tolist()  # Convert back to list of lists


if __name__ == '__main__':
    input_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."