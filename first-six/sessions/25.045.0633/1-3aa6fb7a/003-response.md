# 25.045.0633 • 1-3aa6fb7a • 003 Response

---

*text:*

**Natural Language Description of Transformation:**

For each connected region of color 8 in the input grid:
1. Identify the topmost-leftmost cell of the region. This is the cell with the minimum row index, and among cells with the same minimum row index, the minimum column index.
2. Attempt to change the color of the cell immediately to the **right** of this topmost-leftmost cell to color 1, but only if:
    a. The cell to the right is within the grid boundaries.
    b. The cell to the right is currently color 0 in the input grid.
    c. The cell to the right is not part of the same connected region of color 8.
3. If the change in step 2 is not possible (because condition a, b, or c is not met), then attempt to change the color of the cell immediately **below** the topmost-leftmost cell to color 1, but only if:
    a. The cell below is within the grid boundaries.
    b. The cell below is currently color 0 in the input grid.
    c. The cell below is not part of the same connected region of color 8.
4. If the change in step 3 is not possible, then attempt to change the color of the cell immediately to the **left** of the topmost-leftmost cell to color 1, but only if:
    a. The cell to the left is within the grid boundaries.
    b. The cell to the left is currently color 0 in the input grid.
    c. The cell to the left is not part of the same connected region of color 8.
5. If the change in step 4 is not possible, then attempt to change the color of the cell immediately **above** the topmost-leftmost cell to color 1, but only if:
    a. The cell above is within the grid boundaries.
    b. The cell above is currently color 0 in the input grid.
    c. The cell above is not part of the same connected region of color 8.
6. If none of the above changes are possible, no change is made for this region.

**Python Implementation:**

```python
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
```
