"""
The task is to modify the input grid based on the presence of color 8 (azure).
For each cell in the grid, we check if its value is 0 (white).
If it is 0, we then examine its immediate left and right neighbors in the same row.
If either the left neighbor or the right neighbor has a value of 8 (azure), we change the value of the current cell to 1 (blue) in the output grid.
If neither neighbor is 8, or if the original cell value is not 0, we keep the original cell value unchanged in the output grid.
When checking neighbors, we need to handle boundary cases. If a cell is on the left edge, it has no left neighbor; if it's on the right edge, it has no right neighbor. In these cases, we only consider the existing neighbor.
"""

import copy

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    output_grid = copy.deepcopy(input_grid)

    for r in range(rows):
        for c in range(cols):
            if input_grid[r][c] == 0:
                # Check left neighbor
                left_neighbor_is_8 = False
                if c > 0 and input_grid[r][c-1] == 8:
                    left_neighbor_is_8 = True

                # Check right neighbor
                right_neighbor_is_8 = False
                if c < cols - 1 and input_grid[r][c+1] == 8:
                    right_neighbor_is_8 = True

                if left_neighbor_is_8 or right_neighbor_is_8:
                    output_grid[r][c] = 1

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

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."