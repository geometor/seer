import numpy as np
from scipy.ndimage import label

def transform_grid(input_grid):
    grid = np.array(input_grid)
    output_grid = np.copy(grid)
    labeled_grid, num_labels = label(grid == 8)

    for label_id in range(1, num_labels + 1):
        component_indices = np.argwhere(labeled_grid == label_id)
        min_row = np.min(component_indices[:, 0])
        topmost_cells = component_indices[component_indices[:, 0] == min_row]
        topleft_cell_row, topleft_cell_col = topmost_cells[np.argmin(topmost_cells[:, 1])]

        # Try to change cell to the right
        cell_right_col = topleft_cell_col + 1
        if (0 <= topleft_cell_row < grid.shape[0] and
            0 <= cell_right_col < grid.shape[1]):
            if grid[topleft_cell_row, cell_right_col] == 0 and labeled_grid[topleft_cell_row, cell_right_col] != label_id:
                output_grid[topleft_cell_row, cell_right_col] = 1
                continue # If right cell is changed, move to next component

        # If right cell cannot be changed, try cell below
        cell_below_row = topleft_cell_row + 1
        if (0 <= cell_below_row < grid.shape[0] and
            0 <= topleft_cell_col < grid.shape[1]):
            if grid[cell_below_row, topleft_cell_col] == 0 and labeled_grid[cell_below_row, topleft_cell_col] != label_id:
                output_grid[cell_below_row, topleft_cell_col] = 1
                continue # If below cell is changed, move to next component

    return output_grid.tolist()

# Example usage with input from problem description
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
print("Output Grid:")
for row in output_grid:
    print(row)