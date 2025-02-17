"""
The task is to transform the input grid by examining each cell.
For every cell in the grid, we check its color.
If the cell's color is 0 (white), we then look at its immediate horizontal neighbors: the cell to its left and the cell to its right in the same row.
If either the left neighbor or the right neighbor has a color of 8 (azure), we change the color of the current cell to 1 (blue) in the output grid.
If neither the left nor the right neighbor has a color of 8, or if the original cell's color was not 0, we retain the original color of the cell in the output grid.
When considering neighbors, we must be mindful of grid boundaries. Cells on the left edge have no left neighbor, and cells on the right edge have no right neighbor. In these cases, we only check for the existing neighbor if applicable.
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