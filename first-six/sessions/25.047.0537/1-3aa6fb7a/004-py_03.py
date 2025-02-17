"""
The transformation rule is as follows:

1.  Identify all azure (color 8) objects that are 2x1 vertical rectangles.
2.  For each such object, find the cell immediately to the right of its top cell.
3.  Change the color of that cell to blue (color 1).
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    output_np = np.copy(input_np)
    rows, cols = input_np.shape

    for r in range(rows - 1):
        for c in range(cols):
            if input_np[r, c] == 8 and input_np[r+1, c] == 8:
                # Check if it's a 2x1 vertical rectangle
                is_2x1 = True
                if c > 0 and input_np[r,c-1] == 8: #check left
                  is_2x1 = False
                if c < cols - 1 and input_np[r,c+1] == 8 and input_np[r+1,c+1] !=8:
                  is_2x1 = False # check if it is not just the beginning of a horizontal line.
                if r > 0 and input_np[r-1,c] == 8:
                  is_2x1 = False #check above
                
                if is_2x1:

                  if c + 1 < cols:
                      output_np[r, c + 1] = 1
    return output_np.tolist()  # Convert back to list


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