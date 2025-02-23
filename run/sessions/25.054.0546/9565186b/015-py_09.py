import numpy as np

def calculate_error_pixels(expected_grid, output_grid):
    """Calculates the number of pixels that differ between two grids."""
    if expected_grid.shape != output_grid.shape:
        return -1 # Indicates an error due to shape mismatch
    diff = expected_grid != output_grid
    return np.sum(diff)

def transform(input_grid):
    output_grid = np.copy(input_grid)
    height = output_grid.shape[0]
    middle_row = height // 2
    for x in range(output_grid.shape[1]):
      if output_grid[middle_row, x] == 8:
          output_grid[middle_row, x] = 5
    return output_grid

# Example data (replace with actual data from the examples)
examples = [
    (np.array([[2, 2, 2], [2, 1, 8], [2, 8, 8]]), np.array([[2, 2, 2], [2, 5, 5], [2, 5, 5]])),
    (np.array([[1, 1, 1], [8, 1, 3], [8, 2, 2]]), np.array([[1, 1, 1], [5, 1, 5], [5, 5, 5]])),
    (np.array([[2, 2, 2], [8, 8, 2], [2, 2, 2]]), np.array([[2, 2, 2], [5, 5, 2], [2, 2, 2]])),
    (np.array([[3, 3, 8], [4, 4, 4], [8, 1, 1]]), np.array([[5, 5, 5], [4, 4, 4], [5, 5, 5]])),
]

for i, (input_grid, expected_output) in enumerate(examples):
    transformed_output = transform(input_grid)
    error_pixels = calculate_error_pixels(expected_output, transformed_output)
    print(f"Example {i+1}:")
    print(f"Input:\n{input_grid}")
    print(f"Expected Output:\n{expected_output}")
    print(f"Transformed Output:\n{transformed_output}")
    print(f"Error Pixels: {error_pixels}")
    print("-" * 20)
