import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the column index of the gray line (color code 5)
    gray_col = -1
    for j in range(cols):
        if np.all(input_grid[:, j] == 5):
            gray_col = j
            break

    if gray_col == -1:  # No gray line found, return all zeros
        return output_grid

    # Count blue cells (color code 1) to the left and right of the gray line for each row
    for r in range(rows):
        left_blue_count = 0
        right_blue_count = 0

        for c in range(cols):
            if input_grid[r, c] == 1:
                if c < gray_col:
                    left_blue_count += 1
                elif c > gray_col:
                    right_blue_count += 1
        
        if left_blue_count > right_blue_count:
            output_grid[0,r]=2
        elif right_blue_count > left_blue_count:
             output_grid[1,r] = 2
        elif right_blue_count == left_blue_count:
             output_grid[2,r] = 2



    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
     [1, 1, 0, 5, 0, 1, 0],
     [0, 0, 1, 5, 1, 1, 1],
     [1, 1, 0, 5, 0, 1, 0]
    ]

    expected_output_grid = [
    [0, 2, 0],
    [0, 0, 2],
    [0, 2, 0]
    ]

    output_grid = transform(input_grid)

    if output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid)

    print()
    assert output_grid == expected_output_grid, "Transformed output does not match expected output."