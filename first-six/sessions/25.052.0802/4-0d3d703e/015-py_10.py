"""
The transformation rule is a color substitution based on a mapping
derived from example input-output pairs. The spatial structure is preserved.
If an input color is encountered that wasn't seen in the examples,
the original color is kept.
"""

import numpy as np

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

# Example Usage (and how it would be tested)
example_inputs = [np.array([[9, 4, 2], [9, 4, 2], [9, 4, 2]])]
example_outputs = [np.array([[8, 3, 6], [8, 3, 6], [8, 3, 6]])]

# Build the color map from the examples.
color_map = build_color_map(example_inputs, example_outputs)

# Example input to transform.
input_grid = np.array([[9, 4, 2], [9, 4, 2], [9, 4, 2]])

# Now, transform the input grid using the color map.
output_grid = transform(input_grid, color_map)

# Print the output (for verification).
print(output_grid)

#Test another input
input_grid2 = np.array([[9, 4, 2], [1, 4, 9], [9, 0, 2]]) #Introduce colors 0, 1
output_grid2 = transform(input_grid2, color_map)
print(output_grid2)