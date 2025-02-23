import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified color mapping rule.
    """
    output_grid = np.copy(input_grid)

    color_map = {
        3: 4,
        1: 5,
        2: 6,
        8: 9,
        5: 1,
        6: 2,
        9: 8,
        4: 3,
        0: 0
    }

    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            input_color = output_grid[i, j]
            output_grid[i, j] = color_map.get(input_color, input_color)  # Use get() to handle unknown colors. Default keep color.

    return output_grid