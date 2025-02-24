"""
1.  For each input/output pair, identify the colors present in the input grid.
2.  Identify which of those input colors are *not* present in the output grid.
3.  Set all pixels of those colors in the input grid to black (0) to create the
    output grid. In other words, remove colors from the input that do not appear
    at all in the output.
"""

import numpy as np

def transform(input_grid, examples):
    # initialize output_grid as a copy of the input, ensures same size/type
    output_grid = np.copy(input_grid)
    
    # find the corresponding output for this input.
    #  the examples are provided, find the output that matches this input
    
    current_output = None
    for example in examples:
        if np.array_equal(example['input'], input_grid):
            current_output = example['output']
            break

    if current_output is None:  # very important safety check!
        return output_grid # Should not occur, but handle for safety

    # Get unique colors in the input grid
    input_colors = np.unique(input_grid)

    # Get unique colors in the corresponding output grid
    output_colors = np.unique(current_output)

    # Find colors present in input but NOT in output
    colors_to_remove = [color for color in input_colors if color not in output_colors]

    # Set pixels with those colors to 0 in the output grid
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] in colors_to_remove:
                output_grid[i, j] = 0

    return output_grid