import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a "gravity" effect to colored objects.
    Objects fall down until they hit the bottom or another object.
    """
    output_grid = np.zeros_like(input_grid)
    height, width = input_grid.shape

    # Iterate through each column
    for x in range(width):
        # Keep track of the next available row in this column (from the bottom)
        next_available_row = height - 1

        # Iterate through the input column from bottom to top
        for y in range(height - 1, -1, -1):
            color = input_grid[y, x]
            if color != 0:  # If it's a colored cell (an object)
                output_grid[next_available_row, x] = color
                next_available_row -= 1  # Move the available row up

    return output_grid