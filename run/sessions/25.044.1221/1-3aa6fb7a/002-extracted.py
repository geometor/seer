"""
1.  **Identify '8' formations:** Locate all connected formations of the digit '8'.
2. **Locate start and end:** Locate the beginning and end of each formation, determined by row.
3.  **Change to '1':** Change the digit '8' at the start and end of the '8' formation, to '1'.
4. **Preserve other cells:** All the other cells remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Create a copy of the input grid to modify
    output_grid = [row[:] for row in input_grid]
    input_array = np.array(input_grid)

    # Iterate through each cell in the grid
    for r in range(len(input_grid)):
        for c in range(len(input_grid[0])):
            # Find '8's
            if input_array[r,c] == 8:
                #Check above
                if r > 0 and input_array[r-1, c] != 8:
                      output_grid[r][c] = 1
                #check below
                if r < len(input_array)-1 and input_array[r+1,c] !=8:
                    output_grid[r][c] = 1

    return output_grid


if __name__ == '__main__':
    input_grid = [
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

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    assert output == expected_output, "Transformed output does not match expected output."
