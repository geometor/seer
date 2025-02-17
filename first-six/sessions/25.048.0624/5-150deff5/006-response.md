# 5-150deff5 • 006 • Response

---

*text:*

```python
"""
The input grid contains a single object of color 5 (gray) on a background of color 0 (white).
The transformation replaces the gray object with two colors: 8 (azure) and 2 (red).
The "top arm" of the gray object is replaced with color 8, while the rest of the gray object is replaced with color 2.
The background remains unchanged.
"""

import numpy as np

def find_object(grid, color):
    """Finds the coordinates of all cells with the given color."""
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = input_grid.copy()

    # Find the object with color 5 (gray).
    object_5_coords = find_object(input_grid, 5)

    # If no object with color 5 is found, return the original grid.
    if object_5_coords.size == 0:
        return output_grid

    # Find the "top arm" of the object.

    # Iterate the first row that contains the color 5.
    min_row = np.min(object_5_coords[:, 0])
    row_indices = np.where(object_5_coords[:, 0] == min_row)[0]
    row_coords = object_5_coords[row_indices]
    #Sort the coordinates
    row_coords_sorted = row_coords[row_coords[:,1].argsort()]

    top_arm_coords = []
    # Add to the azure coordinates, cells of the first row except those where there is no cell of color 5 below.
    for cell in row_coords_sorted:
        next_row_cell_down = [cell[0]+1, cell[1]]
        indices = np.where((object_5_coords == next_row_cell_down).all(axis=1))[0]
        if indices.size > 0:
            top_arm_coords.append(cell)

    # Add to the azure coordinates the cells of the second row that contains color 5, placed under cells selected in the previous step
    for cell in top_arm_coords:
        next_row_cell_down = [cell[0]+1, cell[1]]
        indices = np.where((object_5_coords == next_row_cell_down).all(axis=1))[0]
        if indices.size > 0:
            top_arm_coords.append(object_5_coords[indices[0]])
    top_arm_coords = np.array(top_arm_coords)

    # change color of the top arm
    for coord in top_arm_coords:
        output_grid[coord[0], coord[1]] = 8

    # Replace the remaining cells of object 5 with color 2.
    for coord in object_5_coords:
        if output_grid[coord[0], coord[1]] == 5:
            output_grid[coord[0], coord[1]] = 2

    return output_grid
```

