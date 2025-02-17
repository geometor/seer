"""
The transformation rule is as follows:

1.  Identify all azure (color 8) objects.
2.  For each azure object, locate the top-most pixel.
3.  Place a blue (color 1) pixel immediately to the right of this top-most pixel.
4.  All the existing object positions are preserved.
"""

import numpy as np

def transform(input):
    # Initialize output as a copy of the input
    output = np.copy(input)
    rows = len(input)
    cols = len(input[0])

    # Iterate through the grid to find azure pixels
    for i in range(rows):
        for j in range(cols):
            if input[i][j] == 8:
                # Check if this is the top-most azure pixel of a contiguous object
                if i == 0 or input[i-1][j] != 8:
                    # Place a blue pixel to the right
                    if j + 1 < cols:
                        output[i][j+1] = 1

    return output.tolist()  #convert back to list from numpy array

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

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."