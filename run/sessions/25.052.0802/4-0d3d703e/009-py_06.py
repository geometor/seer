import numpy as np

# Previous examples (assuming these are defined elsewhere)
example_1_input = np.array([[3, 1, 2], [3, 1, 2], [3, 1, 2]])
example_1_output = np.array([[4, 5, 6], [4, 5, 6], [4, 5, 6]])

example_2_input = np.array([[2, 3, 8], [2, 3, 8], [2, 3, 8]])
example_2_output = np.array([[6, 4, 9], [6, 4, 9], [6, 4, 9]])

# New example
example_3_input = np.array([[5, 8, 6], [5, 8, 6], [5, 8, 6]])
example_3_output = np.array([[1, 9, 2], [1, 9, 2], [1, 9, 2]])

# Build the color map using *all* examples
example_inputs = [example_1_input, example_2_input, example_3_input]
example_outputs = [example_1_output, example_2_output, example_3_output]
color_map = build_color_map(example_inputs, example_outputs)

# Test with a new input (same as example 3)
new_input = np.array([[5, 8, 6], [5, 8, 6], [5, 8, 6]])
output_grid = transform(new_input, color_map)
print(output_grid)  # Expected: [[1 9 2] [1 9 2] [1 9 2]]

# Demonstrating the 'unknown color' handling (using '7' which isn't in the map)
new_input_unknown = np.array([[5, 7, 6], [5, 7, 6], [5, 7, 6]])
output_grid_unknown = transform(new_input_unknown, color_map)
print(output_grid_unknown)  # Expected: [[1 7 2] [1 7 2] [1 7 2]] - 7 remains unchanged.

def build_color_map(example_inputs, example_outputs):
    """Builds a color mapping dictionary from example input/output pairs."""
    color_map = {}
    for input_grid, output_grid in zip(example_inputs, example_outputs):
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                input_color = input_grid[i, j]
                output_color = output_grid[i, j]
                color_map[input_color] = output_color
    return color_map

def transform(input_grid, color_map):
    """
    Transforms the input grid into the output grid by applying a color substitution
    based on the provided color_map.

    Args:
        input_grid (numpy.ndarray): The input grid.
        color_map (dict):  A dictionary mapping input colors to output colors

    Returns:
        numpy.ndarray: The transformed output grid.
    """
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.zeros_like(input_grid)

    # Iterate through each cell in the input grid.
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Get the color of the current cell.
            input_color = input_grid[i, j]

            # Apply the color substitution if mapping is known.
            output_color = color_map.get(input_color, input_color) # Default: Keep original

            # Place the new color in the corresponding cell of the output grid.
            output_grid[i, j] = output_color

    return output_grid
