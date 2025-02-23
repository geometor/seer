import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on a color substitution rule, preserving structure.
    """
    output_grid = np.copy(input_grid)

    # Define the color mapping based on the observed transformations.
    color_map = {
        9: 8,  # Maroon -> Azure
        4: 3,  # Yellow -> Green
        2: 6,  # Red -> Magenta
    }

    # Iterate through each cell and apply the color mapping.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            original_color = output_grid[i, j]
            if original_color in color_map:
                output_grid[i, j] = color_map[original_color]

    return output_grid