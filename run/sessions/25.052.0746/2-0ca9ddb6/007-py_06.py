import numpy as np

def create_plus_shape(grid, center, color):
    """Creates a plus shape around a center cell with a specified color,
    without overwriting the center cell itself."""
    rows, cols = grid.shape
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in offsets:
        r, c = center[0] + dr, center[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            grid[r, c] = color  # Directly set the color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)  # Work on a copy
    rows, cols = input_grid.shape

    # Iterate through all cell positions
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:  # Red cell
                create_plus_shape(output_grid, (r, c), 4) #yellow
            elif input_grid[r, c] == 1:  # Blue cell
                create_plus_shape(output_grid, (r, c), 7) #orange

    return output_grid