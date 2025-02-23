# 25.045.0741 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
The transformation process operates on connected regions of color '8' (azure) within the input grid. For each distinct connected component of '8's, the algorithm identifies a specific cell within that component: the "top-leftmost" cell. This cell is defined as the cell with the smallest row index, and in case of ties, the smallest column index among those with the smallest row index within the component.

Once the top-leftmost cell of a component is located, the algorithm first checks the cell immediately to its right. If this cell is within the grid boundaries and its color in the input grid is '0' (white), then the color of this cell is changed to '1' (blue) in the output grid.

If the cell to the right is not modified (either because it's out of bounds, or its color is not '0'), the algorithm then checks the cell immediately below the top-leftmost cell. If this cell is within the grid boundaries and its color in the input grid is '0', then the color of this cell is changed to '1' in the output grid.

If neither the cell to the right nor the cell below meet the conditions for color change, then no modification is made for that specific connected component. This process is repeated for every connected component of color '8' in the input grid to produce the final output grid.
"""

import numpy as np
from scipy.ndimage import label

def transform(input_grid):
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


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
```
