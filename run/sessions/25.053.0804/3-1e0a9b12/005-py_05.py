import numpy as np

input_grid = np.array([
    [0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0],
    [0, 3, 0, 1, 2],
    [6, 0, 0, 0, 0],
    [0, 3, 0, 0, 0]
])

output_grid = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 3, 0, 1, 0],
    [6, 3, 0, 1, 2]
])

print("Input Grid:\n", input_grid)
print("\nOutput Grid:\n", output_grid)

# Find non zero pixels and their positions

def find_non_zero_pixels(grid):
    non_zero_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value != 0:
                non_zero_pixels.append((value, (row_index, col_index)))
    return non_zero_pixels

input_non_zero = find_non_zero_pixels(input_grid)
output_non_zero = find_non_zero_pixels(output_grid)

print("\nInput Non-zero Pixels:", input_non_zero)
print("Output Non-zero Pixels:", output_non_zero)