"""
Crops and overlays colored regions from the input grid onto an output grid,
maintaining relative positions and scaling to the output size.
"""

import numpy as np

def get_output_size(example_outputs):
    """Determines the output grid size from the example outputs."""
    first_output = example_outputs[0]
    return (len(first_output), len(first_output[0]))

def find_colored_pixels(grid):
    """Finds all pixels with non-zero color."""
    colored_pixels = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != 0:
                colored_pixels.append((i, j, grid[i, j]))
    return colored_pixels

def transform(input_grid, output_grid_shape):
    # initialize output_grid
    output_grid = np.zeros(output_grid_shape, dtype=int)

    # find all colored pixels
    colored_pixels = find_colored_pixels(input_grid)

    # Scale and map colored pixels
    input_rows, input_cols = input_grid.shape
    output_rows, output_cols = output_grid.shape

    for r, c, color in colored_pixels:
        out_r = int(r * output_rows / input_rows)
        out_c = int(c * output_cols / input_cols)
        output_grid[out_r, out_c] = color

    return output_grid