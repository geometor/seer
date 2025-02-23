import numpy as np

COLOR_MAP = {
    0: (238, 238, 238),  # white
    1: (30, 147, 255),  # blue
    2: (220, 50, 40),  # red
    3: (79, 204, 48),  # green
    4: (230, 200, 0),  # yellow
    5: (85, 85, 85),  # gray
    6: (229, 58, 163),  # magenta
    7: (230, 120, 20),  # orange
    8: (135, 216, 241),  # azure
    9: (146, 18, 49),  # maroon
}

def transform(input_grid):
    """
    Transforms a 3x3 grid by incrementing each integer by 1.
    """
    # Initialize the output grid with the same dimensions as the input.
    output_grid = np.copy(input_grid)

    # Iterate through each cell in the input grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Increment the integer in the output by 1.
            output_grid[i, j] = (output_grid[i,j] + 1)

    return output_grid

# Example Data (Reproducing the provided examples)
examples = [
    (np.array([[3, 1, 2], [3, 1, 2], [3, 1, 2]]), np.array([[4, 5, 6], [4, 5, 6], [4, 5, 6]])),
    (np.array([[2, 3, 8], [2, 3, 8], [2, 3, 8]]), np.array([[6, 4, 9], [6, 4, 9], [6, 4, 9]])),
    (np.array([[5, 8, 6], [5, 8, 6], [5, 8, 6]]), np.array([[1, 9, 2], [1, 9, 2], [1, 9, 2]])),
    (np.array([[9, 4, 2], [9, 4, 2], [9, 4, 2]]), np.array([[8, 3, 6], [8, 3, 6], [8, 3, 6]])),
]

# Test the transform function and compare with expected outputs
for i, (input_grid, expected_output) in enumerate(examples):
    transformed_output = transform(input_grid)
    match = np.array_equal(transformed_output, expected_output)
    pixels_off = np.sum(transformed_output != expected_output)
    print(f"Example {i+1}:")
    print(f"Input:\n{input_grid}")
    print(f"Expected Output:\n{expected_output}")
    print(f"Transformed Output:\n{transformed_output}")
    print(f"Match: {match}")
    print(f"Pixels Off: {pixels_off}")
    print("---")
    
def calculate_mapping(examples):
    """Calculates and prints the mapping of input values to output values."""
    mapping = {}
    for input_grid, output_grid in examples:
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                input_val = input_grid[i, j]
                output_val = output_grid[i, j]
                mapping[input_val] = output_val
    return mapping

mapping = calculate_mapping(examples)
print(mapping)

