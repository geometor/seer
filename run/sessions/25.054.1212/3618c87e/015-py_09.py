import numpy as np

# Example 1
input_grid_1 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 5, 0, 0],
    [5, 5, 5, 5, 5]
])
output_grid_1 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0],
    [5, 5, 1, 5, 5]
])

# Example 2
input_grid_2 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 5, 0, 5, 0],
    [5, 5, 5, 5, 5]
])
output_grid_2 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 5, 0, 5, 0],
    [5, 1, 5, 1, 5]
])

# Example 3
input_grid_3 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 5, 0, 0, 5],
    [5, 5, 5, 5, 5]
])
output_grid_3 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 5, 0, 0, 5],
    [5, 1, 5, 5, 1]
])
def report_pixel_values(input_grid, output_grid):
    """Prints the pixel values for rows 2, 4 of input and row 5 of output."""
    print("Input Row 3 (index 2):", input_grid[2])
    print("Input Row 4 (index 3):", input_grid[3])
    print("Output Row 5 (index 4):", output_grid[4])
    print("-" * 20)

print("Example 1:")
report_pixel_values(input_grid_1, output_grid_1)
print("Example 2:")
report_pixel_values(input_grid_2, output_grid_2)
print("Example 3:")
report_pixel_values(input_grid_3, output_grid_3)