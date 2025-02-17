import numpy as np
from scipy.ndimage import label

def transform_grid(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid_np = np.copy(input_grid_np)

    labeled_grid, num_components = label(input_grid_np == 8)

    for component_index in range(1, num_components + 1):
        component_coords = np.argwhere(labeled_grid == component_index)
        min_row = np.min(component_coords[:, 0])
        topmost_cells = component_coords[component_coords[:, 0] == min_row]
        top_leftmost_cell_coord = topmost_cells[np.argmin(topmost_cells[:, 1])]
        row, col = top_leftmost_cell_coord

        # Check cell to the right
        right_col = col + 1
        if 0 <= right_col < input_grid_np.shape[1]:
            if input_grid_np[row, right_col] == 0:
                output_grid_np[row, right_col] = 1
                continue # If right is changed, do not check below

        # Check cell below
        below_row = row + 1
        if 0 <= below_row < input_grid_np.shape[0]:
            if input_grid_np[below_row, col] == 0:
                output_grid_np[below_row, col] = 1

    return output_grid_np.tolist()

# Example usage (with the input provided in the problem description)
input_grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

output_grid = transform_grid(input_grid)
print(output_grid)