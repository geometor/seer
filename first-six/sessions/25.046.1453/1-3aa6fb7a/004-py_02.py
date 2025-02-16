"""
The transformation rule is as follows:

1.  Identify all azure (color 8) objects in the input grid.
2.  For each azure object, locate the top-most pixel.
3.  Change the color of the pixel immediately to the right of this top-most pixel to blue (color 1).
4. All other pixels keep their color.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = input_np.copy()
    rows, cols = input_np.shape

    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                # Check if this is the top-most pixel of an azure object
                is_topmost = True
                if r > 0 and input_np[r-1, c] == 8:
                    is_topmost = False

                if is_topmost:
                    #Change the pixel to the right to blue, if exists
                    if c + 1 < cols:
                        output_np[r,c+1] = 1
    return output_np.tolist()


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