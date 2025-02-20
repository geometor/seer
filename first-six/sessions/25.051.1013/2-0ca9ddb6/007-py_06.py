import numpy as np

def find_objects(grid, color):
    """Finds the positions of all single-cell objects of the specified color."""
    coords = np.argwhere(grid == color)
    # Convert to list of tuples
    return [tuple(coord) for coord in coords]

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""
    output_grid = np.copy(input_grid)

    # Find all red and blue cells
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)

    # Red cell actions: add yellow cells for each red cell
    for red_pos in red_positions:
        if red_pos[0] - 1 >= 0 and red_pos[1] - 1 >= 0:
            output_grid[red_pos[0] - 1, red_pos[1] - 1] = 4  # Up-Left
        if red_pos[0] - 1 >= 0 and red_pos[1] + 1 < output_grid.shape[1]:
            output_grid[red_pos[0] - 1, red_pos[1] + 1] = 4  # Up-Right

    # Blue cell actions: add orange cells in L-shape
    for blue_pos in blue_positions:
        if blue_pos[1] - 1 >= 0:
            output_grid[blue_pos[0], blue_pos[1] - 1] = 7  # Left
        if blue_pos[0] + 1 < output_grid.shape[0] and blue_pos[1] - 1 >= 0:
            output_grid[blue_pos[0] + 1, blue_pos[1] - 1] = 7  # Down-Left
        if blue_pos[0] + 1 < output_grid.shape[0]:
            output_grid[blue_pos[0] + 1, blue_pos[1]] = 7 # Down

    return output_grid