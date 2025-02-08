import copy


def transform(grid):
    """
    Transformation Rule:

    1. Traverse the grid and examine every contiguous 2x2 sub-grid.
    2. For each sub-grid, if exactly three cells have the same non-white color (i.e., a color in 1-9)
       and the remaining cell is white (0), then fill that white cell with blue (color 1).
    3. Leave all other cells unchanged.

    This process effectively completes an almost-complete 2x2 square (an L-shape) by inserting a blue cell.

    Parameters:
        grid (list of list of int): The input grid, where each integer represents a color.

    Returns:
        list of list of int: The output grid after applying the transformation.
    """
    # Get grid dimensions
    if not grid or not grid[0]:
        return grid  # Return as is if grid is empty

    rows = len(grid)
    cols = len(grid[0])

    # Create a deep copy of the grid to avoid modifying the input directly.
    new_grid = copy.deepcopy(grid)

    # Helper function: check a 2x2 block starting at (r, c)
    def process_block(r, c):
        # Coordinates of the 2x2 block cells
        coords = [(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)]
        # Get the values in the block
        values = [grid[i][j] for i, j in coords]

        # Count how many are white (0) and group non-white values.
        white_indices = [idx for idx, val in enumerate(values) if val == 0]
        nonwhite_values = [val for val in values if val != 0]

        # Only consider block if exactly one cell is white and three cells are non-white.
        if len(white_indices) == 1 and len(nonwhite_values) == 3:
            # Check if all three non-white values are identical.
            if nonwhite_values.count(nonwhite_values[0]) == 3:
                # Complete the 2x2 square: set the white cell to blue (color 1)
                missing_idx = white_indices[0]
                missing_cell = coords[missing_idx]
                new_grid[missing_cell[0]][missing_cell[1]] = 1  # blue

    # Iterate over every possible 2x2 sub-grid in the grid
    for r in range(rows - 1):
        for c in range(cols - 1):
            process_block(r, c)

    return new_grid


# Example usage (using the provided example):
if __name__ == "__main__":
    input_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    output_grid = transform(input_grid)
    print("Output Grid:")
    for row in output_grid:
        print(row)

    # Optionally, check against the expected output.
    assert (
        output_grid == expected_output
    ), "The output grid does not match the expected result."
