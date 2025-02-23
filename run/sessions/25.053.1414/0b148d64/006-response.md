# 0b148d64 • 006 • refine_coder

---
```python
"""
1.  **Identify All Objects:** Find all contiguous objects in the input grid. An object is a group of connected pixels of the same color.

2.  **Bottom-Left Object Selection:** Sort the objects based on the bottom-most and then left-most pixel coordinate, selecting the first one, using the object coordinate list.

3.  **Color Change Detection (if applicable):** If example output is given,
    then compare the color of the selected object in the input grid to its color in the output grid.

4.  **Cropping (if applicable):**
    Crop the input grid around the selected object, using the min and max row and col of the objects coordinates.

5.  **Color Filtering (if applicable):** If a color change was detected, create a copy of the cropped input grid and replace all pixels that do not match the *output* color with 0 (white). If no color change occurred, keep the original object colors, but apply to cropped area.

6.  **Output:** Return the (potentially cropped and color-filtered) grid.
"""

import numpy as np

def find_all_objects(grid):
    """Find all contiguous objects in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object_coords):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col]):
            return 0

        visited[row, col] = True
        current_object_coords.append((row,col))
        size = 1

        size += dfs(row + 1, col, current_object_coords)
        size += dfs(row - 1, col, current_object_coords)
        size += dfs(row, col + 1, current_object_coords)
        size += dfs(row, col - 1, current_object_coords)
        return size

    for row_start in range(grid.shape[0]):
        for col_start in range(grid.shape[1]):
             if not visited[row_start, col_start]:
                current_object = []
                dfs(row_start, col_start, current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def get_object_color(grid, object_coords):
    """Get the color of an object (assumes all pixels in coords have the same color)."""
    return grid[object_coords[0]]

def crop_grid(grid, coords):
    """Crops the grid to the bounding box defined by the coordinates."""
    min_row = min(r for r, _ in coords)
    max_row = max(r for r, _ in coords)
    min_col = min(c for _, c in coords)
    max_col = max(c for _, c in coords)

    return grid[min_row:max_row + 1, min_col:max_col + 1]

def transform(input_grid, output_grid_expected=None):
    # Find all objects
    all_objects = find_all_objects(input_grid)

    # Select bottom-left object
    if not all_objects:
        return input_grid.copy()

    bottom_left_objects = sorted(all_objects, key=lambda obj: (-max(r for r, _ in obj), min(c for _, c in obj)) )
    target_object_coords = bottom_left_objects[0]

    # Crop the grid
    cropped_input = crop_grid(input_grid, target_object_coords)

    if output_grid_expected is not None:
        # Get color of the object in input and expected output
        input_color = get_object_color(input_grid, target_object_coords)

        #find object in output_grid_expected, adjust the coordinates for crop
        cropped_expected = crop_grid(output_grid_expected, target_object_coords)
        transformed_object = [(r - min(r for r, _ in target_object_coords), c - min(c for _, c in target_object_coords)) for r, c in target_object_coords if (r - min(r for r, _ in target_object_coords)) < cropped_expected.shape[0] and (c - min(c for _, c in target_object_coords)) < cropped_expected.shape[1] ]

        if transformed_object:
            output_color = get_object_color(cropped_expected, transformed_object)

            # Filter colors based on output color
            output_grid = cropped_input.copy()

            #if the color changes apply color filter
            if input_color != output_color:
              for row in range(output_grid.shape[0]):
                  for col in range(output_grid.shape[1]):
                      if output_grid[row, col] != output_color:
                          output_grid[row, col] = 0  # Set to white
            else: #copy cropped object colors
                for row in range(output_grid.shape[0]):
                    for col in range(output_grid.shape[1]):
                        if output_grid[row,col] != input_color:
                          output_grid[row, col] = 0
        else:
          output_grid = cropped_input.copy()

    else: #test input, so no expected output
        input_color = get_object_color(input_grid, target_object_coords)
        output_grid = cropped_input.copy()
        for row in range(output_grid.shape[0]):
            for col in range(output_grid.shape[1]):
                if output_grid[row,col] != input_color:
                    output_grid[row, col] = 0


    return output_grid
```
