"""
The transformation rule identifies two specific blue (8) cells in the input grid:
the cell at row 2, column 3, and the cell at row 5, column 6.
These cells are changed to orange (1). All other cells remain unchanged.
"""

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Change the color of the blue object at row 2, column 3 to orange (1).
    Change the color of the blue object at row 5, column 6 to orange (1).
    """
    # Create a copy of the input grid to avoid modifying the original.
    output_grid = [row[:] for row in input_grid]

    # Change the color at the specified positions (adjusting for 0-indexing).
    output_grid[1][2] = 1  # Row 2, Column 3 (0-indexed: row 1, column 2)
    output_grid[4][5] = 1  # Row 5, Column 6 (0-indexed: row 4, column 5)

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

    transformed_output_grid = transform(input_grid)

    if transformed_output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", transformed_output_grid)

    print()
    assert transformed_output_grid == expected_output_grid, "Transformed output does not match expected output."