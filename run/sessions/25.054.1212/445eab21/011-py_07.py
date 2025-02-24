import numpy as np

# Example data (from the provided examples)
example1_input = np.array([
    [0, 7, 7, 7, 7, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 7, 0, 0, 0, 0, 0],
    [0, 7, 7, 7, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 8, 8, 8, 8, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 8, 8, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])
example1_expected = np.array([[8, 8], [8, 8]])

example2_input = np.array([
    [6, 6, 6, 6, 6, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 6, 0, 0, 0, 0, 0],
    [6, 6, 6, 6, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])
example2_expected = np.array([[7, 7], [7, 7]])

example3_input = np.array([
    [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 4, 4, 4, 4, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2]
])
example3_expected = np.array([[4, 4], [4, 4]])


def extract_2x2_square(grid, color):
    """
    Extracts the first 2x2 square of the specified color.
    Returns coordinates of the 2x2 square as a list of tuples.
    """
    coords = np.argwhere(grid == color)
    for r, c in coords:
        if (r + 1 < grid.shape[0] and c + 1 < grid.shape[1] and
            grid[r + 1, c] == color and
            grid[r, c + 1] == color and
            grid[r + 1, c + 1] == color):
            return [[r, c], [r + 1, c], [r, c + 1], [r + 1, c + 1]]
    return []

def check_2x2_squares(input_grid, expected_output):
    unique_colors = np.unique(input_grid)
    print(f"Unique colors: {unique_colors}")
    found_squares = {}
    for color in unique_colors:
        square_coords = extract_2x2_square(input_grid, color)
        found_squares[color] = bool(square_coords)
        if square_coords: # print coords if found
            print(f"Found 2x2 {color=} at {square_coords=}")
    print(f"Found 2x2 squares: {found_squares}")
    print(f"Expected: \n {expected_output}")

print("Example 1:")
check_2x2_squares(example1_input, example1_expected)
print("\nExample 2:")
check_2x2_squares(example2_input, example2_expected)
print("\nExample 3:")
check_2x2_squares(example3_input, example3_expected)