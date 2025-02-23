"""
The transformation rule is as follows:

1.  Identify all objects of color 8 (azure).
2.  For each identified object, find the top-most pixel.
3.  Place a pixel of color 1 (blue) immediately to the right of this top-most pixel.
"""

import numpy as np

def transform(input):
    # Initialize output as a copy of the input
    output = np.copy(input)
    rows = len(input)
    cols = len(input[0])

    # Iterate through the input grid
    for r in range(rows):
        for c in range(cols):
            # Check for color 8
            if input[r][c] == 8:
                # Check if there is an element to the right
                if c+1 < cols:
                  #Check that there isn't already blue there
                  if output[r][c+1] != 1:
                    #find top most azure pixel
                    top_most = True
                    if r > 0:
                      if input[r-1][c] == 8:
                        top_most = False

                    if top_most:
                      output[r][c + 1] = 1

    return output


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

    if output.tolist() == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output.tolist())

    print()
    assert output.tolist() == expected_output, "Transformed output does not match expected output."