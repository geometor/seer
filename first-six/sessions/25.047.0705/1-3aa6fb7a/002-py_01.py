"""
The transformation identifies cells that have specific relations to the L-shape objects and changes the color of cells in the described location. The other elements of the grid remain the same.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the positions of the L-shaped objects
    l_shape_positions = []
    for r in range(len(input_grid)):
        for c in range(len(input_grid[0])):
            if input_grid[r][c] == 8:
                l_shape_positions.append((r, c))

    # Extract coordinates for the first L-shape.
    first_l_shape = sorted(l_shape_positions[:3])
    #print(first_l_shape)
    # Get the top cell of the first L-shape.
    top_cell_first_l = first_l_shape[0]


    # Change the cell to the right of the top cell to color 1.
    output_grid[top_cell_first_l[0]][top_cell_first_l[1] + 1] = 1

     # Extract coordinates for the second L-shape.

    second_l_shape = sorted(l_shape_positions[3:])
    #print(second_l_shape)

    # Get the bottom cell of the second L-shape.

    bottom_cell_second_l = second_l_shape[-1]

    # Change the cell to the left of the bottom cell to color 1
    output_grid[bottom_cell_second_l[0]][bottom_cell_second_l[1] - 1] = 1


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

    if output_grid.tolist() == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid.tolist())

    print()
    assert output_grid.tolist() == expected_output_grid, "Transformed output does not match expected output."