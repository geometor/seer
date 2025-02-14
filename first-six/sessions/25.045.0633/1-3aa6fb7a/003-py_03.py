import numpy as np
from scipy.ndimage import label

def transform(input):
    grid = np.array(input)
    output_grid = np.copy(grid)
    labeled_grid, num_labels = label(grid == 8)

    for label_id in range(1, num_labels + 1):
        component_indices = np.argwhere(labeled_grid == label_id)
        min_row = np.min(component_indices[:, 0])
        topmost_cells = component_indices[component_indices[:, 0] == min_row]
        topleft_cell_row, topleft_cell_col = topmost_cells[np.argmin(topmost_cells[:, 1])]

        # Try to change cell to the right
        cell_r_row, cell_r_col = topleft_cell_row, topleft_cell_col + 1
        if (0 <= cell_r_row < grid.shape[0] and 0 <= cell_r_col < grid.shape[1] and
            grid[cell_r_row, cell_r_col] == 0 and labeled_grid[cell_r_row, cell_r_col] != label_id):
            output_grid[cell_r_row, cell_r_col] = 1
            continue

        # Try to change cell below
        cell_b_row, cell_b_col = topleft_cell_row + 1, topleft_cell_col
        if (0 <= cell_b_row < grid.shape[0] and 0 <= cell_b_col < grid.shape[1] and
            grid[cell_b_row, cell_b_col] == 0 and labeled_grid[cell_b_row, cell_b_col] != label_id):
            output_grid[cell_b_row, cell_b_col] = 1
            continue

        # Try to change cell to the left
        cell_l_row, cell_l_col = topleft_cell_row, topleft_cell_col - 1
        if (0 <= cell_l_row < grid.shape[0] and 0 <= cell_l_col < grid.shape[1] and
            grid[cell_l_row, cell_l_col] == 0 and labeled_grid[cell_l_row, cell_l_col] != label_id):
            output_grid[cell_l_row, cell_l_col] = 1
            continue

        # Try to change cell above
        cell_a_row, cell_a_col = topleft_cell_row - 1, topleft_cell_col
        if (0 <= cell_a_row < grid.shape[0] and 0 <= cell_a_col < grid.shape[1] and
            grid[cell_a_row, cell_a_col] == 0 and labeled_grid[cell_a_row, cell_a_col] != label_id):
            output_grid[cell_a_row, cell_a_col] = 1
            continue

    return output_grid.tolist()