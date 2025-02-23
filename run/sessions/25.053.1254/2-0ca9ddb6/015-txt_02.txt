import numpy as np

def analyze_changes(input_grid, output_grid, expected_grid):
    """Analyzes the differences between the output and expected grids."""
    incorrect_changes = []
    rows, cols = input_grid.shape

    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] != expected_grid[i, j]:
                incorrect_changes.append(
                    (i, j, input_grid[i,j], output_grid[i, j], expected_grid[i, j])
                )
    return incorrect_changes

#Example Usage with the provided examples.
input_grid_1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]])
expected_grid_1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 7, 0, 0],
[0, 0, 0, 0, 0, 7, 1, 7, 0],
[0, 0, 0, 0, 0, 0, 7, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]])
output_grid_1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[4, 0, 2, 0, 4, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 4, 0, 0],
[0, 0, 4, 0, 0, 4, 0, 4, 0],
[0, 0, 0, 0, 4, 0, 1, 0, 4],
[0, 0, 0, 0, 0, 4, 0, 4, 0],
[0, 0, 0, 0, 0, 0, 4, 0, 0]])

input_grid_2 = np.array([[0, 0, 0, 8, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]])
expected_grid_2 = np.array([[0, 0, 0, 8, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 4, 0, 4, 0],
[0, 0, 7, 0, 0, 0, 2, 0, 0],
[0, 7, 1, 7, 0, 4, 0, 4, 0],
[0, 0, 7, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 7, 0, 0],
[4, 0, 4, 0, 0, 7, 1, 7, 0],
[0, 2, 0, 0, 0, 0, 7, 0, 0],
[4, 0, 4, 0, 0, 0, 0, 0, 0]])
output_grid_2 = np.array([[0, 0, 7, 8, 7, 0, 4, 0, 0],
[0, 0, 4, 7, 0, 4, 0, 4, 0],
[0, 4, 0, 4, 4, 0, 2, 0, 4],
[4, 0, 1, 0, 4, 4, 0, 4, 0],
[0, 4, 0, 4, 0, 0, 4, 0, 0],
[0, 4, 4, 0, 0, 4, 0, 4, 0],
[4, 0, 4, 0, 4, 0, 1, 0, 4],
[0, 2, 0, 4, 0, 4, 0, 4, 0],
[4, 0, 4, 0, 0, 0, 4, 0, 0]])

input_grid_3 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 6, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]])
expected_grid_3 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 6, 0, 0],
[0, 0, 0, 7, 0, 0, 0, 0, 0],
[0, 0, 7, 1, 7, 0, 0, 0, 0],
[0, 0, 0, 7, 0, 0, 0, 0, 0]])
output_grid_3 = np.array([[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[4, 0, 2, 0, 4, 0, 0, 0, 0],
[0, 4, 0, 4, 0, 0, 0, 0, 0],
[0, 0, 4, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 4, 0, 0, 6, 0, 0],
[0, 0, 4, 0, 4, 0, 0, 0, 0],
[0, 4, 0, 1, 0, 4, 0, 0, 0],
[0, 0, 4, 0, 4, 0, 0, 0, 0]])
incorrect_changes_1 = analyze_changes(input_grid_1, output_grid_1, expected_grid_1)
incorrect_changes_2 = analyze_changes(input_grid_2, output_grid_2, expected_grid_2)
incorrect_changes_3 = analyze_changes(input_grid_3, output_grid_3, expected_grid_3)

print("Incorrect Changes Example 1:", incorrect_changes_1)
print("Incorrect Changes Example 2:", incorrect_changes_2)
print("Incorrect Changes Example 3:", incorrect_changes_3)