"""
The transformation rule is: Find the cell immediately to the right of the top-left corner cell of each azure object. Change the color of that cell to blue (color 1).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through the grid to find azure objects
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 8:
                # Check if it's the top-left corner of an azure object
                # Check for vertical 2x1 rectangle
                if i + 1 < rows and input_grid[i+1, j] == 8 and (j==0 or input_grid[i,j-1]!=8) and (i==0 or input_grid[i-1, j]!=8):
                    #change the right neighbor to blue
                     if j + 1 < cols:
                        output_grid[i, j + 1] = 1
                # Check for horizontal 1x2 rectangle
                if j + 1 < cols and input_grid[i, j+1] == 8 and (i==0 or input_grid[i-1,j]!=8) and (j==0 or input_grid[i,j-1]!=8) :
                    # change the right neighbor of top-left corner to blue
                    if j + 1 < cols:
                        output_grid[i, j + 1] = 1

    return output_grid.tolist()


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

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
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