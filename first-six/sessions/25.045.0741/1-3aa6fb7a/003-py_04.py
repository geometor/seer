"""
The transformation process begins by identifying all connected components of color '8' (azure) in the input grid. These components are then ordered. The ordering criterion is based on the top-leftmost cell of each component: components are primarily sorted by the row index of their top-leftmost cell, and secondarily by the column index in case of ties in row indices.

After ordering, the algorithm iterates through the first three connected components in this determined order. For each of these components, starting with its top-leftmost cell, it attempts to modify a neighboring cell. The algorithm first checks the cell immediately to the right. If this cell is within the grid boundaries and its color in the input grid is '0' (white), then the color of this cell is changed to '1' (blue) in the output grid, and the process is stopped for the current component, moving on to the next component (if any, up to the first three).

If the cell to the right is not modified (either because it's out of bounds, or its color is not '0'), the algorithm then checks the cell immediately below the top-leftmost cell. If this cell is within the grid boundaries and its color in the input grid is '0', then the color of this cell is changed to '1' in the output grid, and again, the process stops for the current component.

If neither the cell to the right nor the cell below meet the conditions for color change for a component, no modification is made for that specific component.

This entire process is only applied to the first three connected components of color '8' in the determined order. For the fourth and any subsequent connected components, no transformations are performed. The resulting grid after these operations is the output grid.
"""

import numpy as np
from scipy.ndimage import label

def transform(input_grid):
    input_grid_np = np.array(input_grid)
    output_grid_np = np.copy(input_grid_np)

    labeled_grid, num_components = label(input_grid_np == 8)
    components = []
    for component_index in range(1, num_components + 1):
        component_coords = np.argwhere(labeled_grid == component_index)
        min_row = np.min(component_coords[:, 0])
        topmost_cells = component_coords[component_coords[:, 0] == min_row]
        top_leftmost_cell_coord = topmost_cells[np.argmin(topmost_cells[:, 1])]
        components.append(top_leftmost_cell_coord)

    # Order components by top-leftmost cell (row then col)
    ordered_components_indices = sorted(range(len(components)), key=lambda i: (components[i][0], components[i][1]))

    for i in range(min(3, num_components)): # Process only first 3 components
        component_index = ordered_components_indices[i]
        top_leftmost_cell_coord = components[component_index]
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
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
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