"""
The transformation rule identifies azure (color 8) objects and paints a blue pixel (color 1)
to the right of the top cell of vertical objects and to the left of the bottom-right cell of square shaped objects.
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                # Check for 2x1 vertical object
                if r + 1 < rows and input_np[r+1, c] == 8 and (r == 0 or input_np[r-1,c] !=8) :
                    if c + 1 < cols:
                        output_np[r, c+1] = 1
                # Check for bottom right corner
                if r + 1 < rows and c+1 < cols and input_np[r+1,c+1] == 8 and input_np[r+1,c]==8 and input_np[r,c+1] ==8:
                   if c > 0:
                       output_np[r+1,c] = 1

    return output_np.tolist()

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