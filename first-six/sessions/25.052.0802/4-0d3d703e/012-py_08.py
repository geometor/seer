"""
The transformation rule involves creating a color map from the example input-output pairs
and then applying this map to the test input grid. If a color in the test input
is not in the map, it remains unchanged.
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

def transform(input_grid, example_inputs, example_outputs):
    """
    Transforms the input grid into the output grid by applying a color substitution
    based on the provided example input/output grids.

    Args:
        input_grid (numpy.ndarray): The input grid.
        example_inputs (list): List of example input grids.
        example_outputs (list): List of example output grids.

    Returns:
        numpy.ndarray: The transformed output grid.
    """

    # Build the color map
    color_map = build_color_map(example_inputs, example_outputs)

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