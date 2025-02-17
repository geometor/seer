"""
Iterate through each cell in the input grid.
If a cell is azure (color 8):
  Check the cell to the immediate right. If it's white (0), change it to blue (1).
  Check the cell to the immediate left. If it's white (0), change it to blue (1).
"""

import numpy as np

def transform(input_grid):
    input_np = np.array(input_grid)
    rows, cols = input_np.shape
    output_np = input_np.copy()

    for r in range(rows):
        for c in range(cols):
            if input_np[r, c] == 8:
                # Check right neighbor
                if c + 1 < cols and input_np[r, c + 1] == 0:
                    output_np[r, c + 1] = 1
                # Check left neighbor
                if c - 1 >= 0 and input_np[r, c - 1] == 0:
                    output_np[r, c - 1] = 1
    return output_np.tolist()  # Convert back to list for comparison


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