"""
The transformation rule is as follows:

1.  Identify all azure (color 8) objects.
2.  For each azure object, locate the top-most pixel.
3.  Place a blue (color 1) pixel immediately to the right of this top-most pixel.
4.  All the existing object positions are preserved.
"""

import numpy as np

def transform(input_grid):
    input_array = np.array(input_grid)
    output_array = np.copy(input_array)
    rows, cols = input_array.shape

    for r in range(rows):
        for c in range(cols):
            if input_array[r, c] == 8:
                # Check if this is the topmost pixel of the object
                is_topmost = True
                if r > 0 and input_array[r-1, c] == 8:
                    is_topmost = False

                if is_topmost:
                    if c + 1 < cols:  # Ensure we don't go out of bounds
                        output_array[r, c+1] = 1

    return output_array.tolist()


if __name__ == '__main__':

    input = [
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

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."