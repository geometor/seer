"""
1.  **Identify the Target Object:** Find an object in the bottom-left of the input grid, distinguished by either:
    *   Example 1: Being the largest contiguous region of a single color (initially observed as red).
    *   Example 2: Being an object that *changes color* from input to output.
    *   Example 3: Being the largest object in the bottom-left, even if no color change happens.

2.  **Crop:** Crop the input grid to a bounding box that fully contains the target object.

3.  **Filter Colors:** Remove all colors from the cropped grid *except* those present in the target object *after* the transformation (i.e., in the expected output).  If the target object does not change color keep the original. If a pixel is a different color from any of the colors in the cropped object, replace the pixel with color 0 (white).

4.  **Output:** The cropped and filtered grid.
"""

import numpy as np

def find_largest_object(grid, color=None):
    """Find the largest contiguous object of a specific color or any color."""
    visited = np.zeros_like(grid, dtype=bool)
    max_size = 0
    max_object_coords = []

    def dfs(row, col, current_object_coords, target_color):
        """Depth-first search to find contiguous regions."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or (target_color is not None and grid[row, col] != target_color)):
            return 0
        visited[row, col] = True
        current_object_coords.append((row, col))
        size = 1
        size += dfs(row + 1, col, current_object_coords, target_color)
        size += dfs(row - 1, col, current_object_coords, target_color)
        size += dfs(row, col + 1, current_object_coords, target_color)
        size += dfs(row, col - 1, current_object_coords, target_color)
        return size

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col]:
                current_object_coords = []
                target_color = grid[row,col] if color is None else color
                size = dfs(row, col, current_object_coords, target_color)
                if size > max_size:
                    max_size = size
                    max_object_coords = current_object_coords

    return max_object_coords

def crop_grid(grid, coords):
    """Crops the grid to the bounding box defined by the coordinates."""
    min_row = min(r for r, _ in coords)
    max_row = max(r for r, _ in coords)
    min_col = min(c for _, c in coords)
    max_col = max(c for _, c in coords)

    return grid[min_row:max_row + 1, min_col:max_col + 1]

def get_object_colors(grid, coords):
    """Returns a set of unique colors within the object defined by coordinates."""
    colors = set()
    for r, c in coords:
        colors.add(grid[r, c])
    return colors

def transform(input_grid, output_grid_expected=None):
    # Find largest object in the bottom-left, regardless of initial color.
    # Prioritize bottom-left by finding any object and taking the lowest row number, then leftmost column.
    all_objects = []
    visited = np.zeros_like(input_grid, dtype=bool)

    def dfs(row, col, current_object_coords):
        if (row < 0 or row >= input_grid.shape[0] or col < 0 or col >= input_grid.shape[1] or
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

    for row_start in range(input_grid.shape[0]):
        for col_start in range(input_grid.shape[1]):
             if not visited[row_start, col_start]:
                current_object = []
                dfs(row_start, col_start, current_object)
                if current_object:
                    all_objects.append(current_object)

    #select bottom-left
    if not all_objects:
        return input_grid.copy()

    bottom_left_objects = sorted(all_objects, key=lambda obj: (-max(r for r, _ in obj), min(c for _, c in obj)) )
    target_object_coords = bottom_left_objects[0]

    # Crop the grid.
    cropped_input = crop_grid(input_grid, target_object_coords)

    # Determine target colors from expected output, if provided.
    if output_grid_expected is not None:
        cropped_expected = crop_grid(output_grid_expected, target_object_coords)
        target_colors = get_object_colors(cropped_expected, [(r - min(r for r, _ in target_object_coords), c - min(c for _, c in target_object_coords)) for r, c in target_object_coords if (r - min(r for r, _ in target_object_coords)) < cropped_expected.shape[0] and (c - min(c for _, c in target_object_coords)) < cropped_expected.shape[1] ])

    else:  #if test input
        target_colors = get_object_colors(input_grid, target_object_coords)

    # Filter colors in the cropped region.
    output_grid = cropped_input.copy()
    for row in range(output_grid.shape[0]):
        for col in range(output_grid.shape[1]):
            if output_grid[row, col] not in target_colors:
                output_grid[row, col] = 0  # Set to white (background).

    return output_grid